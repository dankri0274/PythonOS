import os
import sys
import time
import json
import socket
import platform
from os import name, system

try:
	import stdiomask
except ImportError:
	if name == "nt":
		os.system("pip install stdiomask")
	else:
		os.system("pip3 install stdiomask")

#*___________________SETUP___________________

cmd = ""
rootpassword = "admin"

root = False
running = True

host = socket.gethostname()
ip = socket.gethostbyname(host)

def symbol():
	if root:
		return "#"
	else:
		return "$"

#*Style and color for output text
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

#Checks if code is running on a Windows or a Linux OS
def cls():
	if name == "nt":
		_ = system("cls")
	else:
		_ = system("clear")

def systeminfo():
	print(f"Full name:\t{user}")
	print(f"User:\t\t{username}")
	print(f"OS:\t\t{platform.system()}")
	print(f"Release:\t{platform.release()}")
	print(f"Version:\t{platform.version()}")
	print(f"IPv4:\t\t{ip}")

cls()

#*_________________________The program itself_________________________

cls()
user = input("Enter name: ")
user = user.title()
cls()
username = input("Enter username: ")
username = username.lower()
cls()
password = stdiomask.getpass(prompt = "Enter a password: ")
cls()
passConf = stdiomask.getpass(prompt = "Confirm password: ")

#add variables user, username, password to data
data = {
	"Name": user,
	"Username": username,
	"Password": password
}
#add data to terminalusers.json
with open("C:/Users/dankri/documents/programmering/python/OS/terminal/terminalusers.json", "w") as file:
	json.dump(data, file)

if password == passConf:
	print(style.green + "Account created" + style.reset)
elif len(password) < 8 or len(passConf) < 8:
	print(style.red + "Password must contain at least 8 characters" + style.reset)
else:
	print(style.red + "Passwords don't match" + style.reset)

cls()

while running:
	cmd = input(f"{style.green + username}@{host + style.reset}:{style.blue}~{style.reset}{style.red + symbol() + style.reset if root else symbol()} ")
	cmd = cmd.lower()

	#*COMMANDS

	#*Practical commands
	if cmd == "-help":
		print(
			style.cyan +
			"Commands:\n"
			"\t1. su # = switch user to root user\n"
			"\t2. ip = Get the local IPv4 address\n"
			"\t3. clear / cls = clear screen\n"
			"\t4. pcname = shows the name of the PC\n"
			"\t5. whoami = shows if you are root user or local user\n"
			"\t6. ping = enter ping, and a second line will appear where\n\t-you can enter a website or local address to ping\n"
			"\t7. shutdown -now = quits the program"
			+ style.reset
		)
	elif cmd == "ip":
		print(style.blue + ip + style.reset)
	elif cmd == "pcname":
		print(style.green + host + style.reset)
	elif cmd == "clear" or cmd == "cls":
		cls()
	elif cmd == "su #":
		root = True
		cls()
	elif cmd == "su":
		root = False
	elif cmd == "whoami":
		if root:
			print(f"{username} as root")
		else:
			print(f"{style.red + user + style.reset} as user {style.blue + username + style.reset}")
	elif cmd == "ping":
		pingaddress = input("Enter address to ping: ")
		pingcmd = f"ping {pingaddress}"
		os.system(pingcmd)
	elif cmd == "sysinfo":
		systeminfo()
	elif cmd == "shutdown -now":
		cls
		print(style.cyan + "Made by Daniel Kristensen\nWritten in Python" + style.reset)
		time.sleep(2)
		exit()
	

#*__________Commands that change system settings__________
	
	elif cmd == "chg name":
		if root:
			user = input("Enter new name: ")
			user = user.title()
			print(f"Name successfully changed to: {style.blue + user + style.reset}")
			time.sleep(2)
			cls()
		else:
			print(style.red + "You must be root user to change owner name!" + style.reset)

	elif cmd == "chg username":
		if root:
			username = input("Enter new username: ")
			print(f"Username successfully changed to: {style.blue + username + style.reset}")
			time.sleep(2)
			cls()
		else:
			print(style.red + "You must be root user to change username!" + style.reset)
	

	elif cmd == "list su cmd" and root:
		print(
			"Available commands:\n"
			"\t1. chg username = change username of user\n"
			"\t2. chg name = change name of user\n"
			"\t3. chg password\n"
		)

#*__________Root settings__________
	elif cmd == "chg password":
		if root:
			password = stdiomask.getpass(prompt = "Enter new password: ", mask = "*")
			passConf = stdiomask.getpass(prompt = "confirm new password: ", mask = "*")
			if password == passConf:
				print(style.green + f"Password for {username} successfully changed" + style.reset)
				time.sleep(2)
				cls()
			else:
				print(style.red + "Passwords don't match" + style.reset)
		else:
			print(style.red + "You must be root user to change password!")

	#EOS
	else:
		print(style.red + "Unknown command!" + style.reset)
		