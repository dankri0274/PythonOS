from main import *

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

def loading():
		for i in range(2):
			sys.stdout.write(st.GRN + "\r|" + st.RESET)
			time.sleep(config.setup.interval)
			sys.stdout.write(st.GRN + "\r/" + st.RESET)
			time.sleep(config.setup.interval)
			sys.stdout.write(st.GRN + "\r-" + st.RESET)
			time.sleep(config.setup.interval)
			sys.stdout.write(st.GRN + "\r\\" + st.RESET)
			time.sleep(config.setup.interval)