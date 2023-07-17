def perfectSquareOrNot(n):
    i=1
    while(i*i<=n):
        if n/i==i:
            return True
        i+=1
    return False
print(perfectSquareOrNot(int(input())))
