import requests
import services

# colours
green     = '\033[92m'
cyan      = '\033[95m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'
#ascii art
ascii_art = f'''
{green}{bold}
                         
______  ___     ______ _____                           ______  
___   |/  /________  /____(_)__________________ __________  /_ 
__  /|_/ /_  __ \_  __ \_  /_  ___/_  ___/  __ `/_  ___/_  __ \
_  /  / / / /_/ /  /_/ /  / / /__ _  /   / /_/ /_(__  )_  / / /
/_/  /_/  \____//_.___//_/  \___/ /_/    \__,_/ /____/ /_/ /_/ 


{end}
                                                               
                      
'''
print(ascii_art)
# header
print(f"{green}{bold}\t\t{underline}[MOCRASH 1.1]{end}")
print(f"{green}{bold}\t\t{underline}[HITLÖS OFFICIAL TOOL]{end}")
print()
print(f"{bold}Developed by{end}", end="")
print(f"{green}{bold} >> {end}", end="")
print(f"{cyan}{bold}Sajadtlpr{end}")

print(f"{bold}twitter{end}", end="")
print(f"{green}{bold} >> {end}", end="")
print(f"{cyan}{bold}@Sajadtlpr{end}")
print()

# inputs
print('\x1b[32;1m' + 'enter the number without or with prefixes (+7) (8)\nexample: 9018017010' + '\x1b[0m')
input_number = input('\x1b[32;1m\x1b[1m>> \x1b[0m')
print('\x1b[32;1mIos or android to crash?:\nTime of executions...select time to continue atks?' + '\x1b[0m')
sms = int(input('\x1b[32;1m\x1b[1m>> \x1b[0m'))

print(f"you need a\x1b[36;1m tor \x1b[0my/n? ")
is_tor = input('\x1b[1m\x1b[32m>> \x1b[0m')


def parse_number(number):
	msg = f"[*]check number - {green}{bold}OK{end}"
	if len(number) in (10, 11, 12):
		if number[0] == "8":
			number = number[1:]
			print(msg)
		elif number[:2] == "+7":
			number = number[2:]
			print(msg)
		elif int(len(number)) == 10 and number[0] == 9:
			print(msg)
	else:
		print(f"[*]check number - {red}{bold}failed number!{end}\nThis bomber is intended only for Russia and if the number you entered belongs to another country then alas this bomber is not suitable for you!")
		quit()
	return number
number = parse_number(input_number)

# tor
if str(is_tor) == "y":
        print(f"[*]launch {cyan}{bold}Tor{end}...")
        proxies = {
            'http': 'socks5://139.59.53.105:1080',
            'https': 'socks5://139.59.53.105:1080'
        }
        tor = requests.get('http://icanhazip.com/', proxies=proxies).text
        tor = (tor.replace('\n', ''))
        print(f"[*]launch {cyan}{bold}Tor{end} - {green}{bold}OK{end}")

services.attack(number, sms)
