public class scroller{

	public static void main(String[] args) throws Exception{

		// set default values
		String message = ("hello world!");
		String cMessage;
		int trail = 15;
		int width = 80;
		int speed = 100;

		try{
			cMessage = args[0];
		}
		catch(Exception e){
			cMessage = message;
		}

		//String cMessage = message;

		/* pad the message with empty characters to the width of the display */
		for(int i=0; i<trail; ++i){
			cMessage = cMessage + ' ';
		}

		/* append extra copies of the message to the end of the message, if
			it + the extra trail whitespace is less/equal to the display
			width. Ensures display prints out correct width, and trailing
			whitespace is as specified, where multiple instances of the
			message appear on the display at once if short enough. */
		while(cMessage.length() <= width){
			cMessage = cMessage + cMessage;
		}

		/* initialise pointer positions for which parts of the message to 
			display at the beginning of the program. p1 at the first message
			character, p2 at the character that will be at the end of the
			display's width. */
		int p1 = 0;
		int p2 = width;
		System.out.print("\u001b[?25l");
		while (true){
			if(p2 < p1){
				System.out.print(cMessage.substring(p1, cMessage.length()) + 
					cMessage.substring(0, p2) + "\r");
				p1 = (p1 + 1)%cMessage.length();
				p2 = (p2 + 1)%cMessage.length();
			}

			else if(p1 < p2){
				System.out.print(cMessage.substring(p1, p2) + "\r");
				p1 = (p1 + 1)%cMessage.length();
				p2 = (p2 + 1)%cMessage.length();
			}
			Thread.sleep(speed);
		}

	}

	public void getHelp(){
		System.out.println(
			"\nList of options:\n\n"+
			"- (m)essage to display\n"+
			"- (t)railing whitespace characters to display after message,"+
				"\n  default=15\n"+
			"- (w)idth of display in columns to show message on,"+
				"\n  default=60\n"+
			"- (d)uration of each display update in seconds,"+
				"\n  default=0.2\n"+
			"--help to show this help message"
			);

		System.out.println(
			"\nUsage:\n\n"+
			"Print 'Hello World!' with the default trailspace of " +
			"15 characters,\ndisplay width of 60 columns and duration of " +
			"0.2s:\n\n" +
			"\tscroller.py -m 'Hello World!'\n\n"+
			"Print 'Hello World!' with a trailspace of 10 characters,\n"+
			"display width of 80 columns and duration of 0.1s:\n\n"+
			"\tscroller.py -m 'Hello World!' -t 10 -w 80 -d 0.1\n"
			);
		System.exit(0);
	}

}