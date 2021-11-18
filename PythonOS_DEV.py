
#*! Can only run in Python 3.6 and above

import os
import sys
import time
import socket
import masking
import datetime
import platform
from os import name, system

#*_______________SETUP_______________
def main():
	cmd = ""
	rootRequest = ""
	rootpassword = "root"

	root = False
	running = True
	loggedIn = False

	interval = 0.5 #* For time.sleep()

	history = []

	DEBUG = False

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
		return "1.3.2 DEV"

	def username():
		if DEBUG == True:
			username = "DEBUG"
			return username
		else:
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
			time.sleep(interval)
			sys.stdout.write(st.GRN + "\r██     LOADING" + st.RESET)
			time.sleep(interval)
			sys.stdout.write(st.GRN + "\r███    LOADING" + st.RESET)
			time.sleep(interval)
			sys.stdout.write(st.GRN + "\r████   LOADING" + st.RESET)
			time.sleep(interval)
			sys.stdout.write(st.GRN + "\r█████  LOADING" + st.RESET)
			time.sleep(interval)
			sys.stdout.write(st.GRN + "\r██████ LOADING" + st.RESET)
			time.sleep(interval)
			sys.stdout.write(st.GRN + "\r███████LOADING" + st.RESET)
			time.sleep(interval)

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
			f"|             {st.GRN}|  _ \\ _   _| |_| |__   ___  _ __   XXXXX XXXX     {st.RESET}               |\n"
			f"|             {st.GRN}| |_) | | | | __| '_ \\ / _ \\| '_ \\  X   X X___    {st.RESET}                |\n"
			f"|             {st.GRN}|  __/| |_| | |_| | | | (_) | | | | X   X    X  {st.RESET}                  |\n"
			f"|             {st.GRN}|_|    \\__, |\\__|_| |_|\\___/|_| |_| XXXXX XXXX    {st.RESET}                |\n"
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
	if DEBUG == True:
		nameOfUser = "Debugger"
		password = "Debugging"
		passwordc = "Debugging"
		loggedIn = True
	else:
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
			f"{st.BLUE}┌──({st.BLUE + username() + st.GRN}@{st.YLW}PythonOS{st.BLUE})-[{st.RESET}~{st.BLUE}]{st.RESET}\n"
			f"{st.BLUE}└─{st.RED + symbol() + st.RESET if root else st.GRN + symbol() + st.RESET} "
		)
		cmd = cmd.lower()

		history.append(cmd)

		#* COMMANDS

		#* Practical commands
		if cmd == "help" or cmd == "list cmd": #! List all commands
			print(
				st.GRN +
				"Commands\n"
				"|\n"
				"\--{System}\n"
				"|    |\n"
				"|    \--{Networking}\n"
				"|    |    \--[ip]          > Shows the IPv4 adress of the machine\n"
				"|    |    \--[ping]        > Pings a website or local adress\n"
				"|    \--{Terminal}\n"
				"|    |    \--[cls/clear]   > Clears the terminal\n"
				"|    |    \--[hist]        > Shows the command history\n"
				"|    |    \--[hist -clear] > Clears the command history\n"
				"|    |    \--[echo]        > Prints to the terminal what is entered after the \"echo\" command\n"
				"|    |\n"
				"|    \--[sysinfo]          > Displays info about the system\n"
				"|    \--[pcname]           > Shows the name of the machine the OS is running on\n"
				"|    \--[shutdown]         > Shuts down the OS (PythonOS)\n"
				"\--{User Account}\n"
				"     \--[chg name]    > Changes the name for the current session\n"
				"     \--[chg passwd]  > Changes the password for the current session\n"
				"     \--[su # / su]   > \"su #\" changes to the superuser, \"su\" changes back\n"
				"     \--[whoami]      > Shows which user is currently active\n"
				+ st.RESET
			)

		#* SYSTEM COMMANDS

		elif cmd == "ip" or cmd == "ip address": #! Get the local IPv4 address
			print(st.CYAN + IPV4 + st.RESET)

		elif cmd == "pcname": #! Shows the name of the PC
			print(st.GRN + HOST + st.RESET)

		elif cmd == "hist":
			print("\n".join(history))

		elif cmd == "hist -clear":
			history.clear()

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
