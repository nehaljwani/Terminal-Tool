#!/usr/bin/python

#+------------------------------------------------------------------
# Import modules here
#+------------------------------------------------------------------
import os,time

#+------------------------------------------------------------------
# Function definitions and globals here
#+------------------------------------------------------------------

LAST_COMMAND="";
LAST_OUTPUT="";

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

def fetchLastOutput():
	global LAST_OUTPUT
	tempFilePtr=open("/tmp/last_output")
	LAST_OUTPUT=tempFilePtr.read()
	tempFilePtr.close()
	
def executeLastCommand():
	os.system("sh /tmp/last_command > /tmp/last_output")

#+------------------------------------------------------------------
# Main flow of code 
#+------------------------------------------------------------------

os.system('PS1=""')
os.system('clear')
os.system('chmod 777 /tmp/last_command')

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
