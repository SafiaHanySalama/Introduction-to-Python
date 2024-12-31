'''Start the loop to get the Fibonacci numbers for the user’s input.
Print the number of every loop.
F(n)=F(n-1)+F(n-2)
a,b,a+b,a+2b,2a+3b,3a+5b,5a+8b

'''
num=int(input("Enter the number: "))
try:
    if(num>0):
        #the size of the list is the number of fibonacci numbers the user wants
        fibonacci=[0]*num
        fibonacci[0]=0
        print(fibonacci[0])
        fibonacci[1]=1
        print(fibonacci[1])
        for i in range(2,num):
            #the next number is the sum of the previous two numbers
            fibonacci[i]=fibonacci[i-1]+fibonacci[i-2]
            print(fibonacci[i])
except ValueError:
    print("Please enter a positive number")