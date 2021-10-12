#!/usr/bin/env python3

#! Can only run in Python 3.6 and above

import re
import os
import sys
import time
import socket
import masking
import datetime
import platform
import webbrowser
from os import name, system

#*_______________SETUP_______________
def main():
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

	def pythonVersion():
		if sys.version_info[0] == 3 and sys.version_info[1] >= 6:
			return True
		else:
			return False

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

	def sysver():
		return "1.3.1 DEV"

	def username():
		space = nameOfUser.rfind(" ")
		username = nameOfUser[0:3] + nameOfUser[space + 1:space + 4]
		username = username.lower()

		return username

	def SYSINFO():
		print(f"Full name:\t{nameOfUser}")
		print(f"User:\t\t{username()}")
		print(f"OS:\t\tPythonOS")
		print(f"Release:\tDEVELOPER")
		print(f"Version:\t{sysver()}")
		print(f"IPv4:\t\t{IPV4}")

	def loading():
		for i in range(1):
			sys.stdout.write(st.GRN + "\r█      LOADING" + st.RESET)
			time.sleep(0.5)
			sys.stdout.write(st.GRN + "\r██     LOADING" + st.RESET)
			time.sleep(0.5)
			sys.stdout.write(st.GRN + "\r███    LOADING" + st.RESET)
			time.sleep(0.5)
			sys.stdout.write(st.GRN + "\r████   LOADING" + st.RESET)
			time.sleep(0.5)
			sys.stdout.write(st.GRN + "\r█████  LOADING" + st.RESET)
			time.sleep(0.5)
			sys.stdout.write(st.GRN + "\r██████ LOADING" + st.RESET)
			time.sleep(0.5)
			sys.stdout.write(st.GRN + "\r███████LOADING" + st.RESET)
			time.sleep(0.5)

	def startUp():
		print(
			".===============================================================================.\n"
			f"|                                                                               |\n"
			f"|                                {st.CYAN}.::::::::::.{st.RESET}                                   |\n"
			f"|                              {st.CYAN}.::``::::::::::.{st.RESET}                                 |\n"
			f"|                              {st.CYAN}:::..:::::::::::{st.RESET}                                 |\n"
			f"|                              {st.CYAN}````````::::::::{st.RESET}                                 |\n"
			f"|                      {st.CYAN}.:::::::::::::::::::::::{st.YLW} iiiiiii,{st.RESET}                        |\n"
			f"|                   {st.CYAN}.::::::::::::::::::::::::::{st.YLW} iiiiiiiii.{st.RESET}                      |\n"
			f"|                   {st.CYAN}:::::::::::::::::::::::::::{st.YLW} iiiiiiiiii{st.RESET}                      |\n"
			f"|                   {st.CYAN}:::::::::::::::::::::::::::{st.YLW} iiiiiiiiii{st.RESET}                      |\n"
			f"|                   {st.CYAN}::::::::::{st.YLW} ,,,,,,,,,,,,,,,,,iiiiiiiiii{st.RESET}                      |\n"
			f"|                   {st.CYAN}::::::::::{st.YLW} iiiiiiiiiiiiiiiiiiiiiiiiiii{st.RESET}                      |\n"
			f"|                   {st.CYAN}`:::::::::{st.YLW} iiiiiiiiiiiiiiiiiiiiiiiiii`{st.RESET}                      |\n"
			f"|                      {st.CYAN}`::::::{st.YLW} iiiiiiiiiiiiiiiiiiiiiii`{st.RESET}                         |\n"
			f"|                              {st.YLW}iiiiiiii,,,,,,,,{st.RESET}                                 |\n"
			f"|                              {st.YLW}iiiiiiiiiii''iii{st.RESET}                                 |\n"
			f"|                              {st.YLW}`iiiiiiiiii..ii`{st.RESET}                                 |\n"
			f"|                                {st.YLW}`iiiiiiiiii`{st.RESET}                                   |\n"
			f"|                                                                               |\n"
			f"|             {st.GRN} ____        _   _                            {st.RESET}                    |\n"
			f"|             {st.GRN}|  _ \ _   _| |_| |__   ___  _ __   XXXXX XXXX     {st.RESET}               |\n"
			f"|             {st.GRN}| |_) | | | | __| '_ \ / _ \| '_ \  X   X X___    {st.RESET}                |\n"
			f"|             {st.GRN}|  __/| |_| | |_| | | | (_) | | | | X   X    X  {st.RESET}                  |\n"
			f"|             {st.GRN}|_|    \__, |\__|_| |_|\___/|_| |_| XXXXX XXXX    {st.RESET}                |\n"
			f"|                    {st.GRN}|___/{st.RESET}                                                      |\n"
			f"|                                                                               |\n"
			f"'==============================================================================='\n"
		)
	CLS()

	#!_______________The_Program_Itself_______________

	pythonVersion()

	if pythonVersion() == False:
		print(st.RED + "PythonOS requires Python 3.6 or above to run!\nUpdate your Python version to run PythonOS" + st.RESET)
		time.sleep(10)
		CLS()
		sys.exit()

	startUp()
	loading()

	CLS()

	nameOfUser = input("Enter your full name: ")
	nameOfUser = nameOfUser.title()

	CLS()
	print(st.YLW + "Password must contain atleast 8 characters!" + st.RESET)
	sys.stdout.write("\r" + st.YLW + 37 * " " + "├─ Minimum lenght\r" + st.RESET)
	password = masking.getpass(prompt = f"Enter a password for {st.GRN + username() + st.RESET}: ", mask = "*")

	CLS()
	print(st.YLW + f"Characters in last password: {len(password)}!" + st.RESET)
	sys.stdout.write("\r" + st.YLW + 29 * " " + len(password) * " " + "├── Lenght of password" + "\r" + st.RESET)
	passwordC = masking.getpass(prompt = f"Confirm password for {st.GRN + username() + st.RESET}: ", mask = "*")

	CLS()

	if password == passwordC and len(password) >= 8 and len(passwordC) >= 8:
		print(st.GRN + "Account created, logging in" + st.RESET)
		loggedIn = True
		loading()
		time.sleep(1)

	elif len(password) < 8 or len(passwordC) < 8:
		print(st.RED + "Password must contain atleast 8 characters!" + st.RESET)
		time.sleep(2)

	else:
		print(st.RED + "Passwords don't match!")
		time.sleep(2)

	CLS()

	while running and loggedIn:
		cmd = input(
			f"{st.BLUE + username() + st.RESET + st.GRN}@{st.RESET + st.YLW}PythonOS{st.RESET}"
			f":{st.BLUE}~{st.RESET}{st.RED + symbol() + st.RESET if root else st.GRN + symbol() + st.RESET} "
		)
		cmd = cmd.lower()

		#* COMMANDS

		#* Practical commands
		if cmd == "help" or cmd == "list cmd": #! List all commands
			print(
				st.GRN +
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
				"\t11. chg name = change name\n"
				"\t12. sysinfo = get information about system\n"
				f"\t{st.RED}13. url \"website\" = opens that url in system default browser UNSTABLE\n"
				+ st.RESET
			)

		#* SYSTEM COMMANDS

		elif cmd == "ip" or cmd == "ip address": #! Get the local IPv4 address
			print(st.CYAN + IPV4 + st.RESET)

		elif cmd == "pcname": #! Shows the name of the PC
			print(st.GRN + HOST + st.RESET)

		elif cmd == "sysinfo": #! Shows system information
			SYSINFO()

		elif cmd == "whoami": #! Shows if you are root or not
			if root:
				print(f"{st.RED + username() + st.RESET} as root")
			else:
				print(f"{st.YLW + nameOfUser + st.RESET} as user {st.CYAN + username() + st.RESET}")

		elif cmd.startswith("ping"): #! Pings a website or local address
			pingCMD = f"ping {cmd[5:]}"
			os.system(pingCMD)

		elif cmd.startswith("url"): #! Open URL in webbrowser
			s = cmd.index(" ")
			s + 1
			url = cmd[s:]
			webbrowser.open(url)

		elif cmd.startswith("echo"): #! Prints a string to terminal
			print(cmd[5:])

		elif cmd == "clear" or cmd == "cls": #! Clear screen
			CLS()

		#* SWITCH USER

		elif cmd == "su #": #! Switch user to root
			if not root: 
				rootRequest = masking.getpass(prompt = "Enter root password: ", mask = "*")
				if rootRequest == rootpassword:
					root = True
					CLS()
				else:
					print("Password is incorrect, try agian!")
					time.sleep(1)
					CLS()
			else:
				root = False

		elif cmd == "su": #! Switch user to local
			if root:
				root = False
				CLS()
			else:
				rootRequest = masking.getpass(prompt = "Enter root password: ", mask = "*")
				if rootRequest == rootpassword:
					root = True
					CLS()

		#* CHANGE NAME / USERNAME / PASSWORD

		elif cmd == "chg name": #! Change name
			nameOfUser = input("Enter name: ")

			pwd = masking.getpass(prompt = "Enter password: ", mask = "*")
			if pwd == password:
				nameOfUser = nameOfUser.title()
				print(f"Name changed to {nameOfUser}")
			else:
				print(st.RED + "Password is incorrect!" + st.RESET)

		elif cmd == "chg passwd": #! Change password
			if root:
				newrootpassword = masking.getpass(prompt = "Enter new password for this session: ", mask = "*")
				newrootpasswordC = masking.getpass(prompt = "Confirm new password for this session: ", mask = "*")
				if newrootpassword == newrootpasswordC:
					rootpassword = newrootpassword
			else:
				password = masking.getpass(prompt = "Enter new password for this session: ", mask = "*")
				passwordC = masking.getpass(prompt = "Confirm new password for this session: ", mask = "*")
				if password == passwordC:
					password = password
					print(f"Password changed to {password}")
				else:
					print(st.RED + "Passwords don't match!" + st.RESET)

		#* SHUTDOWN

		elif cmd == "shutdown" or cmd == "exit": #! Shutdown the program
			print(st.RED + "Thank you for using PythonOS" + st.RESET)
			time.sleep(2)
			exit()

		else:
			print(st.RED + "Unknown command, Type 'help' or 'list cmd' for a list of available commands" + st.RESET)
if __name__ == "__main__":
	main()

#! ©Daniel Kristensen 2021
