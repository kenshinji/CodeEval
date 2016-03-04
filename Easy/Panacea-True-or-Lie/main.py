import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    params = test.strip().split('|')
    hexs = params[0].strip().split()
    bins = params[1].strip().split()
    sum_h = 0
    sum_b = 0
    for h in hexs:
        sum_h = int(h,16) + sum_h
    for b in bins:
        sum_b = int(b,2) + sum_b
    if(sum_b >= sum_h):
        print 'True'
    else:
        print 'False'
test_cases.close()

