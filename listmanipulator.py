import itertools as it
import sys
from days_months_years import days, months, years
help = "[Help] Usage: python3 listmanipulator.py option list\nOptions:\n-c (combine)\n-uc (upper case)\n-lc (lower case)\n-fuc (first upper case)\n-ad (add date)"
if len(sys.argv) == 1:
    print(help)
    sys.exit(1)
elif len(sys.argv) > 3:
    print("[Error] Provide 1 option and 1 list!")
    print(help)
    sys.exit(1)

base_list = open(sys.argv[2], "r")

def uppercase(base_list):
    my_file = open(sys.argv[2]+"_uc" ,"w")
    for line in base_list:
        my_file.write(line.upper())

def lowercase(base_list):
    my_file = open(sys.argv[2]+"_lc" ,"w")
    for line in base_list:
        my_file.write(line.lower())

def first_uc(base_list):
    my_file = open(sys.argv[2]+"_fuc" ,"w")
    for line in base_list:
        my_file.write(line.title())

def combine(base_list, combine_with):
    combine = open(combine_with, "r")
    my_file = open(sys.argv[2]+"_"+str(combine_with) ,"w")
    templist = []
    templist1 = []
    for line in base_list:
        templist.append(str(line).replace('\n', ""))
    for line in combine:
        templist1.append(str(line).replace('\n', ""))
    combinations = (it.product(templist, templist1, repeat=1))
    for i in combinations:
        guess = ""
        for e in i:
            guess = str(guess) + str(e)
        my_file.write(guess + '\n')

def add_date(base_list):
    my_file = open(sys.argv[2]+"_ad" ,"w")
    templist = []
    for line in base_list:
        templist.append(str(line).replace('\n', ""))
    combinations = (it.product(templist, days, months, years, repeat=1))
    for i in combinations:
        guess = ""
        for e in i:
            guess = str(guess) + str(e)
        my_file.write(guess + '\n')



if sys.argv[1] == "-c":
    combine_with = input("List to combine with: ")
    combine(base_list, combine_with)
elif sys.argv[1] == "-uc":
    uppercase(base_list)
elif sys.argv[1] == "-lc":
    lowercase(base_list)
elif sys.argv[1] == "-fuc":
    first_uc(base_list)
elif sys.argv[1] == "-ad":
    add_date(base_list)
else:
    print("[Error] Wrong option!")
    print(help)
