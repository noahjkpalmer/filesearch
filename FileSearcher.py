'''
	Noah Palmer
	A Family for Every Child
	File Searcher
'''

#System Imports
from os import listdir
from os.path import isdir, isfile, join

class FileSearcher():
	"""CONSTRUCTOR FOR FILESEARCHER"""
	def __init__(self, _directory):
		self.directory = _directory
		self.locations = {}

	def dirlist(self, directory):
		return [join(directory, f) for f in listdir(directory)]

	def search(self, _word):
		self.locations.clear()
		self.searchDirectory(_word, self.dirlist(self.directory))
		return self.locations

	def searchDirectory(self, _word, _paths):
		for path in _paths:
			if isdir(path):
				self.searchDirectory(_word, self.dirlist(path))
			else:
				self.searchFile(_word, path)

	def searchFile(self, _word, _filepath):
		try:
			with open(_filepath) as f:
				for i, line in enumerate(f):
					if _word in line:
						if _filepath not in self.locations:
							self.locations[_filepath] = []
						self.locations[_filepath].append(i+1)
		except:
			pass
		