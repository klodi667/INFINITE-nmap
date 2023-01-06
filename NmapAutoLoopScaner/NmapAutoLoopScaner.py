#!/usr/bin/python3

import nmap
import time
import datetime
scanner = nmap.PortScanner()
print("Welcome, this is a simple nmap automation tool")
print("Nmap Version: ", scanner.nmap_version())
print("<------------------------------------------------>")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

port = input("Please enter the Port you want to scan(example: 1-1024): ")
print("The Port you entered is: ", port)
type(port)

option = input("Please enter the NmapOption you want to scan(example: -v -sS): ")
print("The NmapOption you entered is: ", option)
type(option)

looptime = float(input("Prease enter how frequently you want to scan (minutes): "))
print("Scaning frequently is {} minutes once".format(looptime))

count = int(input("How many you want to scan: "))
print("The scan count is ", count)


for i in range(count):
    dt = datetime.datetime.now()
    print("Current time　", dt)
    print("Please wait...")
    scanner.scan(ip_addr, port, option)
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    for pro in scanner[ip_addr].all_protocols():
        print("<------------------------------------------------>")
        print(pro)
        print("Open Port: ", scanner[ip_addr][pro].keys())

    print("<------------------------------------------------>")
    print("Scaning frequently is {} minutes once".format(looptime))
    if i != (count - 1):
        print("Scaned", i + 1, "time, After ", count - (i + 1), " scan to end")
        print("Please wait until the next... or ctrl + c to exit")
        time.sleep(looptime * 60)

print("end")
