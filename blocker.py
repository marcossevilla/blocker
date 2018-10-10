import time
from datetime import datetime as dt

'''
    Following lines: location of host file,
    name of temporal file (hosts),
    I.P for redirection,
    default websites to block.
'''

hosts_path = "/etc/hosts"
hosts_temp = "hosts"
redirect = "127.0.0.1"
websites = []

many_websites = int(input("How many websites do you want to start blocking? "))
print("Input the websites...\n")

for i in range(many_websites):
	website = str(input()) 
	websites.append(website)

while True:

    # date comparing interval to know if right now is working time
    working = dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year,
    dt.now().month, dt.now().day, 16)

    if working:
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    else:
        print("Less fun hours...")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()

    time.sleep(5)
