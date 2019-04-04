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
		self.data = {}

	def dirlist(self, directory):
		return [join(directory, f) for f in listdir(directory)]

	def search(self, _words):
		self.data.clear()
		for passtype in _words.keys():
			self.data[passtype] = {}
		self.searchDirectory(_words, self.dirlist(self.directory))
		return self.data

	def searchDirectory(self, _words, _paths):
		for path in _paths:
			if isdir(path):
				self.searchDirectory(_words, self.dirlist(path))
			else:
				self.searchFile(_words, path)

	def searchFile(self, _words, _filepath):
		try:
			with open(_filepath) as f:
				for i, line in enumerate(f):
					for passtype in _words.keys():
						if _words[passtype] in line:
							if _filepath not in self.data[passtype]:
								self.data[passtype][_filepath] = []
							self.data[passtype][_filepath].append(i+1)
		except:
			pass
		