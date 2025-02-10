import requests
import os
from faker import Faker
from colorama import Fore, init
init(autoreset=True)

g = Fore.GREEN
r = Fore.RED
w = Fore.WHITE
y = Fore.YELLOW
reset = Fore.RESET
fake = Faker("ID_id")


os.system('cls' if os.name == "nt" else 'clear')
print(f"""{g}
    _   _   _   _   _   _   _  
   / \ / \ / \ / \ / \ / \ / \ 
  ( S | p | o | t | i | f | y )  {w}Spotify Account Creator{g}
   \_/ \_/ \_/ \_/ \_/ \_/ \_/
{reset}""")

CONFIG = {
    "proxy"    : "xxxxxx", # format proxy -> http://username:password@host:port
    "password" : "xxxxxx", # at least 8 characters, example: masuk12345
    "domain"   : "xxxxxx" # your domain without @ , example: gmail.com
}

while True:
    try:
        check_proxies = requests.get("http://ip-api.com/json", proxies={"http":CONFIG['proxy'],"https":CONFIG['proxy']}, timeout=5)
        if "407" in check_proxies.text:
            exit(f"\n{r}Proxy Authentication Required. Your username or password is incorrect or your plan expired.")
        else:
            print(f"\nProxy Connected : {check_proxies.json()['country']} {check_proxies.json()['query']}")
            break
    except Exception as e:
        continue

amount = int(input("Amount create   : "))
print(f"{y}\nUsing a proxy might slow things down and even cause failures. This is a beta version, so there might still be some bugs. if u run into any issues, don’t forget to report them to {w}t.me/agallagherz !\n")
success = 0
while success < amount:
    data = {
        "name": fake.first_name().lower() + fake.last_name().lower(),
        "password": CONFIG['password'],
        "email": fake.first_name().lower() + fake.last_name().lower() + "@" + CONFIG['domain'],
        "proxy": CONFIG['proxy']
    }
    signup = requests.post("https://apisangkara.my.id/spotify/create", data=data, headers={"X-Apikey":"chsangkara"}).json()
    try:
        if signup['success']:
            print(f"{g}Success : {data['email']}")
            success += 1
            with open("spotify_proxies.txt","a") as f:
                f.write(f"{data['email']}|{data['password']}\n")
    except Exception as e:
        continue
