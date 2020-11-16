import sys, time, getopt
from signal import signal, SIGINT

def handler(signal_received, frame):
	# Handle any cleanup here
	print('\nSIGINT or CTRL-C detected. Exiting gracefully')
	# bring back the console cursor on the terminal when SIGINT/CTRL-C
	# detected, as otherwise it will continue to be hidden for the
	# rest of the terminal session
	print("\u001b[?25h", end="")
	exit(0)

def getHelp():
	# print help information, then quit
	print("\nList of options:\n\n"+
		"- (m)essage to display\n"+
		"- (t)railing whitespace characters to display after message, "+
			"default=15\n"+
		"- (w)idth of display in columns to show message on, default=60\n"+
		"--help to show this help message")
	sys.exit(0)

def main():
	# Tell Python to run the handler() function when SIGINT is recieved
	signal(SIGINT, handler)

	# set default values
	message = None
	trail = 15
	width = 60

	argv = sys.argv[1:]

	# try getting supported parameters and args from command line
	try:
		opts, args = getopt.getopt(argv, "m:t:w:", 
			["message=", "trail=", "width=", "help"])
	except:
		print("Error parsing options")
		getHelp()

	# assign variables based on command line parameters and args
	for opt, arg in opts:
		if opt in ['-m', '--message']:
			try:
				message = str(arg)
			except:
				print("Error parsing message!")
				getHelp()
		elif opt in ['-t', '--trail']:
			try:
				trail = int(arg)
			except:
				print("Error parsing trail!")
				getHelp()
		elif opt in ['-w', '--width']:
			try:
				width = int(arg)
			except:
				print("Error parsing width!")
				getHelp()
		elif opt in ['--help']:
			getHelp()

	# print help if no message is entered
	if message == None:
		print("No message entered!")
		getHelp()

	# pad the message with empty characters to the width of the display
	cMessage = message + " "*trail

	# append extra copies of the message to the end of the message,
	# if it + the extra trail whitespace is shorter than the display width.
	# Ensures the display prints out the correct width, and the trailing
	# whitespace is as specified, where multiple instances of the message
	# appear on the display at once if short enough.
	while(len(cMessage) < width):
		cMessage = cMessage + cMessage

	# initialise pointer positions for which parts of the message to display
	# at the beginning of the program. p1 at the first message character,
	# p2 at the character that will be at the end of the display's width.
	p1 = 0
	p2 = width

	while True:
		if(p2 < p1):
			# get rid of the console cursor on the screen
			print("\u001b[?25l", end="")
			print(cMessage[p1:len(cMessage)] + cMessage[0:p2], end="\r")
			p1 = (p1+1)%len(cMessage)
			p2 = (p2+1)%len(cMessage)

		elif(p1 < p2):
			# get rid of the console cursor on the screen
			print("\u001b[?25l", end="")
			print(cMessage[p1:p2] + cMessage[p1:0], end="\r")
			p1 = (p1+1)%len(cMessage)
			p2 = (p2+1)%len(cMessage)

		time.sleep(0.2)

if __name__ == '__main__':
	main()