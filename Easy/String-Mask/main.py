import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    prt = ""
    params = test.strip().split()

    for i in range(0,len(params[1])):
        if(params[1][i] == '1'):
            prt = prt + params[0][i].upper()
        else:
            prt = prt + params[0][i]
    print prt



test_cases.close()