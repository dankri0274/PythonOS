import sys

STR_TYPE = str # type: type

try:
	from typing import List
except ImportError:
	pass # There is no typing module on Python 2, but that's fine because we use the comment-style of type hints.

if sys.platform == 'win32':
	# For some reason, mypy reports that msvcrt doesn't have getch, ignore this warning:
	from msvcrt import getch # type: ignore

	def getpass(prompt='Password: ', mask='*'):
		# type: (str, str) -> str
		if not isinstance(prompt, STR_TYPE):
			raise TypeError('prompt argument must be a str, not %s' % (type(prompt).__name__))
		if not isinstance(mask, STR_TYPE):
			raise TypeError('mask argument must be a zero- or one-character str, not %s' % (type(prompt).__name__))
		if len(mask) > 1:
			raise ValueError('mask argument must be a zero- or one-character str')

		if mask == '' or sys.stdin is not sys.__stdin__:
			# Fall back on getpass if a mask is not needed.
			import getpass as gp
			return gp.getpass(prompt)

		enteredPassword = [] # type: List[str]
		sys.stdout.write(prompt)
		sys.stdout.flush()
		while True:
			key = ord(getch())
			if key == 13: # Enter key pressed.
				sys.stdout.write('\n')
				return ''.join(enteredPassword)
			elif key in (8, 127): # Backspace/Del key erases previous output.
				if len(enteredPassword) > 0:
					# Erases previous character.
					sys.stdout.write('\b \b') # \b doesn't erase the character, it just moves the cursor back.
					sys.stdout.flush()
					enteredPassword = enteredPassword[:-1]
			elif 0 <= key <= 31:
				# Do nothing for unprintable characters.
				pass
			else:
				# Key is part of the password; display the mask character.
				char = chr(key)
				sys.stdout.write(mask)
				sys.stdout.flush()
				enteredPassword.append(char)

else: #* macOS and Linux
	import tty, termios
	def getch():
		# type: () -> str
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

	def getpass(prompt='Password: ', mask='*'):
		# type: (str, str) -> str
		if not isinstance(prompt, STR_TYPE):
			raise TypeError('prompt argument must be a str, not %s' % (type(prompt).__name__))
		if not isinstance(mask, STR_TYPE):
			raise TypeError('mask argument must be a zero- or one-character str, not %s' % (type(prompt).__name__))
		if len(mask) > 1:
			raise ValueError('mask argument must be a zero- or one-character str')

		if mask == '' or sys.stdin is not sys.__stdin__:
			# Fall back on getpass if a mask is not needed.
			import getpass as gp
			return gp.getpass(prompt)

		enteredPassword = [] # List[str]
		sys.stdout.write(prompt)
		sys.stdout.flush()
		while True:
			key = ord(getch())
			if key == 13: # Enter key pressed.
				sys.stdout.write('\n')
				return ''.join(enteredPassword)
			elif key in (8, 127): # Backspace/Del key erases previous output.
				if len(enteredPassword) > 0:
					# Erases previous character.
					sys.stdout.write('\b \b') # \b doesn't erase the character, it just moves the cursor back.
					sys.stdout.flush()
					enteredPassword = enteredPassword[:-1]
			elif 0 <= key <= 31:
				# Do nothing for unprintable characters.
				# TODO: Handle Esc, F1-F12, arrow keys, home, end, insert, del, pgup, pgdn
				pass
			else:
				# Key is part of the password; display the mask character.
				char = chr(key)
				sys.stdout.write(mask)
				sys.stdout.flush()
				enteredPassword.append(char)