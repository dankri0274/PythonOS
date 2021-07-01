import sys
import time
import socket
import stdiomask
from os import name, system

#*___________________SETUP___________________

cmd = ""

root = False
host = socket.gethostname()
ip = socket.gethostbyname(host)
running = True

def booting():
	for _ in range(3):
		sys.stdout.write("\rStarting up   ")
		time.sleep(1)
		sys.stdout.write("\rStarting up.  ")
		time.sleep(1)
		sys.stdout.write("\rStarting up.. ")
		time.sleep(1)
		sys.stdout.write("\rStarting up...")
		time.sleep(1)


def symbol():
	if root:
		return "#"
	else:
		return "$"

class style():
	underline = '\033[4m' #!Styling
	
	#*Colors
	magenta = '\033[35m'
	yellow = '\033[33m'
	black = '\033[30m'
	white = '\033[37m'
	green = '\033[32m'
	blue = '\033[34m'
	cyan = '\033[36m'
	red = '\033[31m'
	reset = '\033[0m'

def cls():
	if name == "nt":
		_ = system("cls")
	else:
		_ = system("clear")

cls()

#*_________________________The program itself_________________________

booting()

cls()

user = input("Enter name: ")
user = user.title()

cls()

username = input("Enter username: ")
username = username.lower()
"""
cls()

password = stdiomask.getpass(prompt = "Enter a password: ")

cls()

passConf = stdiomask.getpass(prompt = "Confirm password: ")

if password == passConf:
	print(style.green + "Account created" + style.reset)
elif len(password) < 8 or len(passConf) < 8:
	print(style.red + "Password must contain at least 8 characters" + style.reset)
else:
	print(style.red + "Passwords don't match" + style.reset)
"""
cls()

while running:
	cmd = input(style.green + f"{username}@{host}" + style.reset + f":~{symbol()} ")
	cmd = cmd.lower()

	if cmd == "ip":
		print(ip)
	elif cmd == "pcname":
		print(f"This PC has the name: {host}")
	elif cmd == "clear":
		cls()
	elif cmd == "su #":
		root = True
		cls()
	elif cmd ==  "su":
		root = False
		cls()
	elif cmd == "chg name" and not root:
		print(style.red + "You must be root user to change owner name!" + style.reset)
	elif cmd == "chg name" and root:
		user = input("Enter new name: ")

	elif cmd == "chg username" and not root:
		print(style.red + "You must be root user to change username!" + style.reset)
	elif cmd == "chg username" and root:
		username = input("Enter new username: ")

	elif cmd == "whoami":
		if root:
			print(f"{username} as root")
		else:
			print(f"{user} as user {username}")
	elif cmd == "shutdown -now":
		print(style.yellow + "Shutting down..." + style.reset)
		time.sleep(2)
		exit()
	else:
		print(style.red + "Unknown command!" + style.reset)
