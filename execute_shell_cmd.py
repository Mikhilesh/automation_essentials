# coding: utf-8
# (C)   "Copyright 2017 , Mikhilesh Sekhar

from subprocess import Popen, PIPE, STDOUT
import subprocess
import os


def execute_cmd(cmd):
    """    
    Method to execute command and take the output to a variable.Uses the subprocess modules in python.
    @Args:- cmd(Command that needs to be executed)
    @Return:- Returns output of the command in the variable output.

    Python_version:- 2.7 and above
    Modules used: - 
    	from subprocess import Popen, PIPE, STDOUT
			import subprocess
			import os
	
	Usage:-
		1) execute_cmd(cmd) # Executes the command.
		2) obj = execute_cmd(cmd) # Executes the command and stores the output to variable(obj)

    """
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate() 
    output = out.strip()

    return output
