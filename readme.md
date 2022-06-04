<div id="top"></div>
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<div align="center">
<a href="https://github.com/Falc0n2k/speedtest-dashboard/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/falc0n2k/speedtest-dashboard?style=for-the-badge"></a>
<a href="https://github.com/Falc0n2k/speedtest-dashboard/network/members"><img alt="GitHub forks" src="https://img.shields.io/github/forks/falc0n2k/speedtest-dashboard?style=for-the-badge"></a>
<a href="#"><img alt="GitHub repo stars" src="https://img.shields.io/github/stars/falc0n2k/speedtest-dashboard?style=for-the-badge"></a>
<a href="https://github.com/Falc0n2k/speedtest-dashboard/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues-raw/falc0n2k/speedtest-dashboard?style=for-the-badge"></a>
<a href="https://github.com/Falc0n2k/speedtest-dashboard/blob/main/LICENSE.txt"><img alt="GitHub" src="https://img.shields.io/github/license/falc0n2k/speedtest-dashboard?style=for-the-badge"></a>
</div>

<br/>
<br/>

<h1 align="center">Speed Monitor Dashboard</h1>
<p align="center">A lightweight Grafana dashboard that reports results from Ookla's speedtest-cli.</p>
</div>

<br/>
<br/>

<!-- ABOUT THE PROJECT -->
## About The Project

<img src="/images/dashboard.png" width="75%" height="75%">

### Built With

* [JSON](https://www.json.org/)

### Dependancies

* Ookla's [speedtest-cli](https://www.speedtest.net/apps/cli) application
* [Python 3](https://www.python.org/download/releases/3.0/)
* [InfluxDB](https://www.influxdata.com)
* [Grafana](https://grafana.com)
* Patience


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

For the best experience, please make sure you have the speedtest-cli script working, and InfluxDB and Grafana installed. This dashboard will do nothing until you have basic functionality and data storage in place first. If you need detailed instructions on how to do that, you can follow
the [Dependancy Primer](dependancy-primer.md).

### Installation

1. Install the dashboard using the JSON config file (`config.json`) logging into Grafana and hovering over the plus (+) icon in the left sidebar, clicking **Import**. Copy and paste the entire contents of `config.json` into the **Import via panel json**, then click **Load**.

2. If this is a fresh install for you - meaning you've set the speedtest-cli script up from scratch along with InfluxDB and Grafana, now is a good time to test the ingest from the scrip to the database, seeing how the dashboard presents that data to you. To do this, you can spam `python3 speedtest.py` a few times on the command line (I recommend at least three or four passes). Once those test results are stored in the database, you can customize the rest of the dashboard to your liking.

3. As the final step, you'll want to set the speedtest script to run at an interval you're comfortable with, automatically. To do this, we'll use `crontab -e`. If this is the first time you're running it, or you have a fresh install of Linux, do yourself a favor us select Nano as your editor. I run my speedtest every 30 minutes, but you may consider running it every hour or less if you're on a metered connection or your ISP has a data limitation. For a sample of the format you'll want to use:

##### 30-minute interval
```
# m h  dom mon dow   command
*/30 * * * * python3 /home/pi/speedtest.py
```

##### 60-minute interval
```
# m h  dom mon dow   command
*/60 * * * * python3 /home/pi/speedtest.py
```

##### 2-hour interval
```
# m h  dom mon dow   command
*/120 * * * * python3 /home/pi/speedtest.py
```

N.B. - customize the directory where you have your Python script sitting. `pwd` and `ls -l` are your friends.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE.txt](/LICENSE.txt) for more information.


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [PiUpMyLife](https://piupmylife.com/)
* [@djshadowxm82](https://github.com/djshadowxm82), for inspiring me to learn Python.
