#!/usr/bin/env python3

import re
import os
import sys
import time
#import mask
import socket
import platform
from os import name, system


try:
	import stdiomask
except ImportError:
	if name == "nt":
		os.system("pip install stdiomask")
	else:
		os.system("sudo apt install python3-pip")
		os.system("pip3 install stdiomask")


#*_______________SETUP_______________

cmd = ""
rootRequest = ""
rootpassword = "root"

root = False
running = True
loggedIn = False

HOST = socket.gethostname()
IPV4 = socket.gethostbyname(HOST)

def symbol():
	if root:
		return "#"
	else:
		return "$"

class st():
	ULINE = '\033[4m'

	#* Colors

	MGN		=		'\033[35m'
	YLW		=		'\033[33m'
	BLK		=		'\033[30m'
	WHT		=		'\033[37m'
	GRN		=		'\033[32m'
	BLUE	=		'\033[34m'
	CYAN	=		'\033[36m'
	RED		=		'\033[31m'
	RESET	=		'\033[0m'

#! Checks if code is running on a Windows or a Linux machine and clears terminal accordingly
def CLS():
	if name == "nt":
		_ = system("cls")
	else:
		_ = system("clear")

def SYSINFO():
	print(f"Full name:\t{nameOfUser}")
	print(f"User:\t\t{username}")
	print(f"OS:\t\t{platform.system()}")
	print(f"Release:\t{platform.release()}")
	print(f"Version:\t{platform.version()}")
	print(f"IPv4:\t\t{IPV4}")

def username():
	space = nameOfUser.rfind(" ")
	username = nameOfUser[0:3] + nameOfUser[space + 1:space + 4]
	username = username.lower()

	return username

CLS()

#*_______________The_Program_Itself_______________

print(st.GRN +
	"This program is created and maintained by Daniel Kristensen\n"
	"For source code access send e-mail request to: dankri0274@gmail.com"
+ st.RESET)

nameOfUser = input("Enter your full name: ")
nameOfUser = nameOfUser.title()

CLS()
print(st.RED + "Password must contain atleast 8 characters!" + st.RESET)
password = stdiomask.getpass(prompt = f"Enter a password for {username()}: ", mask = "*")
if password == "mordi":
	print(st.CYAN + f"Hmm, {password}?" + st.RESET)
	time.sleep(2)
	exit()

CLS()
print(st.YLW + f"Characters in last password: {len(password)}!" + st.RESET)
passwordC = stdiomask.getpass(prompt = f"Confirm password for {username()}: ", mask = "*")

CLS()

if password == passwordC and len(password) >= 8 and len(passwordC) >= 8:
	print(st.GRN + "Account created, logging in" + st.RESET)
	loggedIn = True
	time.sleep(1)
elif len(password) < 8 or len(passwordC) < 8:
	print(st.RED + "Password must contain atleast 8 characters!" + st.RESET)
	time.sleep(2)
else:
	print(st.RED + "Passwords don't match!")
	time.sleep(2)

CLS()

while running and loggedIn:
	cmdR = input(f"{st.GRN + username()}@{HOST + st.RESET}:{st.BLUE}~{st.RESET}{st.RED + symbol() + st.RESET if root else st.GRN + symbol() + st.RESET} ")
	cmdR = cmdR.lower()
	cmd = re.sub("[^a-z0-9]", "", cmdR)

	#* COMMANDS

	#* Practical commands
	if cmd == "help" or cmd == "list cmd":
		print(
			st.CYAN +
			"Commands:\n"
			"\t1. su # = switch user to root user / su = switch back\n"
			"\t2. ip = Get the local IPv4 address\n"
			"\t3. clear / cls = clear screen\n"
			"\t4. pcname = shows the name of the PC\n"
			"\t5. whoami = shows if you are root user or local user\n"
			"\t6. ping = enter address to ping after ping\n\tex ping www.google.com\n"
			"\t7. shutdown / exit = quits the program\n"
			"\t8. echo = enter a string after echo to print it to terminal\n"
			"\t9. list cmd / help = show this help message\n"
			"\t10. chg passwd = change password\n"
			"\t11. chg name = change name"
			+ st.RESET
		)
	elif cmd == "ip":
		print(st.CYAN + IPV4 + st.RESET)
	elif cmd == "pcname":
		print(st.GRN + HOST + st.RESET)
	elif cmd == "clear" or cmd == "cls":
		CLS()
	elif cmd == "su #":
		if not root: 
			rootRequest = stdiomask.getpass(prompt = "Enter root password: ", mask = "*")
			if rootRequest == rootpassword:
				root = True
				CLS()
			else:
				print("Password is incorrect, try agian!")
				time.sleep(1)
				CLS()
	elif cmd == "sysinfo":
		SYSINFO()
	elif cmd == "su":
		if root:
			root = False
		else:
			print("Enter 'su #' to become root user")
	elif cmd == "whoami":
		if root:
			print(f"{st.RED + username() + st.RESET} as root")
		else:
			print(f"{st.YLW + nameOfUser + st.RESET} as user {st.CYAN + username() + st.RESET}")
	elif cmd.startswith("ping"):
		pingCMD = f"ping {cmd[5:]}"
		os.system(pingCMD)
	elif cmd.startswith("echo"):
		print(cmd[5:])
	elif cmd == "chg name":
		nameOfUser = input("Enter name: ")
	elif cmd == "shutdown" or cmd == "exit":
		print(st.RED + "Thank you for using PythonOS" + st.RESET)
		if "Karl Amund" in nameOfUser:
			time.sleep(15)
			os.system("shutdown /r /c \"PC-en støtte på et problem og trenger en omstart.\"")
		exit()

	elif cmd == "chg passwd":
		if root:
			rootpassword = stdiomask.getpass(prompt = "Enter new password for this session: ", mask = "*")
			rootpasswordC = stdiomask.getpass(prompt = "Confirm new password for this session: ", mask = "*")
		else:
			password = stdiomask.getpass(prompt = "Enter new password for this session: ", mask = "*")
			passwordC = stdiomask.getpass(prompt = "Confirm new password for this session: ", mask = "*")
	else:
		print(st.RED + "Unknown command, Type 'help' or 'list cmd' for a list of available commands" + st.RESET)

#! ©Daniel Kristensen 2021