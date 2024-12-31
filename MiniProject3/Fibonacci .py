'''Start the loop to get the Fibonacci numbers for the user’s input.
Print the number of every loop.
F(n)=F(n-1)+F(n-2)
a,b,a+b,a+2b,2a+3b,3a+5b,5a+8b

'''
fibonacci=int(input("Enter the number: "))
a=0
b=1
for i in range(fibonacci):
    print(a)
    a=b
    b=a+b
