#!/usr/local/bin/python3

#    _____  _____
#   |  __ \|  __ \    AUTHOR: Pedro Rivero
#   | |__) | |__) |   ---------------------------------
#   |  ___/|  _  /    DATE: December 5, 2019
#   | |    | | \ \    ---------------------------------
#   |_|    |_|  \_\   https://github.com/pedrorrivero
#

# ---------------------------------------- #
#         LIBRARIES AND PARAMETERS         #
# ---------------------------------------- #

from math import log, ceil
import secrets
import pyperclip
from argparse import ArgumentParser

password_entropy_bits = 256
character_set = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!?.,;:-+/*=()[]{}<>%@#$&|'"

# ---------------------------------------- #
#             ARGUMENT PARSER              #
# ---------------------------------------- #

def parse_args():
	parser = ArgumentParser(description="generate cryptographically secure password ".upper() + "(default: copy to clipboard)")
	parser.add_argument("-n", "--not-copy", action="store_true", dest="not_copy", default=False,
						help="not copy to clipboard and print in hidden format")
	parser.add_argument("-a", "--ask", action="store_true", dest="ask", default=False, help="ask before copy to clipboard")
	parser.add_argument("-p", "--print", action="store_true", dest="printer", default=False, help="print in hidden format")
	parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=False,
						help="ask before copy to clipboard and print in hidden format")
	return parser.parse_args()


# ---------------------------------------- #
#        SECURE PASSWORD GENERATION        #
# ---------------------------------------- #

def generate_secure_password(password_entropy_bits, character_set):
	password_length = ceil(password_entropy_bits/log(len(character_set), 2))
	return "".join(secrets.choice(character_set) for i in range(password_length))


# ---------------------------------------- #
#          DISPLAY USER INTERFACE          #
# ---------------------------------------- #

def display_user_interface(options, password):
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


# ---------------------------------------- #
#                   MAIN                   #
# ---------------------------------------- #

options = parse_args()
password = generate_secure_password(password_entropy_bits, character_set)
display_user_interface(options, password)
