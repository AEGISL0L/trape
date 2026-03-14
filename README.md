trape (stable) v2.1
========

People tracker on the Internet: Learn to track the world, to avoid being traced.

---
Trape is an **OSINT** analysis and research tool, which allows people to track and execute intelligent **social engineering** attacks in real time. It was created with the aim of teaching the world how large Internet companies could obtain **confidential information** such as the status of sessions of their websites or services and control their users through their browser, without their knowledge, but It evolves with the aim of helping **government** organizations, companies and **researchers** to track the cybercriminals.

![--trape header](https://i.imgur.com/2ycpXEj.png)


At the beginning of the year 2018 was presented at **BlackHat Arsenal in Singapore**: https://www.blackhat.com/asia-18/arsenal.html#jose-pino and in multiple security events worldwide.

> **Note:** This fork removes all dependencies on external proprietary services (Google Maps, ngrok, ipgeolocation.io, etc.). The tool is now fully self-contained — no API keys required.

Changes from upstream
-----------

| Removed dependency | Replacement |
|---|---|
| Google Maps JS API | [Leaflet.js](https://leafletjs.com/) + [OpenStreetMap](https://www.openstreetmap.org/) tiles |
| Google Geocoding API | [Nominatim](https://nominatim.openstreetmap.org/) (OpenStreetMap) |
| Google Geolocation API | Browser native geolocation |
| Google Directions API | [OSRM](https://project-osrm.org/) public router + straight-line fallback |
| ngrok | Removed (use your own tunneling if needed) |
| ipgeolocation.io / ipinfo.io | Local `/geoip` endpoint with [MaxMind GeoLite2](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data) |
| Google URL Shortener (goo.gl) | Removed (API dead since 2019) |
| Wikimedia Commons (speed test image) | Local `speedtest.bin` file |
| cdnjs.cloudflare.com (IE polyfills) | Removed (IE 6-9 no longer supported) |
| Google connectivity check | Socket to `1.1.1.1:53` |
| GitHub version check | Removed |
| responsiveVoice.js | [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API) (built into modern browsers) |

Some benefits
-----------
* **LOCATOR OPTIMIZATION:** Trace the path between you and the target you're tracking. Each time you make a move, the path will be updated, the location of the target is obtained silently through a bypass made in the browsers, allowing you to skip the location request on the victim's side, and at the same time maintain a precision of **99%** in the locator.

![](https://lh3.googleusercontent.com/qwq4LzzLTdFGwsGd8C3c9gxbDaN191s7lnvz75y0trwIMUGSaIu22QyBRgwKXxRwLBC5HGekBJLw9qgD5lnxgszcFVqJ24RVqv3q_T3HzD6wJeQU6oY4VVF8QT6Y83hstqD4C020)
* **APPROACH:** When you're close to the target, Trape will tell you.

![](https://lh4.googleusercontent.com/NFnVGLoDF2BmM_N56w8Vf6cnyg1WWIIKgGC1MeBTKXxcIynMDfC1ZSu43ftoiYnwcBb2gjpVdS4y0zm5K7XAzvXf7bPIt5ZrWQCEq9eQuN8KL-SRPOtBgIZL53AWkJjwhC4gJUcG)

*  **REST API:** Generates an API (random or custom), and through this you can control and monitor other Web sites on the Internet remotely, getting the traffic of all visitors.

![](https://lh6.googleusercontent.com/DtQiYYLoL9di3LPcSSTCZ3AuVMlQaNcDkBdv_fZFX7rztjg_epWmIaA2AlGsWCr5Mwr2nVfLcsg1I5PXEcx87ErLS8JaruvRsEUIkScydXA3JhvbsmJov7qxbKooGgD5u32kmBHW)

* **PROCESS HOOKS:** Manages social engineering attacks or processes in the target's browser.

  --- **SEVERAL:** You can issue a phishing attack of any domain or service in real time as well as send malicious files to compromise the device of a target.


  ---  **INJECT JS:** You keep the JavaScript code running free in real time, so you can manage the execution of a **keylogger** or your own custom functions in JS which will be reflected in the target's browser.

  ---   **SPEECH:** A process of audio creation is maintained which is played in the browser of the target, by means of this you can execute personalized messages in different voices with languages in Spanish and English. *(Now powered by the browser's native Web Speech API — no external library needed.)*




* **CLICK ATTACK TO GET CREDENTIALS:** Automatically obtains the target credentials, recognizing your connection availability on a social network or Internet service.

![](https://lh4.googleusercontent.com/IN8xWfHjGPRQ__-QwTXebG-087m4JzDIVFWtSlUtrnRpDn2d0U1cnQdNGqLQZA35-fneej1iTpkxgHZCq_pWZLlCd1SmyLZ-WJ5Juj2KbtyNbX4jI1oLUtqupxieH91mX65_ZmHy)

* **NETWORK:** You can get information about the user's network.

  ---  **SPEED:** Viewing the target's network speed. (Ping, download, upload, type connection)

  --- **HOSTS OR DEVICES:** Here you can get a scan of all the devices that are connected in the target network automatically.

![](https://lh3.googleusercontent.com/gkOWunWn7ge5yJt00lMBN_7GwSUxrAQV2y64ysyrjmD-vz_lO3bu6UkRjPJF8OljxyMTNlWVA9W8gVU3U0iI3RrECNNkr7H44Lz6z5Zj3-bA_hDF5TnTSoV_6584qFvuLkmShTQD)


* **PROFILE:** Brief summary of the target's behavior and important additional information about your device.

  ---   **GPU**
  ---   **ENERGY**

30-session recognition
-------
Session recognition is one of trape most interesting attractions, since you as a researcher can know remotely what service the target is connected to.

![](https://lh6.googleusercontent.com/IFxIh7Eemr63kycj2eBzJYvevCzLH5DkQGWUKzPx_Okn4WoExPl0LR7Qj-cSc0WF0rs9Ew6DJMwcyirZd0kdfLpdrqQ2700P_xdxW7wpZ7K6OWi8pluLKivHtU45HD4VtyM0lLwh)

* **USABILITY:** You can delete logs and view alerts for each process or action you run against each target.

 ![](https://lh4.googleusercontent.com/dXx1lRG2z-ZlSIlQyTx_ra7sbkgKG2jeqGjIt86GebFiAaZyFDA4vy3QBLACd-1wOz4zdSIARWvo3hK2mEvrSJ6VPDSiOZgMLB4rUYXKDHrone0xIB3bwhAKPnsJUcuKW9xf_-sG)

How to use it
-------
 First unload the tool.
```
git clone https://github.com/AEGISL0L/trape.git
cd trape
python3 trape.py -h
```
If it does not work, try to install all the libraries that are located in the file **requirements.txt**
```
pip3 install -r requirements.txt
```

Example of execution
```
Example: python3 trape.py --url http://example.com --port 8080
```

If you face some problems installing the tool, it is probably due to Python versions conflicts, you should run a Python 3 virtual environment:

```
pip3 install virtualenv
virtualenv -p /usr/bin/python3 trape_env
source trape_env/bin/activate
pip3 install -r requirements.txt
python3 trape.py -h
```

GeoIP setup (optional)
-------
For IP geolocation, download the free **MaxMind GeoLite2-City** database:

1. Register at [MaxMind](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data)
2. Download `GeoLite2-City.mmdb`
3. Place it in the trape root directory (or specify a custom path during first-run configuration)

If no `.mmdb` file is present, GeoIP lookups will return "Unknown" — the tool still works.

**HELP  AND OPTIONS**
```
user:~$ python3 trape.py --help
usage: python3 trape.py -u <<Url>> -p <<Port>> [-h] [-u URL] [-p PORT]
                                              [-ak ACCESSKEY] [-l LOCAL]
                                              [-ic INJC] [-ud]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Put the web page url to clone
  -p PORT, --port PORT  Insert your port
  -ak ACCESSKEY, --accesskey ACCESSKEY
                        Insert your custom key access
  -l LOCAL, --local LOCAL
                        Insert your home file
  -ic INJC, --injectcode INJC
                        Insert your custom REST API path
  -ud, --update         Update trape to the latest version
```

**--url**  In this option you add the URL you want to clone, which works as a decoy.

**--port**  Here you insert the port, where you are going to run the  **trape server**.

**--accesskey**  You enter a custom key for the  **trape panel**, if you do not insert it will generate an  **automatic key**.

**--injectcode**  trape contains a  **REST API**  to play anywhere, using this option you can customize the name of the file to include, if it does not, generates a random name allusive to a token.

**--local**  Using this option you can call a local **HTML file**, this is the replacement of the  **--url**  option made to run a local lure in trape.

**--version**  You can see the version number of trape.

**--update**  Option used to upgrade to the latest version of **trape**.

**--help**  It is used to see all the above options, from the executable.


Disclaimer
-------
This tool has been published educational purposes. It is intended to teach people how bad guys could track them, monitor them or obtain information from their credentials, we are not responsible for the use or the scope that someone may have through this project.

We are totally convinced that if we teach how vulnerable things really are, we can make the Internet a safer place.

Developer
-------
This development and others, the participants will be mentioned with name, Twitter and charge.

* **CREATOR**

  --- Jose Pino - [@jofpin](https://twitter.com/jofpin) - (**Security Researcher**)


Happy hacking!
-------
I invite you, if you use this tool helps to share, collaborate. Let's make the Internet a safer place, let's report.


## License

The content of this project itself is licensed under the [Creative Commons Attribution 3.0 license](http://creativecommons.org/licenses/by/3.0/us/deed.en_US), and the underlying source code used to format and display that content is licensed under the [MIT license](http://opensource.org/licenses/mit-license.php).

Copyright, 2018 by [Jose Pino](https://twitter.com/jofpin)

-------------
