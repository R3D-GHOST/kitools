#/bin/python/
#librerias 
import os, time
import subprocess 
#Colores
negro = '\033[30m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
rosado = '\033[35m'
calipso= '\033[36m'
blanco = '\033[37m'
cierre = '\033[39m'
#banner
banner = """

 _  ___ _____ _____ ___   ___  _     ____  
| |/ (_)_   _|_   _/ _ \ / _ \| |   / ___| 
| ' /| | | |   | || | | | | | | |   \___ \ 
| . \| | | |   | || |_| | |_| | |___ ___) |
|_|\_\_| |_|   |_| \___/ \___/|_____|____/ 
                                           

"""
print(rojo+banner)
time.sleep(0.5)
print("")
#menu
print(verde+"1 ->> OSINT")
print(verde+"2 ->> Hacking Web")
print(verde+"3 ->> Wifi Hacking")
print(amarillo+"4 ->> Exit")
opt_menu = input(rojo+">>> ")
if opt_menu == "1":
    os.system('clear')
    time.sleep(1)
    print(amarillo+"1 ->> Mr-Holmes")
    print(amarillo+"2 ->> Sherlock")
    opt_1 = input(">>> ")
    if opt_1 == "1":
        os.system('git clone https://github.com/Lucksi/Mr.Holmes')
    elif opt_1 == "2":
        os.system('git clone https://github.com/sherlock-project/sherlock.git')
elif opt_menu == "2":
    os.system('clear')
    time.sleep(1)
    print("1 ->> SQLMAP")
    print("2 ->> NMAP")
    opt_2 = input(">>> ")
    if opt_2 == "1":
        os.system('git clone https://github.com/sqlmapproject/sqlmap.git')
    elif opt_2 == "2":
        os.system('sudo apt install nmap')
elif opt_menu == "3":
    time.sleep(1)
    os.system('clear')
    print("1 ->> Aircrack-ng")
    print("2 ->> Bettercap")
    print("3 ->> Wireshark")
    opt_3 = input(">>> ")
    if opt_3 == "1":
        os.system('git clone https://github.com/aircrack-ng/aircrack-ng.git')
    elif opt_3 == "2":
        os.system('sudo apt install bettercap')
    elif opt_3 == "3":
        os.system('sudo apt install wireshark')
elif opt_menu == "4":
    time.sleep(1)
    os.system('clear')
    exit()
    