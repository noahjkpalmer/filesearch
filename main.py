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
	directorypath = "/media/hd_internal-02/www/liquidweb"#input("Directory Path: ")
	filesearcher = FileSearcher(directorypath)
	passwords = None
	with open("passwords.json") as f:
		passwords = json.load(f)
	data = filesearcher.search(passwords)

	for passtype in data.keys():
		log("TYPE: " + passtype)
		if not bool(data[passtype]):
			log("Password is not present in directory!")
		else:
			for location in data[passtype].keys():
				log("PATH: " + location + " | LINES: " + str(data[passtype][location]))
		log("")

if __name__ == '__main__':
	main()