# Dependancy Primer

## Bare metal dependancies

1. Install three dependancies with: `sudo apt-get update && sudo apt-get upgrade && sudo apt install apt-transport-https gnupg1 dirmngr`.
2. Fetch the keychain so that you can download the SpeedTest command line interface to your device: `curl -L https://packagecloud.io/ookla/speedtest-cli/gpgkey | gpg --dearmor | sudo tee /usr/share/keyrings/speedtestcli-archive-keyring.gpg >/dev/null`.
3. Add the Ookla repository to `dpkg` with `echo "deb [signed-by=/usr/share/keyrings/speedtestcli-archive-keyring.gpg] https://packagecloud.io/ookla/speedtest-cli/debian/ $(lsb_release -cs) main" | sudo tee  /etc/apt/sources.list.d/speedtest.list`.
4. Now it's time to install the SpeedTest package: `sudo apt update && sudo apt install speedtest`.
5. Verify the package is working with a quick `speedtest`. Upon first run, you'll be prompted to accept the terms and conditions by typing `YES`.

## Create the `speedtest.py` configuration file

1. Do `sudo mkdir ~/speedtest && cd speedtest/` and place the `speedtest.py` file in this directory with `sudo wget https://github.com/falc0n2k/speedtest-dashboard/speedtest.py`. Now would be a good time to review the comments in that file to ensure you'll be running the speedtest to the server closest to you. 

As a point of reference, you'll want to use servers that are on the same ISP as you for optimum results, e.g. If Xfinity is your ISP, use Comcast server. If you have FiOS, try to use a Verizon server, if available. The reason for this is less hops decreasing latency on your test.

2. To determine the top 10 closest servers to you, simply invoke `speedtest -L` and take note of the ID you want to use. In the Python script, replace the comment with the server ID. Please note that you can only run one server in the script and not between a selection of servers at this time.

<img src="/images/speedtest-L.png" width="100%" height="100%">

## Install InfluxDB and configure it

1. Add the keys to your system's keychain. `sudo apt update && sudo apt upgrade && curl https://repos.influxdata.com/influxdb.key | gpg --dearmor | sudo tee /usr/share/keyrings/influxdb-archive-keyring.gpg >/dev/null`

2. Add the required fetch points to your Sources list:

    2a. If you're running Raspbian / Raspi OS: `echo "deb [signed-by=/usr/share/keyrings/influxdb-archive-keyring.gpg] https://repos.influxdata.com/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/influxdb.list`
    2b. If you're running Ubuntu: `echo "deb [signed-by=/usr/share/keyrings/influxdb-archive.keyring.gpg] https://repos.influxdata.com/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/influxdb.list`

Update the package list again and install InfluxDB: `sudo apt update && sudo apt install influxdb`. Set InfluxDB to run on boot with `sudo systemctl unmask influxdb && sudo systemctl enable influxdb`, and then finally `sudo systemctl start influxdb` to launch it.

3. Set up InfluxDB. At a clean prompt, execute `influx` followed by `CREATE DATABASE internetspeed`. Feel free to rename the database to something easy to remember for *you*, just take note of it for finishing the Python configuration. Next, create the user and set the password with `CREATE USER "speedmonitor" WITH PASSWORD 'passwd'`. A final `GRANT ALL ON "internetspeed" to "speedmonitor"` will make sure that the user you just created has the necessary permissions in the database you made. Type `quit` to exit InfluxDB.

4. To get Python to play nice with InfluxDB, run `sudo apt install python3-influxdb`.

## Install Grafana and configure it

1. Before you can install Grafana, you'll need to add the keychain and repo to your device: `sudo apt update && sudo apt upgrade && curl https://packages.grafana.com/gpg.key | gpg --dearmor | sudo tee /usr/share/keyrings/grafana-archive-keyrings.gpg >/dev/null && echo "deb [signed-by=/usr/share/keyrings/grafana-archive-keyrings.gpg] https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list`.

2. Now you can install Grafana with `sudo apt update && sudo apt install grafana`. To set Grafana to run at boot, `sudo systemctl enable grafana-server`.

3. Start the Grafana service with `sudo systemctl start grafana-server`. 

4. Visit `IPADDRESS:3000` to access Grafana. The first time you do, you'll go through the new user prompts. The default credentials are `admin` for both the username and password. While it's possible to skip this step I do not recommend it, especially if you're installing Grafana on a public-facing server.

5. Once you're in, add a new data source by hovering over the gear icon in the left sidebar and click on **Data Sources**. Click **Add data source** on the following page. Select **InfluxDB**. Use `http://localhost:8086` for the server and enter in the InfluxDB credentials in the **Details** section (you created these earlier in Step 4 of the previous section of this guide). Click **Save & Test**.

## Install the dashboard

Once you've completed these steps, you can return to the [installation instructions section](readme.md#Installation) and follow the installation steps for the dashboard itself.