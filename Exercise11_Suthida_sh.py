number = int(input("Select Number :"))
for j in range(number):
    result = " "*(number-1)+("*"*(j*2+1))
    number -= 1
    print(result)
