
#! Can only run in Python 3.6 and above

#! !!UNSTABLE!!
#! This version imports alot of the main features from other files

import config
import masking
import clearScreen
from nec import *

#*_______________SETUP_______________
def main():
	cmd = ""
	history = []

	def symbol():
		if config.setup.root:
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

	def sysver():
		return "1.3.3 DEV"

	def username():
		if config.setup.DEBUG == True:
			username = "DEBUG"
			return username
		else:
			space = nameOfUser.rfind(" ")
			username = nameOfUser[0:3] + nameOfUser[space + 1:space + 4]
			username = username.lower()

			return username
	
	def histClear(): #* If no arguments are made, deletes entire history
		if cmd[7:] != "":
			ptc = int(cmd[7:])
			history.pop(ptc - 1)
		else:
			history.clear()

	def SYSINFO():
		print(f"Full name:    {nameOfUser}")
		print(f"User:         {username()}")
		print(f"OS:           PythonOS")
		print(f"Release:      DEVELOPER")
		print(f"Version:      {sysver()}")
		print(f"IPv4:         {config.setup.IPV4}")

	def loading():
		for i in range(2):
			sys.stdout.write(st.GRN + "\r|" + st.RESET)
			time.sleep(interval)
			sys.stdout.write(st.GRN + "\r/" + st.RESET)
			time.sleep(interval)
			sys.stdout.write(st.GRN + "\r-" + st.RESET)
			time.sleep(interval)
			sys.stdout.write(st.GRN + "\r\\" + st.RESET)
			time.sleep(interval)

	#!_______________The_Program_Itself_______________

	pythonVersion()

	if pythonVersion() == False:
		print(st.RED + "PythonOS requires Python 3.6 or above to run!\nUpdate your Python version to run PythonOS" + st.RESET)
		time.sleep(10)
		clearScreen.CLS()
		sys.exit()

	#loading.startUp()

	clearScreen.CLS()
	if config.setup.DEBUG == True:
		nameOfUser = "Debugger"
		password = "Debugging"
		passwordc = "Debugging"
		config.setup.loggedIn = True
	else:
		nameOfUser = input("Enter your full name: ")
		nameOfUser = nameOfUser.title()

		clearScreen.CLS()
		print(st.YLW + "Password must contain atleast 8 characters!" + st.RESET)
		sys.stdout.write("\r" + st.YLW + 37 * " " + "├─ Minimum lenght\r" + st.RESET)
		password = masking.getpass(prompt = f"Enter a password for {st.GRN + username() + st.RESET}: ", mask = "*")

		clearScreen.CLS()
		print(st.YLW + f"Characters in last password: {len(password)}!" + st.RESET)
		sys.stdout.write("\r" + st.YLW + 29 * " " + len(password) * " " + "├── Lenght of password" + "\r" + st.RESET)
		passwordC = masking.getpass(prompt = f"Confirm password for {st.GRN + username() + st.RESET}: ", mask = "*")

		clearScreen.CLS()

		if password == passwordC and len(password) >= 8 and len(passwordC) >= 8:
			print(st.GRN + "Account created, logging in" + st.RESET)
			loggedIn = True
			loading.loading()
			time.sleep(1)

		elif len(password) < 8 or len(passwordC) < 8:
			print(st.RED + "Password must contain atleast 8 characters!" + st.RESET)
			time.sleep(2)

		else:
			print(st.RED + "Passwords don't match!")
			time.sleep(2)

		clearScreen.CLS()

	while config.setup.running and config.setup.loggedIn:
		cmd = input(
			f"{st.BLUE}┌──({st.BLUE + username() + st.GRN}@{st.YLW}PythonOS{st.BLUE})-[{st.RESET}~{st.BLUE}]{st.RESET}\n"
			f"{st.BLUE}└─> {st.RED + symbol() + st.RESET if config.setup.root else st.GRN + symbol() + st.RESET} "
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
				"|    |    \--[ip]             > Shows the IPv4 adress of the machine\n"
				"|    |    \--[ping]           > Pings a website or local adress\n"
				"|    \--{Terminal}\n"
				"|    |    \--[cls/clear]      > Clears the terminal\n"
				"|    |    \--[hist]           > Shows the command history\n"
				"|    |    \--[hist -c <n>]    > Clears the command history, if \"hist -c <number>\", deletes an individual element\n"
				"|    |    \--[echo]           > Prints to the terminal what is entered after the \"echo\" command\n"
				"|    |\n"
				"|    \--[sysinfo]             > Displays info about the system\n"
				"|    \--[pcname]              > Shows the name of the machine the OS is running on\n"
				"|    \--[shutdown]            > Shuts down the OS (PythonOS)\n"
				"\--{User Account}\n"
				"     \--[chg name]            > Changes the name for the current session\n"
				"     \--[chg passwd]          > Changes the password for the current session\n"
				"     \--[su # / su]           > \"su #\" changes to the superuser, \"su\" changes back\n"
				"     \--[whoami]              > Shows which user is currently active\n"
				+ st.RESET
			)

		#* SYSTEM COMMANDS

		elif cmd == "ip" or cmd == "ip address": #! Get the local IPv4 address
			print(st.CYAN + IPV4 + st.RESET)

		elif cmd == "pcname": #! Shows the name of the PC
			print(st.GRN + HOST + st.RESET)

		#* HISTORY
		elif cmd == "hist":
			print("\n".join(history))

		elif cmd.startswith("hist -c"):
			histClear()

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
			clearScreen.CLS()

		#* SWITCH USER

		elif cmd == "su #" or cmd == "su": #! Switch user to root/local user
			su.switchUser()

		#* CHANGE NAME / USERNAME / PASSWORD

		elif cmd == "chg name": #! Change name
			change.changeName()

		elif cmd == "chg passwd": #! Change password
			change.changePassword()

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