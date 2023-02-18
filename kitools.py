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
print(verde+"4 ->> Spoofing")
print(verde+"5 ->> DDoS")
print(verde+"6 ->> Phishing")
print(verde+"7 ->> Hacking Android")
print(verde+"8 ->> T00LS +")
print(rojo+"9 ->> Exit")
opt_menu = input(rojo+">>> ")
if opt_menu == "1":
    os.system('clear')
    time.sleep(1)
    print(azul)
    print("1 ->> Mr-Holmes")
    print("2 ->> Sherlock")
    print("3 ->> Maigrit")
    print("4 ->> Phoneinfoga")
    print("5 ->> The-Ghost-Seeker")
    print("6 ->> Osintgram")
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
        os.system('cd tools ; git clone https://github.com/R3D-GHOST/The-Ghost-Seeker.git')
    elif opt_1 == "6":
        os.system('cd tools ; git clone https://github.com/Datalux/Osintgram')
elif opt_menu == "2":
    os.system('clear')
    print(amarillo)
    print("1 ->> Sqlmap")
    print("2 ->> Nmap")
    print("3 ->> Burpsuite")
    print("4 ->> Whatweb")
    print("5 ->> Scan-Web")
    print("6 ->> RED_HAWK")
    print("7 ->> Spartan")
    print("8 ->> WebMap")
    print("9 ->> Eternalview")
    print("10 ->> BlackWidow")
    print("11 ->> Reconftw")
    print("12 ->> Doks-eye")
    print("13 ->> Sql-Scanner")
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
    elif opt_2 == "6":
        os.system('cd tools ; git clone https://github.com/Tuhinshubhra/RED_HAWK.git')
    elif opt_2 == "7":
        os.system('apt-get install legion')
    elif opt_2 == "8":
        os.system('cd tools ; git clone https://github.com/Anteste/WebMap.git')
    elif opt_2 == "9":
        os.system('cd tools ; git clone https://github.com/rpranshu/EternalView.git')
    elif opt_2 == "10":
        os.system('cd tools ; git clone https://github.com/1N3/BlackWidow.git')
    elif opt_2 == "11":
        os.system('cd tools ; git clone https://github.com/six2dez/reconftw.git')
    elif opt_2 == "12":
        os.system('cd tools ; git clone https://github.com/BullsEye0/dorks-eye.git')
    elif opt_2 == "13":
        os.system('cd tools ; git clone https://github.com/Bitwise-01/SQL-scanner.git')
elif opt_menu == "3":
    os.system('clear')
    print(calipso)
    print("1 ->> Aircrack-ng")
    print("2 ->> Airgeddon")
    print("3 ->> Wifite")
    print("4 ->> WiFi-Pumpkin")
    print("5 ->> WI-TOOLKIT")
    print("6 ->> Air-Kit")
    print("7 ->> Evillimiter")
    opt_3 = input(">>> ")
    if opt_3 == "1":
        os.system('cd tools ; git clone https://github.com/aircrack-ng/aircrack-ng.git')
    elif opt_3 == "2":
        os.system('sudo apt install airgeddon')
    elif opt_3 == "3":
        os.system('sudo apt install wifite')
    elif opt_3 == "4":
        os.system('cd tools ; git clone https://github.com/P0cL4bs/WiFi-Pumpkin.git')
    elif opt_3 == "5":
        os.system('cd tools ; git clone https://github.com/mkdirlove/WI-TOOLKIT.git')
    elif opt_3 == "6":
        os.system('cd tools ; git clone https://github.com/mkdirlove/AIR-KIT.git')
    elif opt_3 == "7":
        os.system('cd tools ; git clone https://github.com/bitbrute/evillimiter.git')
elif opt_menu == "4":
    os.system('clear')
    print(rosado)
    print("1 ->> Bettercap")
    print("2 ->> SMS Anon")
    print("3 ->> SMS GHOST")
    print("4 ->> God-Killer")
    opt_4 = input(">>> ")
    if opt_4 == "1":
        os.system('sudo apt install bettercap')
    elif opt_4 == "2":
        os.system('cd tools ; git clone https://github.com/HACK3RY2J/Anon-SMS.git')
    elif opt_4 == "3":
        os.system('cd tools ; git clone https://github.com/R3D-GHOST/SMS-GHOST.git')
    elif opt_4 == "4":
        os.system('cd tools ; git clone https://github.com/FDX100/GOD-KILLER.git')
elif opt_menu == "5":
    os.system('clear')
    print(cierre)
    print("1 ->> DDoS RIPPER ")
    print("2 ->> DDoS-Network")
    print("3 ->> SlowHttptest")
    opt_5 = input(">>> ")
    if opt_5 == "1": 
        os.system('cd tools ; git clone https://github.com/palahsu/DDoS-Ripper.git')
    elif opt_5 == "2":
        os.system('cd tools ; git clone https://github.com/R3D-GHOST/DDoS-Network.git')
    elif opt_5 == "3":
        os.system('sudo apt install slowhttptest')
elif opt_menu == "6":
    os.system('clear')
    print(blanco)
    print("1 ->> HiddenEye")
    print("2 ->> PhishX")
    print("3 ->> Phisher-man")
    print("4 ->> Blackeye")
    print("5 ->> Zphisher")
    print("6 ->> AIOPhish")
    print("7 ->> Nexphisher")
    print("8 ->> Evilginx2")
    print("9 ->> Predator-Phish")
    print("10 ->> Gophish")
    print("11 ->> SniperPhish")
    print("12 ->> LordPhish")
    print("13 ->> Shellphish")
    print("14 ->> Black Phish")
    print("15 ->> Modlishka")
    print("16 ->> PhishMailer")
    print("17 ->> Whatsapp-phishing")
    print("18 ->> AdvPhishing")
    print("19 ->> YPhish")
    print("20 ->> Dark Phish")
    print("21 ->> Masphish (Ocultar url de tu Phishing )")
    phs = input(">>> ")
    if phs == "1":
       os.system('cd tools ; git clone https://github.com/Morsmalleo/HiddenEye.git')
    elif phs == "2":
        os.system('cd tools ; git clone https://github.com/kucuksemsiyelicocuk/WeebSec-PhishX.git')
    elif phs == "3":
        os.system('cd tools ; git clone https://github.com/FDX100/Phisher-man.git')
    elif phs == "4":
        os.system('cd tools ; git clone https://github.com/The-Burning/blackeye-im.git')
    elif phs == "5":
        os.system('cd tools ; git clone https://github.com/htr-tech/zphisher.git')
    elif phs == "6":
        os.system('cd tools ; git clone https://github.com/DeepSociety/AIOPhish.git')
    elif phs == "7":
        os.system('cd tools ; git clone https://github.com/htr-tech/nexphisher.git')
    elif phs == "8":
        os.system('cd tools ; git clone https://github.com/kgretzky/evilginx2.git')
    elif phs == "9":
        os.system('cd tools ; git clone https://github.com/tony23x/Predator-Phish.git')
    elif phs == "10":
        os.system('cd tools ; git clone https://github.com/gophish/gophish.git')
    elif phs == "11":
        os.system('cd tools ; git clone https://github.com/GemGeorge/SniperPhish.git')
    elif phs == "12":
        os.system('cd tools ; git clone https://github.com/Black-Hell-Team/LordPhish.git')
    elif phs == "13":
        os.system('cd tools ; git clone https://github.com/suljot/shellphish.git')
    elif phs == "14":
        os.system('cd tools ; git clone https://github.com/iinc0gnit0/BlackPhish.git')
    elif phs == "15":
        os.system('cd tools ; git clone https://github.com/drk1wi/Modlishka.git')
    elif phs == "16":
        os.system('cd tools ; git clone https://github.com/BiZken/PhishMailer.git')
    elif phs == "17":
        os.system('cd tools ; git clone https://github.com/Ignitetch/whatsapp-phishing.git')
    elif phs == "18":
        os.system('cd tools ; git clone  https://github.com/Ignitetch/AdvPhishing.git')
    elif phs == "19":
        os.system('cd tools ; git clone https://github.com/thiagous06/YPhish.git')
    elif phs == "20":
        os.system('cd tools ; git clone https://github.com/Cyber-Anonymous/Dark-Phish.git')
    elif phs == "21":
        os.system('cd tools ; git clone https://github.com/jaykali/maskphish.git')
elif opt_menu == "7":
    os.system('clear')
    print(verde)
    print("1 ->> Evildroid")
    print("2 ->> ApkWash")
    print("3 ->> Rafel-Rat")
    print("4 ->> Backdoor-apk")
    print("5 ->> Androrat")
    print("6 ->> Ahmyth-mod")
    print("7 ->> Ahmyth")
    print("8 ->> Infect")
    android = input(">>> ")
    if android == "1":
       os.system('cd tools ; git clone https://github.com/M4sc3r4n0/Evil-Droid.git')
    elif android == "2":
        os.system('cd tools ; git clone https://github.com/jbreed/apkwash.git')
    elif android == "3":
        os.system('cd tools ; git clone https://github.com/swagkarna/Rafel-Rat,git')
    elif android == "4":
        os.system('cd tools ; git clone https://github.com/dana-at-cp/backdoor-apk.git')
    elif android == "5":
        os.system('cd tools ; git clone https://github.com/DesignativeDave/androrat.git')
    elif android == "6":
        os.system('cd tools ; git clone https://github.com/HiddenPirates/AhMyth-Modified-Version.git')
    elif android == "7":
        os.system('cd tools ; git clone https://github.com/Morsmalleo/AhMyth.git')
    elif android == "8":
        os.system('cd tools ; git clone https://github.com/noob-hackers/infect.git')
elif opt_menu == "8":
    os.system('clear')
    print(azul)
    print("1 ->> Sombyote")
    print("2 ->> Pentbox")
    print("3 ->> Easymacchanger")
    print("4 ->> 4anonimizer")
    print("5 ->> Ghost")
    print("6 ->> Phonesploit")
    print("7 ->> ADB-Toolkit")
    print("8 ->> Cam-Hackers")
    tools = input(">>> ")
    if tools == "1":
        os.system('cd tools ; git clone https://github.com/hasanfirnas/symbiote.git')
    elif tools == "2":
        os.system('cd tools ; git clone https://github.com/H4CK3RT3CH/pentbox-1.8.git')
    elif tools == "3":
        os.system('cd tools ; git clone https://github.com/KALILINUXTRICKSYT/easymacchanger.git')
    elif tools == "4":
        os.system('cd tools ; git clone https://github.com/sysadminmexico/4anonimizer.git')
    elif tools == "5":
        os.system('cd tools ; git clone https://github.com/EntySec/Ghost.git')
    elif tools == "6":
        os.system('cd tools ; git clone https://github.com/mishab-ka/PhoneSploit.git')
    elif tools == "7":
        os.system('cd tools ; git clone https://github.com/ASHWIN990/ADB-Toolkit.git')
    elif tools == "8":
        os.system('cd tools ; git clone https://github.com/AngelSecurityTeam/Cam-Hackers.git')
elif opt_menu == "9":
    exit()
else:
    print(rojo+"Error Opcion No Encontrada")
