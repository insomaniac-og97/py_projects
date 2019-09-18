#!/usr/bin/env python

# script to convert roman numerals into arabic decimal notation

def numerus(roman_num):
    # set up roman to arabic dict
    r2a = {
         'i': 1,
         'v': 5,
         'x': 10,
         'l': 50,
         'c': 100,
         'm': 1000
    }
    # instantiate running total and subtractor e.g. the 'I' in 'IV' must be carried to the next position and subtracted
    total = int()
    subtractor = int()

    # validate input string
    rn = roman_num.lower()
    for char in rn:
        if not char in r2a.keys():
            print("Invalid numeral {0} in alleged roman numeral '{1}'!".format(char,roman_num))
            return -1

    # iterate validated string, adding to total or becoming subtractor
    for i in range(0,len(rn)):
        # print("Processing '{0}'".format(rn[i]))
        #  this position is subtractor if next is greater
        try:
            if r2a[rn[i+1]] > r2a[rn[i]]:
                subtractor = r2a[rn[i]]
                # print("subtractor is " + str(subtractor))
                continue
        # account for last position
        except IndexError:
            pass
        # if we have a subtractor, subtract it from current value and add that to the total
        if subtractor > 0:
            to_add = r2a[rn[i]] - subtractor
            # print("adding {0} which is {1} minus {2}".format(to_add, r2a[rn[i]], subtractor))
            subtractor = 0
            total += to_add
        # else add current value to total
        else:
            print("adding {0} without subtractor".format(r2a[rn[i]]))
            total += r2a[rn[i]]

    # return the running total
    return total
