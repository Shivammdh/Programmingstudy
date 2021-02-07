import datetime
print("your test date and time",datetime.datetime.now())
c=datetime.datetime.now()
print(c.strftime("%A"))


score = 0
score = int(score)

#Ask user for their name
name = input("What is your name?  ")
name = name.title()
import re
s = input("\nenter your email Address:")
s=s.title()
match = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', s, re.I)
print(match.group())
choice=int(input("enter your choice \nfor Python Press 1:\nfor C press 2:\n for C++ Press 3:"))

print("""\nHello {} mail id {} welcome to Quiz...
You will be presented with 10 questions.
Enter the appropriate number to answer the question
Good luck!""".format(name,s))
"""import time
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Blast Off!!!')
#t = input("Enter the time in seconds: ") 
t=600
countdown(int(t))"""

if(choice==1):
	print('\nQuestion1')
	print("""\nprint(''Recursive Function'') 
	def factorial(n): 
	   return(n*factorial(n-1))  
	factorial(4)
	1 - Recursive Function 24.
	
	2- Recursive Function.
	
	3 - Function runs infinitely and causes a StackOverflowError.
	
	4- Syntax Error""")
	
	answer1 = "4"
	response1 = input("Your answer is:")
	
	if (response1==answer1):
		score+=1
	else:
	    print(" ")
	
	
	print('\nQuestion2')
	print("""Which options are correct to create an empty set in Python?
	
	1- {}

	2- ()
	
	3 - []
	
	4- set()""")
	
	answer2 = "2"
	response2 = input("Your answer is:")
	
	
	if (response2==answer2):
		score+=1
	else:
	    print(" ")
	
	print('\nQuestion3')
	print("""What is the output of the following code?
	
	def f(x = 100, y = 100): 
	   return(x+y, x-y) 
	x, y = f(y = 200, x = 100) 
	print(x, y) 
	1- 300 -100
	
	2 - 200 0
	
	3 - 200 100
	
	4 - 0 300""")
	
	answer3 = "1"
	response3 = input("Your answer is:")
	
	if (response3 == answer3):
	    score+=1
	else:
	    print(" ")
	
	print('\nQuestion4')
	print("""What is the output of following code −
	
	[ (a,b) for a in range(3) for b in range(a) ]
	1 - [ (1,0),(2,1),(3,2)]
	
	2- [ (0,0),(1,1),(2,2)]
	
	3 - [(1,0),(2,1),(2,1)]
	
	3- [ (1,0),(2,0),(2,1)]""")
	
	answer4 = "3"
	response4 = input("Your answer is:")
	
	if (response4 == answer4):
	    score+=1
	else:
	    print(" ")
	
	print('\nQuestion5')
	print("""What will be the output of the following Python code?
	
	print('1Rn@'.lower())
	1-n
	2-1rn@
	3- rn
	4-r""")
	
	answer5 = "2"
	response5 = input("Your answer is:")
	
	if (response5 == answer5):
		score+=1
	else:
	    print(" ")
	
	print('\nQuestion6')
	print("""What will be the output of the following code :
	print type(type(int))
	1.type 'int'
	2.type 'type'
	3.Error
	4.0""")
	
	answer6='2'
	response6=input("your answer is")
	if (response6== answer6):
		score+=1
	else:
	    print(" ")
	
	print('\nQuestion7')
	print("""What is the output of the following code :
	L = ['a','b','c','d']
	print "".join(L)
	1.Error
	2.None
	3.abcd
	4.[‘a’,’b’,’c’,’d’]""")
	answer7='3'
	response7=input("your answer is")
	if (response7== answer7):
		score+=1
	else:
	    print(" ")
	
	print('\nQuestion 8')
	print("""What is the output of the following segment :
	chr(ord('A'))
	1.A
	2.B
	3.a
	4.Error""")
	
	answer8='1'
	response8=input("your answer is")
	if (response8== answer8):
		score+=1
	else:
	    print(" ")
	
	print('\nQuestiin9')
	print("""What is the output of the following program :
	y = 8
	z = lambda x : x * y
	print z(6)
	Run on IDE
	1.48
	2.14
	3.64
	4.None of the above""")
	answer9='1'
	response9=input("your answer is")
	if (response9== answer9):
		score+=1
	else:
	    print(" ")
	    
	print('\nQuestion10')
	print("""What is called when a function is defined inside a class?
	1-Module
	2-Class
	3-Another Function
	4-non of these.
	Method""")
	
	answer10='4'
	response10=input("your answer is")
	if (response10== answer10):
		score+=1
	else:
	    print(" ")
	
	print("Your total score is " + str(score) + " out of 10")
	print("Thank you for join {}, goodbye!".format(name))
	
		
if(choice==2):
	print('\nQuestion 1')
	print(""" Which of the following statements should be used to obtain a remainder after dividing 3.14 by 2.1 ?

1.	rem = 3.14 % 2.1;
2.	rem = modf(3.14, 2.1);
3.	rem = fmod(3.14, 2.1);
4.	Remainder cannot be obtain in floating point division.""")
	
	answer1='3'
	response1=input("your answer is")
	if (response1== answer1):
		score+=1
	else:
	    print(" ")
	print('\nQuestion 2')
	print(""" What is (void*)0?

1.	Representation of NULL pointer
2.	Representation of void pointer
3.	Error
4.	None of above.""")
	
	answer2='1'
	response2=input("your answer is")
	if (response2== answer2):
		score+=1
	else:
	    print(" ")
	
	print('\nQuestion 3')
	print(""" 	
If a variable is a pointer to a structure, then which of the following operator is used to access data members of the structure through the pointer variable?

1.	.
2.	&
3.	*
4.	->  """)
	
	answer3='4'
	response3=input("your answer is")
	if (response3== answer3):
		score+=1
	else:
	    print(" ")
	    
	print('\nQuestion 4')
	print(""" 	
A pointer is

1.	A keyword used to create variables
2.	A variable that stores address of an instruction
3.	A variable that stores address of other variable
4.	All of the above	
  """)
	
	answer4='3'
	response4=input("your answer is")
	if (response4== answer4):
		score+=1
	else:
	    print(" ")
	    
	print('\nQuestion 5')
	print("""The operator used to get value at address stored in a pointer variable is

1.	*
2.	&
3.	&&
4.	||  """)
	
	answer5='1'
	response5=input("your answer is")
	if (response5== answer5):
		score+=1
	else:
	    print(" ")
	
	print('\nQuestion 6')
	print(""" 	
The keyword used to transfer control from a function back to the calling function is

1.	switch
2.	goto
3.	go back
4.	return  """)
	
	answer6='4'
	response6=input("your answer is")
	if (response6== answer6):
		score+=1
	else:
	    print(" ")
	
	print('\nQuestion 7')
	print(""" What does the following declaration mean?
int (*ptr)[10];

1.	ptr is array of pointers to 10 integers
2.	ptr is a pointer to an array of 10 integers
3.	ptr is an array of 10 integers
4.	ptr is an pointer to array  """)
	
	answer7='2'
	response7=input("your answer is")
	if (response7== answer7):
		score+=1
	else:
	    print(" ")
	
	print('\nQuestion 8')
	print(""" 	
In C, if you pass an array as an argument to a function, what actually gets passed?

1.	Value of elements in array
2.	First element of the array
3.	Base address of the array
4.	Address of the last element of array  """)
	
	answer8='3'
	response8=input("your answer is")
	if (response8== answer8):
		score+=1
	else:
	    print(" ")
	    
	print('\nQuestion 9')
	print(""" 	Which of the following function sets first n characters of a string to a given character?

1.	strinit()
2.	strnset()
3.	strset()
4.	strcset()  """)
	
	answer9='2'
	response9=input("your answer is")
	if (response9== answer9):
		score+=1
	else:
	    print(" ")
	    
	print('\nQuestion 10')
	print(""" 	
If the two strings are identical, then strcmp() function returns

1.	-1
2.	1
3.	0
4.	Yes   """)
	
	answer10='3'
	response10=input("your answer is")
	if (response10== answer10):
		score+=1
	else:
	    print(" ")
	    
	print("Your total score is " + str(score) + " out of 10")
	print("Thank you for join {}, goodbye!".format(name))
		