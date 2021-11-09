#app that rename in order all the file in a directory

import os

def main():
	i = 0
	path = "/Users/giancarlo/Desktop/fileDaRinominare/" #path of files to rename
	for filename in os.listdir(path):
		my_dest = "foto_sito_giancarlo" + str(i) + ".jpeg" #name and extensions of the files
		my_source =path + filename
		my_dest =path + my_dest
		os.rename(my_source, my_dest)
		i += 1

if __name__ == '__main__':
	main()

