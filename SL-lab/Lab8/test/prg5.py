def OddRange(num1,num2):
    odd = []
    for i in range(num1+1,num2):
        if i%2 != 0:
            odd.append(i)
    return odd
print(OddRange(1,7))
