# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.
import json
import requests
import socket
import platform
import os
import time
import string
import random
from colorama import Fore, init
from pystyle import Colorate, Colors, Center

# Initialisation de Colorama
init(autoreset=True)

class CyberTool:
    def __init__(self):
        self.banner_art = r'''
          ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░  
         ░▒▓█▓▒░░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
        ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░   
        ░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░  
        ░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
        ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
         ░▒▓██████▓▒░   ░▒▓█▓▒░   ░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                                                   
                               By: C Y B Σ R M E N A C E                                  
                           _________________________________
'''
        self.home_art = r'''
                        [01] > Lookup Website     [02] > Webhook Spammer
                        [03] > Ping Test          [04] > System Info
                        [05] > IP Information     [06] > Phone Number Info
                        [07] > Exit
'''

    def banner(self):
        print(Colorate.Vertical(Colors.red_to_black, self.banner_art))

    def homemenu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.banner()
            print(Colorate.Vertical(Colors.red_to_black, self.home_art))
            inp = input(Fore.RED + "[cybertool@MENU] > ").strip()

            if inp == "1":
                self.lookup_website()
            elif inp == "2":
                self.webhook_spammer()
            elif inp == "3":
                self.ping_test()
            elif inp == "4":
                self.system_info()
            elif inp == "5":
                self.ip_information()
            elif inp == "6":
                self.phone_info()
            elif inp == "7":
                print(Fore.GREEN + "Merci d'avoir utilisé cet outil. À bientôt !")
                exit()
            else:
                print(Fore.RED + "[-] Option invalide, veuillez réessayer.")
                time.sleep(1)

    def lookup_website(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + "[+] Lookup Website")
        domain = input(Fore.YELLOW + "Entrez un domaine ou une URL (ex: example.com) : ").strip()
        
        # Nouveau code pour l'option 1
        try:
            ip = socket.gethostbyname(domain)
            response = requests.get(f"http://ip-api.com/json/{ip}")
            data = response.json()

            print(Fore.GREEN + f"\n[+] Informations sur {domain} :\n")
            print(Fore.YELLOW + f" - IP : {data['query']}")
            print(Fore.YELLOW + f" - Pays : {data['country']}")
            print(Fore.YELLOW + f" - Région : {data['regionName']}")
            print(Fore.YELLOW + f" - Ville : {data['city']}")
            print(Fore.YELLOW + f" - FAI : {data['isp']}")
            print(Fore.YELLOW + f" - Organisation : {data['org']}")
            print(Fore.YELLOW + f" - Latitude : {data['lat']}")
            print(Fore.YELLOW + f" - Longitude : {data['lon']}")
        except socket.gaierror:
            print(Fore.RED + "[!] Domaine ou URL invalide.")
        except requests.exceptions.RequestException as e:
            print(Fore.RED + "[!] Erreur lors de la connexion à l'API.")
            print(Fore.RED + f"    {str(e)}")
        input(Fore.CYAN + "Appuyez sur Entrée pour revenir au menu principal...")

    def webhook_spammer(self):
        def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))

        def send_message(webhook_url, sent_count):
            username = id_generator(10)
            message = "@everyone **C Y B Σ R M E N A C E ON TOP** !!!"
            avatar = "https://media.discordapp.net/attachments/1352058264447090790/1352764447063802060/hacking.png"

            data = json.dumps({
                "content": message,
                "username": username,
                "avatar_url": avatar,
                "tts": False
            })

            headers = {"content-type": "application/json"}
            response = requests.post(webhook_url, data=data, headers=headers)

            if response.ok:
                sent_count += 1
                print(Fore.GREEN + f"[+] Message envoyé avec succès ! Total : {sent_count}")
            elif response.status_code == 429:
                print(Fore.RED + "[!] Limite de rate atteinte, en pause...")
                time.sleep(5)
            else:
                print(Fore.RED + "[!] Échec de l'envoi du message.")

            return sent_count

        os.system('cls' if os.name == 'nt' else 'clear')
        webhook_url = input(Fore.YELLOW + "Entrez l'URL du webhook Discord : ").strip()

        if not webhook_url.startswith("https://discord.com/api/webhooks/"):
            print(Fore.RED + "[!] URL du webhook invalide.")
            time.sleep(2)
            return

        sent_count = 0
        while True:
            sent_count = send_message(webhook_url, sent_count)

    def ping_test(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + "[+] Ping Test")
        hostname = input(Fore.YELLOW + "Entrez un domaine ou une adresse IP à ping : ").strip()
        response = os.system(f"ping -n 4 {hostname}" if os.name == "nt" else f"ping -c 4 {hostname}")
        if response == 0:
            print(Fore.GREEN + f"[+] Le ping vers {hostname} a réussi !")
        else:
            print(Fore.RED + f"[-] Impossible de ping {hostname}.")
        input(Fore.CYAN + "Appuyez sur Entrée pour revenir au menu principal...")

    def system_info(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + "[+] System Information")
        print(Fore.YELLOW + f"Système : {platform.system()}")
        print(Fore.YELLOW + f"Nom de l'ordinateur : {socket.gethostname()}")
        print(Fore.YELLOW + f"Version : {platform.version()}")
        print(Fore.YELLOW + f"Processeur : {platform.processor()}")
        input(Fore.CYAN + "Appuyez sur Entrée pour revenir au menu principal...")

    def ip_information(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + "[+] IP Information")
        ip_address = input(Fore.YELLOW + "Entrez une adresse IP pour obtenir des informations : ").strip()
        try:
            response = requests.get(f"https://ipinfo.io/{ip_address}/json")
            data = response.json()
            print(Fore.GREEN + f"IP : {data.get('ip', 'N/A')}")
            print(Fore.GREEN + f"Ville : {data.get('city', 'N/A')}")
            print(Fore.GREEN + f"Région : {data.get('region', 'N/A')}")
            print(Fore.GREEN + f"Pays : {data.get('country', 'N/A')}")
        except:
            print(Fore.RED + "[!] Impossible de récupérer les informations sur l'IP.")
        input(Fore.CYAN + "Appuyez sur Entrée pour revenir au menu principal...")

    def phone_info(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + "[+] Phone Number Information")
        phone_number = input(Fore.YELLOW + "Entrez un numéro de téléphone (ex: +33123456789) : ").strip()
        print(Fore.RED + "[!] Cette fonctionnalité n'est pas encore disponible.")
        input(Fore.CYAN + "Appuyez sur Entrée pour revenir au menu principal...")

# Lancement de l'outil
if __name__ == "__main__":
    tool = CyberTool()
    tool.homemenu()
