#!/usr/bin/env python3
print("This will change your MAC Address temprerly")
print("Enter eth0 or wlan0 or lo in interface")
print("Enter anything in MAC syntax 11:22:33:44:11:22")
import subprocess as sb
import optparse as ops


print("Created by Anonymousboy")
print("Subscribe to Anonymous Boy Youtube Channel")
interface = input("enter interface > ")
new_mac = input("enter new MAC > ")

print(f"[+] Changing MAC address for {interface} to {new_mac}")


sb.call(["sudo", "ifconfig", interface, "down"])
sb.call(["sudo", "ifconfig", interface, "hw","ether",new_mac])
sb.call(["sudo","ifconfig", interface, "up"])
sb.call(["sudo" , "ifconfig", interface])
