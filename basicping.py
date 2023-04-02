import os
import re
import requests

def ping(host):
    response = os.system("ping -c 1 " + host)
    return response == 0

site = input("Enter the site address: ")

if ping(site):
    print("The site is active!")
else:
    print("The site is not active.")

ping_times = []
for i in range(5):
    ping_response = os.popen(f"ping -c 1 {site}").read()
    ping_time = re.search(r"time=(\d+\.\d+) ms", ping_response)
    if ping_time:
        ping_times.append(float(ping_time.group(1)))
if ping_times:
    print(f"Ping response time: {sum(ping_times)/len(ping_times)} ms")


servers = ["www." + site, "mail." + site, "ns1." + site, "ns2." + site]
countries = []
for server in servers:
    server_ip = os.popen(f"nslookup {server}").read().split()[-1]
    try:
        r = requests.get(f"http://ip-api.com/json/{server_ip}")
        country = r.json()['country']
        if country not in countries:
            countries.append(country)
    except:
        pass

if countries:
    print("Countries where the site's servers are located: ")
    for country in countries:
        print(country)
else:
    print("Server information not found.")
