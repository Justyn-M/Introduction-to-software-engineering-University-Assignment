#
# Category2.py - code for category 2
#

# Converting a number which represents a time given in hours to minutes and vice versa, and time given in minute to seconds ad vice versa
import csv

def Hours2Mins():
    print('\n#### Hours to Minutes Convertor ####\n')
    hours = int(input('Enter the number of hours: '))
    if hours < 0:
        print('Invalid number of hours')
    else:
        print('\nConverting Hours to Minutes....\n')
        mins = 60 * hours
        print('\nMinutes =\n', mins)
    print('\nCalculating minutes from input data in csv file...\n')
    with open('testdata.csv', newline = '') as t:
        reader = csv.reader(t)
        for col in reader:
            if col[0] == 'Hours':
                min1 = 60 * int(col[1])
                min2 = 60 * int(col[2])
                min3 = 60 * int(col[3])
    print('\nMinutes =\n', min1,',', min2,',', min3)

    csvMin = ['Minutes =', min1, min2, min3]
    w = open('C2_output.csv', 'w')
    writer = csv.writer(w)
    writer.writerow(csvMin)
    w.close()

def Mins2Secs():
    print('\n#### Minutes to Seconds Convertor ####\n')
    mins = int(input('Enter the number of minutes: '))
    if mins < 0:
        print('Invalid number of minutes')
    else:
        print('\nConverting Minutess to Seconds....\n')
        secs = 60 * mins
        print('\nSeconds =\n', secs)

    print('\nCalculating seconds from input data in csv file...\n')
    with open('testdata.csv', newline = '') as t:
        reader = csv.reader(t)
        for col in reader:
            if col[0] == 'Minutes':
                sec1 = 60 * int(col[1])
                sec2 = 60 * int(col[2])
                sec3 = 60 * int(col[3])
    print('\nSeconds =\n', sec1,',', sec2,',', sec3)
    
    csvSec = ['Seconds =', sec1, sec2, sec3]
    w = open('C2_output.csv', 'w')
    writer = csv.writer(w)
    writer.writerow(csvSec)
    w.close()

def Mins2Hours():
    print('\n#### Minutes to Hours Convertor ####\n')
    mins = int(input('Enter the number of minutes: '))
    if mins < 0:
        print('Invalid number of minutes')
    else:
        print('\nConverting Minutess to Hours....\n')
        hours = mins/60
        print('\nHours =\n', hours)

    print('\nCalculating hours from input data in csv file...\n')
    with open('testdata.csv', newline = '') as t:
        reader = csv.reader(t)
        for col in reader:
            if col[0] == 'Minutes2':
                hour1 = int(col[1])/60
                hour2 = int(col[2])/60
                hour3 = int(col[3])/60
    print('\nHours` =\n', hour1,',', hour2,',', hour3)
    
    csvHour = ['Minutes =', hour1, hour2, hour3]
    w = open('C2_output.csv', 'w')
    writer = csv.writer(w)
    writer.writerow(csvHour)
    w.close()

def Secs2Mins():
    print('\n#### Seconds to Minutes Convertor ####\n')
    secs = int(input('Enter the number of seconds: '))
    if secs < 0:
        print('Invalid number of seconds')
    else:
        print('\nConverting Seconds to Minutes....\n')
        mins = secs/60
        print('\nMinutes =\n',mins)

    print('\nCalculating minutes from input data in csv file...\n')
    with open('testdata.csv', newline = '') as t:
        reader = csv.reader(t)
        for col in reader:
            if col[0] == 'Seconds':
                min1 = int(col[1])/60
                min2 = int(col[2])/60
                min3 = int(col[3])/60
    print('\nMinutes =\n', min1,',', min2,',', min3)
    
    csvMin = ['Minutes =', min1, min2, min3]
    w = open('C2_output.csv', 'w')
    writer = csv.writer(w)
    writer.writerow(csvMin)
    w.close()

def TimeConverter():
    print('\n#### Time Converter ####\n')
    convertchoice = input('Choose your Converter: (H)ours2Mins, (M)ins2Secs, M(i)ins2Hours, (S)ecs2Mins ')
    if convertchoice.upper == 'H':
        print('\n#### Hours to Minutes Convertor ####\n')
        hours = int(input('Enter the number of hours: '))
        print('\nConverting Hours to Minutes....\n')
        mins = 60 * hours
        print(mins)
    elif convertchoice.upper == 'M':
        print('\n#### Minutes to Seconds Convertor ####\n')
        mins = int(input('Enter the number of minutes: '))
        print('\nConverting Minutess to Seconds....\n')
        secs = 60 * mins
        print(secs)
    elif convertchoice.upper == 'I':
        print('\n#### Minutes to Hours Convertor ####\n')
        mins = int(input('Enter the number of minutes: '))
        print('\nConverting Minutess to Hours....\n')
        hours = mins/60
        print(hours)
    elif convertchoice.upper == 'S':
        print('\n#### Seconds to Minutes Convertor ####\n')
        secs = int(input('Enter the number of seconds: '))
        print('\nConverting Seconds to Minutes....\n')
        mins = secs/60
        print(mins)
    else:
        print('\nInvalid Input\n')
        print('Please Try again')


def main():
    Hours2Mins()
    Mins2Secs()
    Mins2Hours()
    Secs2Mins()
    TimeConverter()

if __name__ == '__main__':
    main()
