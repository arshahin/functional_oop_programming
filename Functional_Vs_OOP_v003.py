
####################################### OOP Culture ##################################################### 

class experts():
    def __init__ (self,name,company,discipline,position,math_of_interest):
        self.name=name
        self.company=company
        self.discipline=discipline
        self.position=position
        self.math_of_interest=math_of_interest
#############Check to see whether or not an integer is a prime number############ 
    def check_prime(self,n):
        self.n=n
        for i in range(2, n):
            if (n % i) == 0:
                return True
        return False
######################## Calculate the factorial of an integer number
    def factorial_calc(self,n):
        self.n=n
        f=1
        for i in range(1,n+1):
            f *= i
        return f
######################## Calculate the Fibonacci Series of an integer number
    def fibonacci_calc(self,n):
        self.n=n
        fseries=[0,1]
        if n>2:
            for j in range(2,n):
                fnext=fseries[j-1]+fseries[j-2]
                fseries.append(fnext)
        return fseries
######################## Print function     
    def printData(self):
        print("Name:\t",self.name)
        print("Company:\t",self.company)
        print("Discipline:\t",self.discipline)
        print("Position:\t",self.position)
        print("Math of interest:\t",self.math_of_interest)
        return
################################################ OOP solution is started 
print("********** OOP solution started**********\n\n")
expert=None
nexpert = input("Enter 1 for expert1, 2 for expert2, and 3 for expert3: ")
nexpert = int(nexpert) if nexpert.isnumeric() else -1

num = input("Enter an integer number between 2 to 10: ")
num=int(num) if num.isnumeric() else -1
if (num<2 or num>10):
    print("INVALID NUMBER")
else:
    if nexpert==1:
        expert=experts(name='Alex',company='APG',discipline='Digital Security',position='Manager',math_of_interest='Prime')
        print("Here is the information about expert you selected:")
        expert.printData()
        print("\n\nResults of your query are")
        print("The number "+str(num)+" is not prime." if expert.check_prime(num)==True else "The number "+str(num)+" is prime.")
    elif nexpert==2:
        expert=experts(name='Mark',company='APG',discipline='Data Scientist',position='Principal',math_of_interest='Factorial')
        print("Here is the information about expert you selected:")
        expert.printData()
        print("\n\nResults of your query are")
        print("The factorial of",num,"is",expert.factorial_calc(num),'.')
    elif nexpert==3:
        expert=experts(name='Richard',company='CCOP',discipline='Data Engineer',position='CEO',math_of_interest='Fibonacci')
        print("Here is the information about expert you selected:")
        expert.printData()
        print("\n\nResults of your query are")
        print("The first", num, "numbers of the Fibonacci series are",expert.fibonacci_calc(num),'.')
    else:
        print("INVALID EXPERT OPTION SELECTED")

print("\n\n********** OOP solution ended**********")
##### Print the outputs



#########################################Functional culture################################################# 

#############Create tuples of experts############ 
def expert_func(nexpert):
    expert1=('Alex','APG','Digital Security','Manager','Prime')
    expert2=('Mark','APG','Data Scientist','Principal','Factorial')
    expert3=('Richard','CCOP','Data Engineer','CEO','Fibonacci')
    experts=(expert1,expert2,expert3)
    return experts[nexpert-1]  
#############Print Details of expert############ 
def printExpertDetails(nexpert):
    details=expert_func(nexpert)
    print("\nHere is the information about expert you selected:")
    print("Name:\t",details[0])
    print("Company:\t",details[1])
    print("Discipline:\t",details[2])
    print("Position:\t",details[3])
    print("Math of interest:\t",details[4])
    print("\n")
#############Check to see whether or not an integer is a prime number############ 
def prime_func(n, d=2):
    if n ==2 or d>=n:
        return False
    else:
        return( True if n%d == 0 else prime_func(n, d + 1))
    
###is_prime = lambda n: n > 1 and all(n % i for i in range(2, n))

    
#############Calculate factorial of given number############ 
def factorial_func(n ):
    if n<=1:
        return n
    else:
        return( n*factorial_func(n-1))
    
###factorial_calc = lambda n: 1 if n == 0 else n * factorial_calc(n - 1)

#############Calculate Fibonacci of given number############   
def fibonocci_func(n,count=0, last1=0,last2=1):
    #print(count)
    if count>=n:
        return 
    else:
        count=count+1
        print(last1, end=' ')
        last=last1+last2
        last1=last2
        last2=last
        return fibonocci_func(n,count,last1,last2)
    
    
### fibonocci_func = lambda n: 0 if n == 0 else 1 if n == 1 else fibonocci_func(n - 1) + fibonocci_func(n - 2)
###fibonacci_series = lambda n: [fibonocci_func(i) for i in range(n)]


#############Accepts input from user############       
def input_func():
    nexpert = input("Enter 1 for expert1, 2 for expert2, and 3 for expert3: ")
    nexpert=int(nexpert) if nexpert.isnumeric() else -1
    #print(nexpert)
    num = input("Enter an integer number between 2 to 10: ")
    num=int(num) if num.isnumeric() else -1
    if (nexpert <1 or nexpert >3) or (num<2 or num>10) :
        return (-1,-1) 
    return (nexpert,num)

#############call functions based on input############       
def call_func(nexpert,num):
    printExpertDetails(nexpert)
    print("Results of your query are")
    if nexpert==1:
        print("The number "+str(num)+" is not prime." if prime_func(num)==True else "The number "+str(num)+" is prime.")
    if nexpert==2:
        print("The factorial of",num,"is",factorial_func(num),'.')
    if nexpert==3:
        print("The first "+ str(num) + " numbers of the Fibonacci series are: ",end = '')
        fibonocci_func(num)

        
print("\n\n********** Functional solution started**********\n")
nexpert,num=input_func()
print("INVALID INPUT SELECTED") if (nexpert==-1 or num==-1) else call_func(nexpert,num)

print("\n\n********** Functional solution ended**********")