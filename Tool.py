#!/usr/bin/python

#+------------------------------------------------------------------
# Import modules here
#+------------------------------------------------------------------
import os,time,commands

#+------------------------------------------------------------------
# Function definitions and globals here
#+------------------------------------------------------------------
USER=commands.getstatusoutput('whoami')[1]
LAST_COMMAND="";
LAST_OUTPUT="";
LAST_COMMAND_FILE="/tmp/last_command_"+USER
LAST_OUTPUT_FILE="/tmp/last_output_"+USER

def printHello():
	os.system('clear')
	rows, columns = os.popen('stty size', 'r').read().split()
	print '#'*eval(rows)*2
	print '*'+'WELCOME TO THE TERMINAL TOOL'
	print '#'*eval(rows)*2

def fetchLastCommand():
	global LAST_COMMAND
	tempFilePtr=open(LAST_COMMAND_FILE)
	LAST_COMMAND=tempFilePtr.read()
	tempFilePtr.close()

def fetchLastOutput():
	global LAST_OUTPUT
	tempFilePtr=open(LAST_OUTPUT_FILE)
	LAST_OUTPUT=tempFilePtr.read()
	tempFilePtr.close()
	
def executeLastCommand():
	os.system("sh "+LAST_COMMAND_FILE+" > "+LAST_OUTPUT_FILE )

#+------------------------------------------------------------------
# Main flow of code 
#+------------------------------------------------------------------

os.system('PS1=""')
os.system('clear')

while True:
	global LAST_COMMAND
	currentCommand=LAST_COMMAND
	time.sleep(1)
	fetchLastCommand()
	if currentCommand!=LAST_COMMAND:
		printHello()
		print LAST_COMMAND
		executeLastCommand()
		fetchLastOutput()
		print LAST_OUTPUT
