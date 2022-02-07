from main import *

def changePassword():
	if config.setup.root:
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

def changeName():
	nameOfUser = input("Enter name: ")

	pwd = masking.getpass(prompt = "Enter password: ", mask = "*")
	if pwd == password:
		nameOfUser = nameOfUser.title()
		print(f"Name changed to {nameOfUser}")
	else:
		print(st.RED + "Password is incorrect!" + st.RESET)