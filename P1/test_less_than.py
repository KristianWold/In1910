from less_than import less_than

a = [1,2,3,4,5,6,7,8,9,10]
n = 5
expected = [1,2,3,4]

if less_than(a,n) == expected:
    print("passed")
else:
    print("failed")
