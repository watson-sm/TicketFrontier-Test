#!/usr/bin/env python3
#
# Name: Steven Watson
# Date: 8-25-2017
# Program: Ticket Frontier Test 2
# Purpose: Test ability to retrieve remote information

# import(s)
# sys - for commandline arguments
# urllib.request - to request webpages
# urllib.error - incase of URLError
# urllib.parse - for parsing the URL(s)
import sys
import urllib.request
import urllib.error
import urllib.parse

def main():
    # Check to see if an argument was passed at launch
    try:
        table_arg = sys.argv[1]
    except IndexError:
        # If there was no argument then set table_arg to None/null
        table_arg = None

    if table_arg is None:
        # Generic run
        try:
            web_url = urllib.request.urlopen("http://www.isds.duke.edu/courses/Spring01/sta114/data/andrews.html")
        except urllib.error.URLError as err:
            #print(err, "in", web_url)
            print("There was a problem accessing the webpage.")
            sys.exit()

        html = web_url.read().decode("utf8")

        #print(html)
    else:
        print("Table:", table_arg)

# Make sure this is running as a standalone program and not an import
if __name__ == "__main__":
	main()
# End program
