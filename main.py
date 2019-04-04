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

def log(data):
	logfile = open("log.txt", "a")
	logfile.write(data + "\n")
	logfile.close()
	print(data)


def main():
	directorypath = "../oldsite"#"/media/hd_internal-02/www/liquidweb"#input("Directory Path: ")
	filesearcher = FileSearcher(directorypath)
	passwords = None
	with open("passwords.json") as f:
		passwords = json.load(f)
	for passtype in passwords.keys():
		locations = filesearcher.search(passwords[passtype])
		log("Password Type: " + passtype)
		if not bool(locations):
			log("Password is not present in directory!")
		else:
			for key in locations.keys():
				log("Path: " + key + " | Lines: " + str(locations[key]))
		log("")

if __name__ == '__main__':
	main()