import re
import subprocess
from influxdb import InfluxDBClient

## Replace the [ID] placeholder below with the server ID you want to run the speedtest to.
response = subprocess.Popen('/usr/bin/speedtest --accept-license --accept-gdpr -s [ID]', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

server = re.search('Server:\s+(.*?)\s', response, re.MULTILINE)
sid = re.search('id \=\s+(.*?)\)\s', response, re.MULTILINE)
isp = re.search('ISP:\s+(.*?)\s', response, re.MULTILINE)
ping = re.search('Latency:\s+(.*?)\s', response, re.MULTILINE)
download = re.search('Download:\s+(.*?)\s', response, re.MULTILINE)
upload = re.search('Upload:\s+(.*?)\s', response, re.MULTILINE)
jitter = re.search('\((.*?)\s.+jitter\)\s', response, re.MULTILINE)
pl = re.search('Packet Loss:\s+(.*?)\s', response, re.MULTILINE)
result = re.search('Result URL:\s+(.*?)\s', response, re.MULTILINE)


server = server.group(1)
sid = sid.group(1)
isp = isp.group(1)
ping = ping.group(1)
download = download.group(1)
upload = upload.group(1)
jitter = jitter.group(1)
pl = pl.group(1)
result = result.group(1)

speed_data = [
    {
        "measurement" : "internet_speed",
        "tags" : {
            "host": "home.classicyuppie.com"
        },
        "fields" : {
            "download": float(download),
            "upload": float(upload),
            "ping": float(ping),
            "jitter": float(jitter),
            "pl": str(pl),
            "server": str(server),
            "sid": str(sid),
            "isp": str(isp),
            "result": str(result)
        }
    }
]

## Change the influxdb-user', 'passwd', and 'db-name' fields to your specific values below.
client = InfluxDBClient('localhost', 8086, 'influxdb-user', 'passwd', 'db-name')

client.write_points(speed_data)
