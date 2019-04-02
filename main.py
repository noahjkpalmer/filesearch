'''
	Noah Palmer
	A Family for Every Child
	File Searcher
'''

#System Imports
from getpass import getpass
import json

#Module Imports
from FileSearcher import FileSearcher

def main():
	directorypath = input("Directory Path: ")
	filesearcher = FileSearcher(directorypath)
	passwords = None
	with open("passwords.json") as f:
		passwords = json.load(f)
	for passtype in passwords.keys():
		locations = filesearcher.search(passwords[passtype])
		print("Password Type: ", passtype)
		if not bool(locations):
			print("Password is not present in directory!")
		else:
			for key in locations.keys():
				print(key, locations[key])
		print("")

if __name__ == '__main__':
	main()