x = -123
x = 0
x = -2**31+1
x_rev = int(str(abs(x))[::-1])
print(x_rev)
x_rev = x_rev if x > 0 else (-1)*x_rev
print(x_rev)
if -2**31 <= x_rev <= 2**31-1:
    print(x_rev)
    # return x_rev
else:
    print(0)
    # return 0