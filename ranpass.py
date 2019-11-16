#!/usr/local/bin/python3

#    _____  _____
#   |  __ \|  __ \    AUTHOR: Pedro Rivero
#   | |__) | |__) |   ---------------------------------
#   |  ___/|  _  /    DATE: November 16, 2019
#   | |    | | \ \    ---------------------------------
#   |_|    |_|  \_\   https://github.com/pedrorrivero
#

# ---------------------------------------- #
#                LIBRARIES                 #
# ---------------------------------------- #

import secrets
import pyperclip
from argparse import ArgumentParser	# To input flags along with the command


# ---------------------------------------- #
#                  PARSER                  #
# ---------------------------------------- #

parser = ArgumentParser(description="generate cryptographically secure password ".upper() + "(default: copy to clipboard)")
parser.add_argument("-n", "--not-copy", action="store_true", dest="not_copy", default=False,
			help="not copy to clipboard and print in hidden format")
parser.add_argument("-a", "--ask", action="store_true", dest="ask", default=False, help="ask before copy to clipboard")
parser.add_argument("-p", "--print", action="store_true", dest="printer", default=False, help="print in hidden format")
parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=False,
			help="ask before copy to clipboard and print in hidden format")
options = parser.parse_args()


# ---------------------------------------- #
#        SECURE PASSWORD GENERATION        #
# ---------------------------------------- #

characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!?.,;:-+/*=()[]<>%@#$&"
passlen = 40
password="".join(secrets.choice(characters) for i in range(passlen))


# ---------------------------------------- #
#           OUTPUT AND INTERFACE           #
# ---------------------------------------- #

if options.not_copy: reply = 'n'
else: reply = 'y'

if options.ask or options.verbose:
	reply = str(input('Do you want to copy the generated password to your clipboard?'+' (y/n): ')).lower().strip()

if reply[0] == 'y':
	pyperclip.copy(password)
	print('Generated password copied to clipboard...')
else:
	print('Generated password not copied to clipboard...')

if options.not_copy or options.printer or options.verbose:
	print('GENERTED SECURE PASSWORD (HIDDEN):\033[8m'+password+'\033[0m')
