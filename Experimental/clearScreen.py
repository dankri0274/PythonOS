import os
from os import name, system

def CLS():
	if name == "nt":
		_ = system("cls")
	else:
		_ = system("clear")