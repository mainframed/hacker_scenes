#!/usr/bin/python

import curses, random, signal, os, time, sys, argparse, re, socket
from Queue import Queue
from select import select


#----------------------------\
# catch the ctrl-c to exit   | 
# and say something instead  | 
# of Punt!                   |
#----------------------------/
def signal_handler(signal, frame):
        print "EXCELSIOR!" + bcolors.ENDC
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

class bcolors:
    BLUE = '\033[94m'
    DARKBLUE = '\033[0;34m'
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[1;37m'
    ENDC = '\033[0m'
    DARKGREY = '\033[1;30m'
    
    def disable(self):
        self.BLUE = ''
        self.GREEN = ''
        self.YELLOW = ''
	self.DARKBLUE = ''
	self.PURPLE = ''
	seld.WHITE= ''
        self.RED = ''
        self.ENDC = ''

# from https://gist.github.com/msimpson/1096950
# I didn't write this. - SoF
def flames(cycles):
	screen  = curses.initscr()
	width   = screen.getmaxyx()[1]
	height  = screen.getmaxyx()[0]
	size    = width*height
	char    = [" ", ".", ":", "^", "*", "x", "s", "S", "#", "$"]
	b       = []
 
	curses.curs_set(0)
	curses.start_color()
	curses.init_pair(1,0,0)
	curses.init_pair(2,1,0)
	curses.init_pair(3,3,0)
	curses.init_pair(4,4,0)
	screen.clear
	for i in range(size+width+1): b.append(0)
	 
	for w in xrange(cycles):
	        for i in range(int(width/9)): b[int((random.random()*width)+width*(height-1))]=65
	        for i in range(size):
	                b[i]=int((b[i]+b[i+1]+b[i+width]+b[i+width+1])/4)
	                color=(4 if b[i]>15 else (3 if b[i]>9 else (2 if b[i]>4 else 1)))
	                if(i<size-1):   screen.addstr(  int(i/width),
	                                                i%width,
	                                                char[(9 if b[i]>9 else b[i])],
	                                                curses.color_pair(color) | curses.A_BOLD )
	 
	        screen.refresh()
	        screen.timeout(30)
	        if (screen.getch()!=-1): break
	 
	curses.endwin()

def co(stringer): #Old School Printer
    for c in stringer:
	sys.stdout.write( c )
        sys.stdout.flush()
        time.sleep(random.uniform(0, 0.35))
    print "\n",

def printer(s):
    for c in s:
	sys.stdout.write( c )
        sys.stdout.flush()
        time.sleep(random.uniform(0, 0.01))
    print "\n",

def ab(s):
    for c in s:
	sys.stdout.write( c )
        sys.stdout.flush()
        time.sleep(random.uniform(0, 0.2))
    print "\n",

def hackers_egg():
	print bcolors.GREEN
	co("ATD2125554240")
	printer("DIALING 212-555-4240\nCONNECTING....")
	time.sleep(2)
	print bcolors.PURPLE
	print "        ="
	print "        ===                                                      09/15/1995"
	print "        ====                     OTV Programming: (212)-555-4240"
	time.sleep(random.random())	
	print "        ====="
	print "       =======                   Welcome to the NYC Programming Management"
	time.sleep(random.random())	
	print "     =========                   System of OTV. Unauthorized use is stricly"
	print "    ==========                   prohibited."
	time.sleep(random.random())	
	print "   =========="
	time.sleep(random.random())	
	print "  ==========                     Help/Support: (212)-555-4321"
	print "  ========="
	time.sleep(random.random())	
	print "  ======= _____ _____ _____      1) Ad Billing Reports"
	print "   ===== |     |_   _|  |  |     2) Finance Application Access"
	time.sleep(random.random())	
	print "    ==== |  |  | | | |  |  |     3) ARPS - DO NOT TOUCH!! -j"
	print "     === |_____| |_|  \___/      4) Tape Cartridge Cataloge"
	print "       ="
	print "\n  Please Enter application choice:"
	time.sleep(2)
	print bcolors.GREEN
	print "3"
	time.sleep(random.random())
	print bcolors.BLUE	
	printer('''\n\n     Welcome to ARPS please select region/channel:
      1) ARPS 342  - PRE-ROLL
      2) ARPS 331  - ON AIR!
      3) ARPS 217  - TEST SYSTEM
      4) ARPS 564  - KYRON
      5) ARPS 423  - DECOMISSIONED
      6) EMTPY
      7) EMPTY\n''')

	time.sleep(3)
	print bcolors.GREEN
	co("ARPS 331")
	print bcolors.YELLOW
	ab("  ENTERING\n  ARPS 331")
	time.sleep(2)
	printer('''
       _
      / \\
     / _ \    utomated          -----------------------------------------
    / ___ \                     -                                       -
  _/ /   \ \_                   - WARNING WARNING WARNING WARNING WARNI -
 |____|_|____|                  - NG WARNING WARNING WARNING WARNING WA -
   ______                       -                                       -
  |_   __ \                     -                                       -
    | |__) |                    -   This systems is currently:          -
    |  __ /   ecording          -                 ON-AIR                -
   _| |  \ \_                   -                                       -
  |____|_|___|                  -          Make changes to              -
   ______                       -          the Schedule first.          -
  |_   __ \                     -                                       -
    | |__) |  layback           -          Only Use this System         -
    |  ___/                     -          for EMERGENCIES              -
   _| |_                        -                                       -
  |_____|_                      -                                       -
    _____                       -                                       -
  .' ____ \                     - RNING WARNING WARNING WARNING WARNING -
  | (___ \_|                    - WARNING WARNING WARNING WARNING WARN  -
   _.____`.  ystem              -                                       -
  | \____) |                    -----------------------------------------
   \______.'
''')

	print bcolors.GREEN
	co("E 00-06")
	print bcolors.YELLOW
	printer("EJECTING TAPE IN PLAYER 00-06")
	print bcolors.GREEN
	co("I 03-19")
	print bcolors.YELLOW
	printer("INSERTED TAPE 03-19 IN PLAYER 00-06\nPLAYING TAPE 03-19: Outer Limits 304")
	time.sleep(5)
	os.system("clear")
	flames(35)
	print bcolors.RED
	co( '''\n\n\
   U HAVE TREAD
   UPON MY DOMAIN &
   MUST NOW SUFFER

     WHO R U?
''' )
	print bcolors.GREEN
	time.sleep(2)
	co("   ZERO\b\b\b\bCRASH OVERRIDE")
	co("   WHO WANTS TO KNOW?")
	time.sleep(2)
	os.system("clear")
	flames(40)
	print bcolors.RED
	co('''\n\n\n\t\t\tACID BURN\n\n''')
	print bcolors.YELLOW
	printer("TAPE 03-19 EJECTED FROM PLAYER 00-06")
	time.sleep(2)
	print bcolors.GREEN
	co("E 00-06,I 05-17")
	print bcolors.YELLOW
	printer("TAPE 00-89 EJECTED FROM PLAYER 00-06\nINSERTED TAPE 05-17")
	time.sleep(4)
	os.system("clear")
	flames(15)
	print bcolors.RED
	ab('''      ACID BURN
     SEZ LEAVE B 4
     U R EXPUNGED
''')

	print bcolors.YELLOW
	printer("TAPE ARM 2-345 HAS LOST TAPE 12-1094\nTAPE ARM 2-345 HAS REGAINED TAPE 12-1094\nTAPE 12-1094 INSERTED")
	time.sleep(4)
	os.system("clear")
	flames(15)
	print bcolors.RED
	ab('''        I WILL
     SWAT U LIKE
     THE FLY U R''')

	print bcolors.GREEN
	co("M 12-1094,R 12-1094")
	print bcolors.YELLOW
	printer("TAPE ARM 2-354 ENTERING IN TO MAINTENANCE MODE\nREMOVING TAPE 12-1094 FROM CATALOG")
	print bcolors.GREEN
	co("I 03-85")
	print bcolors.YELLOW
	printer("TAPE 03-85 INSERTED IN TO PLAYER 00-06\n\n")

	time.sleep(3)
	os.system("clear")
	flames(15)
	print bcolors.RED
	ab('''        I WILL
     SNAP YOUR BACK
     LIKE A TOOTHPICK''')


	print bcolors.YELLOW
	printer("TAPE 03-85 EJECT & REMOVED FROM PLAYER 00-06\nTAPE 445-4 INSERTED IN TO PLAYER 00-06")

	print bcolors.GREEN
	co("   MESS WITH THE BEST\n   DIE LIKE THE REST")
	time.sleep(4)
	os.system("clear")
	flames(15)
	print bcolors.RED
	ab('''        YOU ARE
       TERMINATED''')
	time.sleep(1)
	print bcolors.WHITE
	printer("CONNECTION TERMINATED")

	print bcolors.ENDC
	sys.exit(0)

hackers_egg()
