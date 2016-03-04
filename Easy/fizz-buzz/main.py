import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    prt = ""
    test = test.strip().split()

    for i in range(1, int(test[2])+1):
        if(i % int(test[0]) == 0 and i % int(test[1]) != 0):
            prt = prt + "F "
        elif i % int(test[0]) != 0 and i % int(test[1]) == 0:
            prt = prt + "B "
        elif i % int(test[0]) == 0 and i % int(test[1]) == 0:
            prt = prt + "FB "
        else:
            prt = prt + str(i) + " "
    print prt
test_cases.close()
