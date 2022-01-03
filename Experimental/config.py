from nec import socket
from PythonOS_DEV import *

class setup:
	#* ROOT_______________
	rootRequest = ""
	rootpassword = "root"
	root = False

	#* ENV________________
	running = True
	loggedIn = False

	interval = 0.5 #* For time.sleep()

	DEBUG = True #! DEBUGGING

	HOST = socket.gethostname()
	IPV4 = socket.gethostbyname(HOST)