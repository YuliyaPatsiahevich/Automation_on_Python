def numb(a):
    return a % 2 == 0
result = filter (numb,[-2,-3,0,1,-1,2,4])
print (list(result))