#!/usr/bin/env python

import subprocess
import optparse
import re


def get_arguments():
	parser =  optparse.OptionParser()	
	parser.add_option("-i", "--interface", dest="interface", help="interface for your network to change its Mac (MAC CHANGER V -1.2 BY TECH BHAI VEDANT)")
	parser.add_option("-m", "--mac", dest="new_mac", help="Put your New MAC address (MAC CHANGER V -1.2 BY TECH BHAI VEDANT)")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error("[-] Please Specify a Interface --help for help")
	elif not options.new_mac:
		parser.error("[-] Please Specify a Valid MAC --help for help")
	return options


def change_mac(interface, new_mac):
	print("[+] Changing MAC address for " + interface + " to " + new_mac)	
	subprocess.call(["sudo","ifconfig", interface ,"down"])
	subprocess.call(["sudo","ifconfig", interface ,"hw","ether", new_mac])
	subprocess.call(["sudo","ifconfig", interface ,"up"])

def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["sudo","ifconfig", interface])
	mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
	
	if mac_address_search_result:
		return mac_address_search_result.group(0)
	else:
		print("[-]NOT Valid --help for more info")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current_MAC = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
	print("[+]MAC Changed Sucessfully to " + current_mac)
else:
	print("[-]MAC Does Not Get Changed ")
print("By Tech Bhai Vedant")
print("""

Subscribe here for more stuff

https://youtube.com/c/TechBhaiVedantindia

	""")