from itertools import groupby

try:
    
    inputString = str(int(input('Enter input: ')))
    outputString = ''

    for k, g in groupby(inputString):
        group = list(g)
        outputString += '(' + str(len(group)) + ', ' + group[0] + ')'

    print(outputString)

except Exception as e:

    print(e)
    print('Are you sure you entered an integer value?')