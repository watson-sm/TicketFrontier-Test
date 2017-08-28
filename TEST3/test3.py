#!/usr/bin/env python3
#
# Name: Steven Watson
# Date: 8-27-2017
# Program: Ticket Frontier Test 3
# Purpose: Test ability to do simple data manipulation and processing

# import(s)
# sys - for commandline arguments
# os - for file operations
import sys
import os

def makeRecords(data):
    records = []
    dat = data.splitlines()
    for d in dat:
        rec = d.split()
        records.append(rec)
    return records

def yearInfo(data, year):
    # return list of calculated info
    # data is already sorted by year
    recyear = year
    distinctAccidents = 0
    avgWoundedPerAccident = 0
    totWounded = 0
    totAvgKilledPerAccident = 0
    totKilled = 0

    # Go through records to calculate values
    for d in data:
        if recyear == d[6]:
            distinctAccidents += 1
            totWounded += int(d[9])
            if int(d[7]) > totKilled:
                totKilled = int(d[7])

    avgWoundedPerAccident = round(totWounded / distinctAccidents)
    totAvgKilledPerAccident = round(totKilled / distinctAccidents)

    return [recyear, distinctAccidents, avgWoundedPerAccident, \
            totWounded, totAvgKilledPerAccident, totKilled]

def yearHeader():
    print('{0:8}'.format("Year"), end='')
    print('{0:28}'.format("Total Distinct Accidents"), end='')
    print('{0:32}'.format("Average Wounded Per Accident"), end='')
    print('{0:16}'.format("Total Wounded"), end='')
    print('{0:31}'.format("Average Killed Per Accident"), end='')
    print('{0:16}'.format("Total Killed"))

def yearInfoPrint(yearinfo):
    print("{year:8}{totDisAcc:^28}{avgWoundPer:^29}{totWound:^17}{avgKilledPer:^29}{totKilled:^20}" \
        .format(year = yearinfo[0], \
                totDisAcc = yearinfo[1], \
                avgWoundPer = yearinfo[2], \
                totWound = yearinfo[3], \
                avgKilledPer = yearinfo[4], \
                totKilled = yearinfo[5]))

def byYear(data):
    yearHeader()
    dat = sorted(data, key=lambda data: data[6])

    dyear = 0
    for d in dat:
        if d[6] != dyear:
            # Getting info for a new Year
            yinfo = yearInfo(dat, d[6])
            dyear = d[6]
            yearInfoPrint(yinfo)

def weekdayHeader():
    print('{0:8}'.format("Day"), end='')
    print('{0:28}'.format("Total Distinct Accidents"), end='')
    print('{0:16}'.format("Total Wounded"), end='')
    print('{0:16}'.format("Total Killed"))

def sortByDay(data):
    # A little messy but gets job done
    sun = []
    mon = []
    tue = []
    wed = []
    thu = []
    fri = []
    sat = []

    for d in data:
        if d[3] == "Sun":
            sun.append(d)
        if d[3] == "Mon":
            mon.append(d)
        if d[3] == "Tue":
            tue.append(d)
        if d[3] == "Wed":
            wed.append(d)
        if d[3] == "Thu":
            thu.append(d)
        if d[3] == "Fri":
            fri.append(d)
        if d[3] == "Sat":
            sat.append(d)

    return sun + mon + tue + wed + thu + fri + sat

def dayInfo(data, day):
    # return list of calculated info
    # data is already sorted by year
    recday = day
    distinctAccidents = 0
    totWounded = 0
    totKilled = 0

    # Go through records to calculate values
    for d in data:
        if recday == d[3]:
            distinctAccidents += 1;
            totWounded += int(d[9])
            if int(d[7]) > totKilled:
                totKilled = int(d[7])

    return [recday, distinctAccidents, totWounded, totKilled]

def dayInfoPrint(dayinfo):
    print("{day:8}{totDisAcc:^25}{totWound:^18}{totKilled:^14}" \
        .format(day = dayinfo[0], \
                totDisAcc = dayinfo[1], \
                totWound = dayinfo[2], \
                totKilled = dayinfo[3]))

def byWeekday(data):
    weekdayHeader()
    dat = sortByDay(data)

    day = ""
    for d in dat:
        if d[3] != day:
            # Getting info for a new Year
            dinfo = dayInfo(dat, d[3])
            day = d[3]
            dayInfoPrint(dinfo)

def main():
    # Check to see if an argument was passed at launch
    try:
        file_arg = sys.argv[1]
    except IndexError:
        print("Usage: ./test3.py <File Name>")
        sys.exit()

    with open(file_arg) as finput:
        data = finput.read()

    data_list = makeRecords(data)

    # By Year
    print("BY YEAR")
    byYear(data_list)

    print("")
    # By Weekday
    print("BY WEEKDAY")
    byWeekday(data_list)

# Make sure this is running as a standalone program and not an import
if __name__ == "__main__":
	main()
# End program
