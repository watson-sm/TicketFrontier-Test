#!/usr/bin/env python3
#
# Name: Steven Watson
# Date: 8-25-2017
# Program: Ticket Frontier Test 2
# Purpose: Test ability to retrieve remote information

# import(s)
# sys - for commandline arguments
# os - for file operations
# urllib.request - to request webpages
# urllib.error - incase of URLError
# calendar - month names
# re - regular expressions
import sys
import os
import urllib.request
import urllib.error
import calendar
import re

def getWEB(webpage):
    with urllib.request.urlopen(webpage) as web_url:
        return web_url.read().decode("utf8")

def formatForRecords(html):
    html = html.replace("&nbsp;", "")
    html = html[html.find("<TR><TD><A href"):]
    html = html.replace("<A", "\n<A")
    # Space pattern for 1 space followed by 1 or more whitespaces
    spc_pat = re.compile('[\s]\s+')
    html = spc_pat.sub(' ', html)
    return html.splitlines()

def main():
    # Check to see if an argument was passed at launch
    try:
        table_arg = sys.argv[1]
    except IndexError:
        # If there was no argument then set table_arg to None/null
        table_arg = None

    webpage = """http://www.isds.duke.edu/courses/Spring01/sta114/data/andrews.html"""
    webpath = """http://www.isds.duke.edu/courses/Spring01/sta114/data/"""
    entries = []

    # Generic run - no arguments passed at program launch
    html = getWEB(webpage)
    tbl_lines = formatForRecords(html)

    # Go through entries and only collect ones if they have a month name
    # in their description
    month_found = False
    for i in range(len(tbl_lines)):
        for m in range(1, len(calendar.month_name)):
            if calendar.month_name[m] in tbl_lines[i]:
                # calendar "May"(month) will false positive with "Mays"(person)
                # so do a check and make sure it is strictly "May"
                if calendar.month_name[m] == "May" and tbl_lines[i].find("May ") == -1:
                    continue
                else:
                    # Check to see if an listing has more than 1 month listed
                    # to not get duplicates
                    if month_found != False:
                        continue
                    else:
                        month_found = True

                        # Extract href
                        lslice_begin = tbl_lines[i].find("href=\"") + 6
                        lslice_end = tbl_lines[i].find("\">Table")
                        elink = webpath + tbl_lines[i][lslice_begin:lslice_end]

                        # Extract table number
                        numslice_begin = tbl_lines[i].find("Table") + 6
                        numslice_end = tbl_lines[i].find("</A>")
                        tbl_num = tbl_lines[i][numslice_begin:numslice_end]

                        # Create a record of table number and absolute link
                        record = [tbl_num, elink]
                        entries.append(record)
        # Toggle at end of a listing
        month_found = False

    # Check to see if a table was given at launch
    if table_arg is None:
        # Print table numbers and their absolute links
        for e in entries:
            print(str(e[0]) + "\t" + str(e[1]))
    else:
        for e in entries:
            if table_arg == e[0]:
                # If table_arg matches a record then download and output
                # information to file output.dat
                page = getWEB(e[1])
                fname = "output.dat"
                with open(fname, "w") as outfile:
                    print(page, file=outfile)

# Make sure this is running as a standalone program and not an import
if __name__ == "__main__":
	main()
# End program
