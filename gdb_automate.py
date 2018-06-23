#!/usr/bin/env python3
"""
Module latex_parse
"""

__author__ = "Mat"
__version__ = "0.1.0"
__license__ = "GPL"


import re,sys
import json
import logging, getopt
import signal
import time
from hashlib import sha256
from random import randint
from colorama import init, Fore, Style
import os, sys
import datetime
from subprocess import call

EXIT_ERROR = -1
EXIT_SUCCESS = 1


def print_logo(program_name):
    rows, columns = os.popen('stty size', 'r').read().split()
    size = int(columns)-10
    print("\n\n"+Style.BRIGHT+Fore.YELLOW+program_name.center(size,"#")+"\n")
    print(Style.RESET_ALL)
    
def print_message(message, message_type):
    if message_type == "info":
        print(Style.BRIGHT + Fore.BLUE + "[!] " + Style.RESET_ALL + message)
    if message_type == "warning":
        print(Style.BRIGHT + Fore.YELLOW + "[!] " + Style.RESET_ALL + message)
    if message_type == "success":
        print(Style.BRIGHT + Fore.GREEN + "[+] " + Style.RESET_ALL + message)
    if message_type == "error":
        print(Style.BRIGHT + Fore.RED + "[!] " + Style.RESET_ALL + message)
    if message_type == "log":
        print(Style.BRIGHT + Fore.WHITE + "[~] " + Style.RESET_ALL + message)
    print(Style.RESET_ALL)


def lr_justify(left, right, width):
    return '{}{}{}'.format(left, ' '*(width-len(left+right)), right)



def print_purpose(PROGRAM_NAME):
    print("The purpose of this little tool is to generate\n"+
          "some automated gdb results by creating\n"+
          "a gdb script and executing it. As parameters it takes\n"
          "a core dump and the likely function of interest")
    sys.exit(EXIT_SUCCESS)

def print_usage(PROGRAM_NAME):
    print(PROGRAM_NAME+"\n  Usage: gdb_export [-b, --binary, -c, --core] [-i, --info]")
    sys.exit(EXIT_ERROR)



""" A simple tool to generate gdb debug output for some program and its core dump."""
def main():
    GDB_SCRIPT = """ set pagination off
                    set logging file gdb.txt
                    set logging on
                    file $$FILE$$
                    bt
                    i r
                    i f
                    x/100x $rsp
                    q
                    y
                     """

    PROGRAM_NAME = "[ Generate GDB output (automatically) ]"

    """ Main entry point of the app """
    print_logo(PROGRAM_NAME)

    try:
        options, remainder = getopt.getopt(sys.argv[1:], 'b:c:o:', ['binary=',
                                                                   'core=',
                                                                   ])
    except getopt.GetoptError as err:
        logging.error(err)
        sys.exit(EXIT_ERROR)

    binary = None
    core = None 
    gdb_script = None

    for opt, arg in options:
        if opt in ('-b', '--binary'):
            binary = arg
        elif opt in ('-c', '--core'):
            core = arg
        elif opt in ['-o','--out']:
            gdb_script = arg
        else:
            print_purpose(PROGRAM_NAME)
    
    if not binary or not core:
        print_usage(PROGRAM_NAME)

    if not gdb_script:
        gdb_script = "./cc.gds"

    # Change gdb output script
    GDB_SCRIPT = GDB_SCRIPT.replace("$$FILE$$",binary)

    file = open(gdb_script,"w") 
    print_message("Writing script to: "+gdb_script,"info") 
    file.write(GDB_SCRIPT)     
    file.close() 

    print_message("Creating GDB dump: "+"gdb "+binary+" "+core+" -x "+gdb_script,"info")
    if not call(["gdb", binary,core,"-x",gdb_script]):
        print_message("Results written to gdb.txt","success")

def exit_gracefully(signum, frame):
    global SELL_TRIGGER
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, ORIGINAL_SIGINT)

    try:
        if input("\nReally quit? (y/n)> ").lower().startswith('y'):
            sys.exit(EXIT_SUCCESS)

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        sys.exit(EXIT_SUCCESS)    

if __name__ == "__main__":
    """ This is executed when run from the command line """
    ORIGINAL_SIGINT = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    main()



        
