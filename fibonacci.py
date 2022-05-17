n=int(input("Enter the number of terms required "))
a=0
b=1
count=0
if n<=0:
    print("Enter a positive value")
elif n==1:
    print("The required fibanocci series is")
    print(a)
else:
    print("The required fibanocci series is")
    while count < n:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1

