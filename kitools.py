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
        os.system('cd tools ; git clone https://github.com/Lucksi/Mr.Holmes.git ; cd Mr.Holmes ; sudo python3 MrHolmes.py')
    elif opt_1 == "2":
        os.system('cd tools ; git clone https://github.com/sherlock-project/sherlock.git ; cd sherlock ; python3 -m pip install -r requirements.txt ')
    elif opt_1 == "3":
        os.system('sudo pip3 install maigret ; maigret -h ')
    elif opt_1 == "4":
        os.system('cd tools ; curl -sSL https://raw.githubusercontent.com/sundowndev/phoneinfoga/master/support/scripts/install | bash ')
    elif opt_1 == "5":
        os.system('cd tools ; git clone https://github.com/R3D-GHOST/The-Ghost-Seeker.git ; cd The-Ghost-Seeker ; sudo bash install.sh')
    elif opt_1 == "6":
        os.system('cd tools ; git clone https://github.com/Datalux/Osintgram.git ; cd Osintgram ; pip install -r requirements.txt')
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
        os.system('cd tools ; git clone https://github.com/sqlmapproject/sqlmap.git : cd sqlmap ; python3 sqlmap.py -h ')
    elif opt_2 == "2":
        os.system('sudo apt install nmap ; nmap -h ')
    elif opt_2 == "3":
        os.system('sudo apt install burpsuite')
    elif opt_2 == "4":
        os.system('sudo apt install whatweb ; whatweb -h ')
    elif opt_2 == "5":
        os.system('cd tools ; git clone https://github.com/R3D-GHOST/Scan-Web.git ; cd Scan-Web ; python3 scanner.py ')
    elif opt_2 == "6":
        os.system('cd tools ; git clone https://github.com/Tuhinshubhra/RED_HAWK.git ; cd RED_HAWK ; php rhawk.php')
    elif opt_2 == "7":
        os.system('sudo apt-get install legion')
    elif opt_2 == "8":
        os.system('cd tools ; git clone https://github.com/Anteste/WebMap.git ; cd WebMap ; sudo bash install.sh')
    elif opt_2 == "9":
        os.system('cd tools ; git clone https://github.com/rpranshu/EternalView.git ; cd EternalView ; chmod +x EternalView.sh ; ./EternalView.sh')
    elif opt_2 == "10":
        os.system('cd tools ; git clone https://github.com/1N3/BlackWidow.git ; cd BlackWidow ; sudo bash install.sh')
    elif opt_2 == "11":
        os.system('cd tools ; git clone https://github.com/six2dez/reconftw.git ; cd reconftw/ ; sudo bash install.sh')
    elif opt_2 == "12":
        os.system('cd tools ; git clone https://github.com/BullsEye0/dorks-eye.git ; cd dorks-eye ; pip3 install -r requirements.txt')
    elif opt_2 == "13":
        os.system('cd tools ; git clone https://github.com/Bitwise-01/SQL-scanner.git ; cd SQL-scanner ; pip install -r requirements.txt')
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
        os.system('sudo apt install aircrack-ng ; aircrack-ng --help ')
    elif opt_3 == "2":
        os.system('sudo apt install airgeddon ; airgeddon')
    elif opt_3 == "3":
        os.system('sudo apt install wifite ; wifite --help ')
    elif opt_3 == "4":
        os.system('cd tools ; git clone https://github.com/P0cL4bs/WiFi-Pumpkin.git ; cd WiFi-Pumpkin ; sudo bash installer.sh --install')
    elif opt_3 == "5":
        os.system('cd tools ; git clone https://github.com/mkdirlove/WI-TOOLKIT.git ; cd WI-TOOLKIT : sudo bash install.sh ')
    elif opt_3 == "6":
        os.system('cd tools ; git clone https://github.com/mkdirlove/AIR-KIT.git ; cd AIR-KIT ; sudo bash air-kit.sh -h')
    elif opt_3 == "7":
        os.system('cd tools ; git clone https://github.com/bitbrute/evillimiter.git ; cd evillimiter : sudo python3 setup.py install ')
elif opt_menu == "4":
    os.system('clear')
    print(rosado)
    print("1 ->> Bettercap")
    print("2 ->> SMS Anon")
    print("3 ->> SMS GHOST")
    print("4 ->> God-Killer")
    opt_4 = input(">>> ")
    if opt_4 == "1":
        os.system('sudo apt install bettercap ; bettercap --help')
    elif opt_4 == "2":
        os.system('cd tools ; git clone https://github.com/HACK3RY2J/Anon-SMS.git ; cd Anon-SMS ; bash Run.sh')
    elif opt_4 == "3":
        os.system('cd tools ; git clone https://github.com/R3D-GHOST/SMS-GHOST.git ; cd SMS-GHOST ; bash install.sh ; python3 sms-ghost')
    elif opt_4 == "4":
        os.system('cd tools ; git clone  https://github.com/FDX100/GOD-KILLER.git ; cd GOD-KILLER ; python install.py ; GOD-KILLER')
elif opt_menu == "5":
    os.system('clear')
    print(cierre)
    print("1 ->> DDoS RIPPER ")
    print("2 ->> DDoS-Network")
    print("3 ->> SlowHttptest")
    opt_5 = input(">>> ")
    if opt_5 == "1": 
        os.system('cd tools ; git clone https://github.com/palahsu/DDoS-Ripper.git ; cd DDoS-Ripper ; python3 DRipper.py ')
    elif opt_5 == "2":
        os.system('cd tools ; git clone https://github.com/R3D-GHOST/DDoS-Network.git ; cd DDoS-Network ; sudo bash install.sh ; bash DDoS.sh')
    elif opt_5 == "3":
        os.system('sudo apt install slowhttptest ; slowhttptest --help') 
elif opt_menu == "6":
    os.system('clear')
    print(blanco)
    print("1 ->> Phisher-man")
    print("2 ->> Blackeye")
    print("3 ->> Zphisher")
    print("4 ->> AIOPhish")
    print("5 ->> Whatsapp-phishing")
    print("6 ->> Masphish (Ocultar url de tu Phishing )")
    phs = input(">>> ")
    if phs == "1":
        os.system('cd tools ; git clone https://github.com/FDX100/Phisher-man.git ; cd Phisher-man ; python3 app.py  ')
    elif phs == "2":
        os.system('cd tools ; git clone https://github.com/The-Burning/blackeye-im.git ; cd blackeye-im ; chmod +x ./setup.sh ; ./setup.sh')
    elif phs == "3":
        os.system('cd tools ; git clone https://github.com/htr-tech/zphisher.git ; cd zphisher ; bash zphisher.sh')
    elif phs == "4":
        os.system('cd tools ; git clone https://github.com/DeepSociety/AIOPhish.git ; cd AIOPhish ; bash install.sh')
    elif phs == "5":
        os.system('cd tools ; git clone https://github.com/Ignitetch/whatsapp-phishing.git ; cd whatsapp-phishing ; chmod 777 Whatsapp.sh ; ./Whatsapp.sh')
    elif phs == "6":
        os.system('cd tools ; git clone https://github.com/jaykali/maskphish.git ; cd maskphish ; bash maskphish.sh ')
elif opt_menu == "7":
    os.system('clear')
    print(verde)
    print("1 ->> Evildroid")
    print("2 ->> ApkWash")
    print("3 ->> Ahmyth")
    print("4 ->> Infect")
    android = input(">>> ")
    if android == "1":
       os.system('cd tools ; git clone https://github.com/M4sc3r4n0/Evil-Droid.git ;  cd Evil-Droid ; chmod +x evil-droid ; ./evil-droid')
    elif android == "2":
        os.system('cd tools ; git clone https://github.com/jbreed/apkwash.git ; cd apkwash ; chmod +x apkwash ; bash apkwash')
    elif android == "3":
        os.system('cd tools ; git clone https://github.com/Morsmalleo/AhMyth.git ; cd AhMyth/AhMyth-Server ; sudo bash autoinstall')
    elif android == "4":
        os.system('cd tools ; git clone https://github.com/noob-hackers/infect.git ; cd infect ; bash infect.sh')
elif opt_menu == "8":
    os.system('clear')
    print(azul)
    print("1 ->> Sombyote")
    print("2 ->> Easymacchanger")
    print("3 ->> Ghost")
    print("4 ->> Phonesploit")
    print("5 ->> ADB-Toolkit")
    print("6 ->> Cam-Hackers")
    print("7 ->> Email-Bomber")
    tools = input(">>> ")
    if tools == "1":
        os.system('cd tools ; git clone https://github.com/hasanfirnas/symbiote.git ; cd symbiote ; python3 symbiote.py')
    elif tools == "2":
        os.system('cd tools ; git clone https://github.com/KALILINUXTRICKSYT/easymacchanger.git ; cd easymacchanger ; bash installer.sh')
    elif tools == "3":
        os.system('cd tools ; git clone https://github.com/EntySec/Ghost.git ; cd Ghost ; python3 setup.py')
    elif tools == "":
        os.system('cd tools ; git clone https://github.com/mishab-ka/PhoneSploit.git ; cd PhoneSploit ; pip install colorama ; python2 main_linux.py')
    elif tools == "7":
        os.system('cd tools ; git clone https://github.com/ASHWIN990/ADB-Toolkit.git ; cd ADB-Toolkit ; sudo chmod +x install.sh ; sudo ./install.sh -i ')
    elif tools == "8":
        os.system('cd tools ; git clone https://github.com/AngelSecurityTeam/Cam-Hackers.git ; cd Cam-Hackers ; pip install -r requirements.txt ; python3 cam-hackers.py')
    elif tools == "9":
        os.system('cd tools ; git clone https://github.com/RIP-Network/Email-Bomber.git ; cd Email-Bomber ; chmod +x email.py ; chmod +x install.sh ; ./install.sh ; python email.py ')
elif opt_menu == "9":
    exit()
else:
    print(rojo+"Error Opcion No Encontrada")
