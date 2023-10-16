from os import name, system

# helpers.py
class Helpers:
	# init variable os
	def __init__(self):
		self.os = ""

	# function: return text
	def detect_os(self):
		if name == "nt":
			self.os = "windows"
		elif name == "posix":
			self.os = "linux"
		else:
			self.os = "unknown"

		return self.os

	# function: return function system() => clear screen
	def clear_screen(self):
		if self.detect_os() == "windows":
			system("cls")
		elif self.detect_os() == "linux":
			system("clear")
		else:
			pass