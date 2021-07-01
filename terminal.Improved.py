import sys
import time
import json
import socket
import pickle
import stdiomask
from os import name, system

#*Configuring the basics of the terminal

cmd = ""
userID = ""

root = False
businessTools = False
HOST = socket.gethostname()
IP = socket.gethostbyname(HOST)
running = True

#*Functions

#Shows the # symbol when you are root user and $ when you are not
def symbol():
	if root:
		return "#"
	else:
		return "$"

#Makes it possible to print colored output
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

#Clears the screen when called
def cls():
	if name == "nt":
		_ = system("cls")
	else:
		_ = system("clear")

def login():
	userID = int(input("Enter userID: "))

cls()

#*______THE CODE ITSELF______

while running:
	userauth = input("Do you have an account")

