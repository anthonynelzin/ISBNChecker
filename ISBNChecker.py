#!/usr/bin/env python3

"""
	Anthony Nelzin-Santos
	anthony@nelzin.fr
	https://anthony.nelzin.fr

	European Union Public License 1.2
"""

import argparse

# Clean the provided ISBN
def clean_isbn(isbn):
	# Remove hyphens and spaces
	isbn = isbn.replace("-", "").replace(" ", "")
	return isbn
	
# Use the appropriate method to check the ISBN
def check_isbn(isbn):
	if len(isbn) == 10:
		return check_isbn_10(isbn)
	elif len(isbn) == 13:
		return check_isbn_13(isbn)
	else:
		raise ValueError("You didn't enter a valid ISBN.")
		
# Check the validity of an ISBN-10
def check_isbn_10(isbn):
	# The check digit has to be excluded
	digits = list(isbn)[:-1]
	
	# Each of the digits is multiplied by a weight descending from 10 and everything is summed together
	sum = 0
	weight = 10
	for digit in digits:
		sum += weight*int(digit)
		weight -= 1
	
	# The check digit is 11 minus the remainder of the sum divided by 11
	check = 11 - (sum%11)
	
	# If the previous operation equals 10, the check digit is X
	if check == 10:
		check = "X"
	
	# If the previous operation equals 11, the check digit is 0
	if check == 11:
		check = 0
		
	# If the computed check digit equals the provided check digit, we have a valid ISBN-10
	if isbn[-1] == str(check):
		print(isbn + " is a valid ISBN-10 (check number: " + str(check) + ").")
		return isbn
	else:
		raise ValueError("The ISBN " + isbn + " is not a valid ISBN-10.")
	
# Check the validity of an ISBN-13
def check_isbn_13(isbn):
	# The check digit has to be excluded
	digits = list(isbn)[:-1]
	
	# Odd-positioned numbers are multiplied by 1, even ones by 3, and everything is summed together
	sum = 0
	position = 0
	for digit in digits:
		if (position%2 == 0):
			sum += int(digit)
		else:
			sum += 3*int(digit)
		position += 1
	
	# The check digit is 10 minus the remainder of the sum divided by 10
	check = 10 - (sum%10)
	
	# If the previous operation equals 10, the check digit is 0
	if check == 10:
		check = 0
	
	# If the computed check digit equals the provided check digit, we have a valid ISBN-13
	if isbn[-1] == str(check):
		print(isbn + " is a valid ISBN-13 (check number: " + str(check) + ").")
		return isbn
	else:
		raise ValueError("The ISBN " + isbn + " is not a valid ISBN-13.")
	
def main():
	parser = argparse.ArgumentParser(description="Checks whether an ISBN-10 or ISBN-13 is valid or not.")
	parser.add_argument("isbn", help="An ISBN-10 or ISBN-13.")
	
	args = parser.parse_args()
	isbn = clean_isbn(args.isbn)
	isbn = check_isbn(isbn)
	
	return isbn
	
def ISBNChecker(isbn):
	isbn = clean_isbn(isbn)
	isbn = check_isbn(isbn)
	
	return isbn
	
if __name__ == '__main__':
	main()