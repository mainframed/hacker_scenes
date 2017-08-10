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


def osp(stringer): #Old School Printer
    for c in stringer:
        sys.stdout.write( c )
        sys.stdout.flush()
        time.sleep(random.uniform(0, 0.35))
    print "\n",

def mcp(s):
    for c in s:
        sys.stdout.write( c )
        sys.stdout.flush()
        time.sleep(random.uniform(0, 0.1))
    print "\n",



def encom_easter():
    print bcolors.BLUE
    osp("D9165747830")
    print bcolors.GREEN
    time.sleep(1.5) 
    print "\nWelcome to Encom Master System\nUnauthorized access is forbidden."
    print "\n\nEEEEEEE"
    print "EE      nn nnn    cccc  oooo  mm mm mmmm"
    time.sleep(random.random())
    print "EEEEE   nnn  nn cc     oo  oo mmm  mm  mm"
    print "EE      nn   nn cc     oo  oo mmm  mm  mm"
    time.sleep(random.random()) 
    print "EEEEEEE nn   nn  ccccc  oooo  mmm  mm  mm\n"
    print "READY"
    print bcolors.BLUE
    time.sleep(random.random()) 
    osp("CLU")                                          
    time.sleep(random.random())     
    print bcolors.GREEN
    mcp("REQUEST ACCESS TO CLU PROGRAM")
    time.sleep(random.random()) 
    print bcolors.BLUE
    osp("CODE 6 PASSWORD TO MEMORY 0222")
    time.sleep(random.random())
    print bcolors.GREEN
    mcp("ILLEGAL CODE...")
    mcp("CLU PROGRAM DETACHED FROM SYSTEM")
    time.sleep(1)
    print bcolors.BLUE
    osp("REQUEST ACCESS TO CLU PROGRAM")    
    time.sleep(random.random()) 
    print bcolors.GREEN
    mcp("LAST LOCATION: HIGH CLEARANCE MEMORY C4")
    print bcolors.RED
    mcp("\nCONNECTION CLOSED\n")
    time.sleep(random.random())
    print bcolors.BLUE
    mcp("READY")
    time.sleep(random.random())
    osp("FUCK")
    time.sleep(random.random())
    mcp("\n?SYNTAX ERROR")
    mcp("READY")
    time.sleep(4)   
    osp("D9165747830")  
    time.sleep(random.random()) 
    print bcolors.GREEN
    print "\nWelcome to Encom Master System\nUnauthorized access is forbidden."
    print "\n\nEEEEEEE"
    print "EE      nn nnn    cccc  oooo  mm mm mmmm"
    time.sleep(random.random())
    print "EEEEE   nnn  nn cc     oo  oo mmm  mm  mm"
    print "EE      nn   nn cc     oo  oo mmm  mm  mm"
    time.sleep(random.random()) 
    print "EEEEEEE nn   nn  ccccc  oooo  mmm  mm  mm\n"
    print "READY"
    time.sleep(random.random()) 
    print bcolors.BLUE
    osp("ACCESS CODE 6. PASSWORD SERIES PS 17.")
    osp("REINDEER FLOTILLA -WRITE")
    time.sleep(random.random()) 
    os.system("clear")
    print bcolors.RED
    print "\n\n\n\n\n"
    flynn = "YOU SHOULDN'T HAVE COME BACK FLYNN"
    mcp(flynn)
    time.sleep(3)
    print bcolors.GREEN
    mcp("READY")
    print bcolors.BLUE
    time.sleep(random.random()) 
    osp("REACTIVATE HIGH CLEARANCE MEMORY LOCATION C4")
    time.sleep(random.random()) 
    print bcolors.GREEN
    osp("................")
    time.sleep(random.random())
    osp("................")
    osp("................") 
    time.sleep(random.random())
    mcp("CODE SERIES C49-123 ... ACTIVATE.")
    time.sleep(random.random()) 
    mcp("CODE SERIES C4D-E38 ... ACTIVATE.")
    time.sleep(random.random()) 
    mcp("CODE SERIES C4C-036 ... ACTIVATE.")   
    time.sleep(random.random())
    os.system("clear")
    print bcolors.RED
    print "\n\n\n\n\n"  
    flynn = "THAT ISN'T GOING TO DO YOU ANY GOOD FLYNN"
    mcp(flynn)
    time.sleep(3)
    print bcolors.GREEN
    print "\n\nREADY"
    time.sleep(random.random()) 
    print bcolors.BLUE
    osp("DIVIDE SYS6.RAND.FLOAT BY ZERO")
    print "\n\n"
    print bcolors.GREEN
    osp("xXxXXXxXX.../\//////////////")
    mcp("   c  x   $   @  #  */  ****")
    mcp(" 00 <.  $ v g   b...........")
    time.sleep(2)
    os.system("clear")
    print "\n\n"
    time.sleep(random.random()) 
    print bcolors.RED
    flynn = "STOP FLyNN!\nYOU ReALIzE I CAN\T ALL0W THIS!"
    mcp(flynn)
    time.sleep(4)
    print bcolors.GREEN
    mcp("READY")
    time.sleep(random.random()) 
    print bcolors.BLUE
    print bcolors.WHITE+"\n[TRON] "+bcolors.GREEN+"",
    mcp("COMMUNICATIONS SOCKET ACCESSED")
    print bcolors.WHITE+"\n[TRON] "+bcolors.GREEN+"",
    mcp("AWAITING SOFTWARE UPDATE FROM: USER")
    time.sleep(3)
    print bcolors.BLUE
    osp("SUBMIT TPE4:ALAN./TRON.UPDATE")
    osp("......................................")
    time.sleep(2)
    print bcolors.WHITE+"\n[TRON] "+bcolors.GREEN+"",
    mcp("TRON PROGRAM UPDATED\n")
    print bcolors.WHITE+"\n[TRON] "+bcolors.GREEN+"",
    mcp("ILLEGAL MEMORY USAGE: DSK1:CHESS./MCP\n")
    time.sleep(random.random())
    print bcolors.WHITE+"\n[TRON]"+bcolors.GREEN+"",
    mcp(" DEACTIVATE MCP IN PROGRESS")
    time.sleep(random.random()) 
    mcp("...........................")
    time.sleep(random.random())
    mcp("...........................")
    mcp("...........................") 
    print bcolors.WHITE+"\n[TRON]"+bcolors.GREEN+"",
    mcp(" MCP DEACTIVATED")
    time.sleep(5)
    os.system("clear")
    mcp("READY")
    time.sleep(random.random())
    print bcolors.BLUE
    osp("PRINT HISTORY - DSK1:DILLINGER.GAMES.ACCOUNTING.TRASH")
    print bcolors.GREEN
    time.sleep(random.random()) 
    print 'DSK1:DILLINGER.GAMES.ACCOUNTING.TRASH'
    time.sleep(random.random())
    print '--------------------------------------------------------------------------------'
    print 'Access control:'
    time.sleep(random.random())
    print '    This User: Encryption protection (level 5)'
    time.sleep(random.random())
    print '    Other Users: Access Denied'
    print 'Access History:'
    time.sleep(random.random())
    print '    File name   Project name       File Created       Last Access'
    time.sleep(random.random())
    print '    WORM        "Worm"             04-AUG by FLYNN    30-AUG by DILLINGER'
    print '    TANK        "Tank Hunter"      18-MAY by FlYNN    30-AUG by DILLINGER'
    time.sleep(random.random())
    print '    LITBIKE     "Light Bike"       22-JUN by FLYNN    30-AUG by DILLINGER'
    print '    PARA        "Space Paranoids"  21-MAR by FLYNN    30-AUG by DILLINGER'
    print bcolors.ENDC
    time.sleep(10)
    sys.exit(0)

encom_easter()
