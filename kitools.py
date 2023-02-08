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
#almacen de tools
os.system('mkdir tools')
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
print(verde+"4 ->> Tools Extra")
print(amarillo+"5 ->> Exit")
opt_menu = input(rojo+">>> ")
if opt_menu == "1":
    os.system('clear')
    time.sleep(1)
    print(amarillo+"1 ->> Mr-Holmes")
    print(amarillo+"2 ->> Sherlock")
    print(azul+"3 ->> Maigrit")
    print(rojo+"4 ->> Phoneinfoga")
    print(verde+"5 ->> Phishing")
    print(verde+"6 ->> The-Ghost-Seeker")
    opt_1 = input(">>> ")
    if opt_1 == "1":
        os.system('cd tools ; git clone https://github.com/Lucksi/Mr.Holmes')
    elif opt_1 == "2":
        os.system('cd tools ; git clone https://github.com/sherlock-project/sherlock.git')
    elif opt_1 == "3":
        os.system('sudo pip3 install maigret')
    elif opt_1 == "4":
        os.system('cd tools ; curl -sSL https://raw.githubusercontent.com/sundowndev/phoneinfoga/master/support/scripts/install | bash ')
    elif opt_1 == "5":
        os.system('cd tools ; git clone https://github.com/DeepSociety/AIOPhish.git')
    elif opt_1 == "6":
        os.system('cd tools ; git clone https://github.com/R3D-GHOST/The-Ghost-Seeker.git')
elif opt_menu == "2":
    os.system('clear')
    time.sleep(1)
    print("1 ->> Sqlmap")
    print("2 ->> Nmap")
    print("3 ->> Burpsuite")
    print("4 ->> Whatweb")
    print("5 ->> Scan-Web")
    opt_2 = input(">>> ")
    if opt_2 == "1":
        os.system('cd tools ; git clone https://github.com/sqlmapproject/sqlmap.git')
    elif opt_2 == "2":
        os.system('sudo apt install nmap')
    elif opt_2 == "3":
        os.system('sudo apt install burpsuite')
    elif opt_2 == "4":
        os.system('sudo apt install whatweb')
    elif opt_2 == "5":
        os.system('cd tools ; git clone https://github.com/R3D-GHOST/Scan-Web.git')
elif opt_menu == "3":
    time.sleep(1)
    os.system('clear')
    print("1 ->> Aircrack-ng")
    print("2 ->> airgeddon")
    print("3 ->> Wifite")
    opt_3 = input(">>> ")
    if opt_3 == "1":
        os.system('cd tools ; git clone https://github.com/aircrack-ng/aircrack-ng.git')
    elif opt_3 == "2":
        os.system('sudo apt install airgeddon')
    elif opt_3 == "3":
        os.system('sudo apt install wifite')
elif opt_menu == "4":
    print("1 ->> Bettercap")
    print("2 ->> Wireshark")
    opt_4 = input(">>> ")
    if opt_4 == "1":
        os.system('sudo apt install bettercap')
    elif opt_4 == "2":
        os.system('sudo apt install wireshark')
elif opt_menu == "5":
    time.sleep(1)
    os.system('clear')
    exit()
else:
    print("Error Opcion no valida")
