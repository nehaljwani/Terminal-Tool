#!/usr/bin/python

#+------------------------------------------------------------------
# Import modules here
#+------------------------------------------------------------------
import os,time

#+------------------------------------------------------------------
# Function definitions and globals here
#+------------------------------------------------------------------

LAST_COMMAND="";

def printHello():
	os.system('clear')
	rows, columns = os.popen('stty size', 'r').read().split()
	print '#'*eval(rows)*2
	print '*'+'WELCOME TO THE TERMINAL TOOL'
	print '#'*eval(rows)*2

def fetchLastCommand():
	global LAST_COMMAND
	tempFilePtr=open("/tmp/last_command")
	LAST_COMMAND=tempFilePtr.read()
	tempFilePtr.close()

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
	
