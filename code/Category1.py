#
# Category1.py - code for category 1
#
from string import digits

# Converting a given string to uppercase or lowercase

def CaseConverter():
    print('\n#### Text Case Converters ####\n')

    ## Opening file and reading first line
    testdata = open('testdata.txt')
    readData = testdata.readlines()

    # User chooses their converter
    convertchoice = input('Choose your convertor: Text2(L)ower or Text2(H)igher: ')
    if convertchoice.upper() == 'L':
# User inputs their text
        print('Enter your text')
        textstring = input()
        print(textstring.lower())

# Output readline
        print('\nReading test data from txt file...\n')
        print('Test data output = ', readData[0].lower(), 'and', readData[1].lower())

# Write output to file
        with open('C1_outputs.txt', 'a') as out:
            print(textstring.lower(), file = out)
            print('Test data output = ', readData[0].lower(), 'and', readData[1].lower(), file = out)

    elif convertchoice.upper() == 'H':
        print('Enter your text')
        textstring = input()
        print(textstring.upper())
        print('\nReading test data from txt file...\n')
        print('Test data output = ', readData[0].upper(), 'and', readData[1].upper())

        with open('C1_outputs.txt', 'a') as out:
            print(textstring.upper(), file = out)
            print('Test data output = ', readData[0].upper(), 'and', readData[1].upper(), file = out)
    else:
        print('Invalid Selection')
    testdata.close()

# Identify whether numeric values are in a given string

def NumericIdentifier():
    print('\n#### Numeric Identifier ####\n')
    testdata = open('testdata.txt')
    readData = testdata.readlines()
    numerics = []
    testNumerics = []
    textstring = input('Enter your text: ')
    for num in textstring:
        if num.isdigit():
            numerics.append(num)
    if not numerics:
        print('There are no numerics in your text')
    else:
        with open('C1_outputs.txt', 'a') as out:
            print('Numerics Identified:', numerics, file = out)
        print('Numerics Identified:', numerics)

    print('\nReading test data from txt file...\n')
    extractedData = readData[2]
    for no in extractedData:
        if no.isdigit():
            testNumerics.append(no)
    if not testNumerics:
        print('There are no numerics in the test data text')
    else:
        with open('C1_outputs.txt', 'a') as out:
            print('Numerics Identified:', testNumerics, file = out)
        print('Numerics Identified:', testNumerics)
    testdata.close()

# Identify whether a given string is a valid number or not

def NumericValidator():
    print('\n#### Numeric Validator ####\n')
    testdata = open('testdata.txt')
    readData = testdata.readlines()
    print('Enter a number from 0-10')
    number = int(input())
    if 0 > number < 10:
            number == False
            with open('C1_outputs.txt', 'a') as out:
                print('Invalid Number:', number, file = out)
            print('Invalid Number')
    else:
        number == True
        with open('C1_outputs.txt', 'a') as out:
            print('Your number:', number, 'is a valid number', file = out)
        print('Your number', number, 'is a valid number')

    print('\nReading testdata from txt file...\n')
    numberdata = int(readData[3])
    if 0 > numberdata < 10:
            numberdata == False
            with open('C1_outputs.txt', 'a') as out:
                print('Your number:', numberdata, 'is a valid number', file = out)
            print('Invalid Number')
    else:
        numberdata == True
        with open('C1_outputs.txt', 'a') as out:
            print('Your number:', numberdata, 'is a valid number', file = out)
        print('The number', numberdata, 'is a valid number')
    testdata.close()

# Remove any numeric values in a given string then convert the string to upper or lowercase

def NumericRemover():
    print('\n#### Numeric Remover ####\n')
    testdata = open('testdata.txt')
    readData = testdata.readlines()
    textstring = input('Enter your text: ')
    extractedData = readData[4]

    no_num = str.maketrans('', '', digits)
    no_num_textstring = textstring.translate(no_num)
    no_num_exD = extractedData.translate(no_num)

    convertchoice = input('Choose your converter: Text2(L)ower or Text2(H)igher ')
    if convertchoice.upper() == 'H':
        print('\n',no_num_textstring.upper(),'\n')
        print('\nReading test data from txt file...\n')
        print('testdata output =', no_num_exD.upper())
        with open('C1_outputs.txt', 'a') as out:
            print(no_num_textstring.upper(), file = out)
            print('testdata output =', no_num_exD.upper(), file = out)

    elif convertchoice.upper() == 'L':
        print('\n',no_num_textstring.lower(),'\n')
        print('\nReading test data from txt file...\n')
        print('testdata output =', no_num_exD.lower())
        with open('C1_outputs.txt', 'a') as out:
            print(no_num_textstring.lower(), file = out)
            print('testdata output =', no_num_exD.lower(), file = out)

    else:
        print('Invalid Selection')

CaseConverter()
NumericIdentifier()
NumericValidator()
NumericRemover()


