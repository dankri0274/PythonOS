import masking
import main
from main import *

def switchUser():
	if config.setup.root:
		config.setup.root = False
	else:
		config.setup.rootRequest = masking.getpass(prompt = "root password: ", mask = "#")
		if config.setup.rootRequest == config.setup.rootpassword:
			config.setup.root = True
			clearScreen.CLS()
		else:
			print(st.RED + "Wrong password" + st.RESET)
			time.sleep(1)
			clearScreen.CLS()
