#!/usr/bin/env python

import os

merged_name = "main.css"

def mergeCssFiles():
	conf = open("source.txt").read().split('\n')
	fileContents = []

	if len(conf) < 2:
		print("Cannot complete merge, file paths in source.txt missing.")
		return

	elif conf[0] == conf[1]:
		print("The source / destination folders are the same. Please put two different paths in the source.txt file and run the script again.")
		return 

	#1st line = css file location
	for file in os.listdir(conf[0]):
		if file.endswith(".css"):
			fpath = os.path.join(conf[0], file)
			cssfile = open(fpath).read()

			fileContents.append("\n /* " + file + " */ \n")
			fileContents.append(cssfile)


	#2nd line = output location
	outputD = conf[1]

	#create the new merged file
	merged = open(os.path.join(outputD, merged_name),"w+")
	for f in fileContents:
		merged.write(f)

	merged.close() 


mergeCssFiles()