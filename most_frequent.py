def most_frequent(str):
    d = dict()
    for key in str:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    dec_order_freq=dict(sorted(d.items(), key=lambda x: x[1] , reverse=True))
    for x, y in dec_order_freq.items():
        print(x,"=", y,end=" ")

str=input("Enter the string: ")
output=most_frequent(str)
print(output)