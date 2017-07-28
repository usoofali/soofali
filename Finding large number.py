print("PROGRAM FOR FINDING THE LARGEST AMONG THREE NUMBERS")
print("Please enter the numbers")
a=int(input("First Number:"))
b=int(input("Second Number:"))
c=int(input("Third Number:"))
if a > b and a > c:
    print("The largest number is",a)
elif c > a:
        print("The largest number is",c)
elif b > a:
    print("The largest number is",b)
else:
    print("No answer")
input("\n\nPress enter key to exit")
