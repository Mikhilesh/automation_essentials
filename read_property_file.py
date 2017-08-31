import os

def read_properties(file,ky):
	"""
	Method to read values from the property file.This method converts the values of the file into python dictionary as key pair value 
  and parses it and returns the value.
  Usage as below:-
    obj = read_properties(FILE_NAME,KEY)
    FILE_NAME:- Name of the file, or the file name along with the path
    KEY:- Supply the key for getting the corresponding value for it in the 'obj' variable . 
  
	Files with variable and value for it.
  Sample of the file as follows:-
    one=1
    name=mike
    age=23
	"""
  
	d = {}	
	with open(file) as f:
		for line in f:			
			if "=" in line:
				key, value = line.split('=')
				d[key] = value
	return d[ky]
