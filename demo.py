x=int(input("Enter the last digit :"))
def fib(n):
    a=0
    b=1
    if n<1:
        print("Invalid")
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            if c>100:
                break
            print(c)
fib(x)
