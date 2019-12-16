Windows executable File of Python 	=> 	C:\Python35\python.exe
Python Program File 				=> 	$cat file.py 		#prints the contents of the file
										$python file.py 	#executes the python script

>>>help()											#interactive help system
>>>help(module)

>>>import library_name								#import a library
>>>dir(library_name)								#method and contents of that library or module

>>>print('Hello World!')							#printing a statement
>>>print('STRING',VARIABLE)
>>>print('STRING'+VARIABLE+'STRING')

>>>var = input('Statement\n')						#taking input into a variable

>>>type(10)
<class 'int'>

>>>type('hello')
<class 'str'>
>>>type(14.5)
<class 'float'>
>>>type('10')
<class 'str'>


# CONDITIONAL STATEMENTS

if condition:
	statement

if condition:
	statement1
else:
	statement2

if condition1:
	statement1
elif condition2:
	statement2
else:
	statement3




# LOOPING STATEMENTS

>>>while condition:
...		repetive_statements
...		repetive_statements2
>>>outsideloop

>>>for x in xrange(1,10):
...		statement1
>>>	

>>>list1=[1,2,3,4,5]
>>>for listvar in list1:
...		statement1
...		statement2
>>>statement3

#Defining a Class and Creating a Object

>>>class inputOutputValue(object):
>>>		def __init__(self):
>>>			self.s = ""
>>>		def getValue(self):
>>>			self.s = input()
>>>		def printValue(self):
>>>			print(s)
>>>
>>>sampleObj = inputOutputValue()
>>>sampleObj.getValue()
>>>sampleObj.printValue()

# TRY AND EXCEPT BLOCK

try:
	statement1
	statement2
	statement3
except:
	print('Error')


# BUILT-IN FUNCTIONS

>>>max('STRING')					#max value in the list	T 
>>>min('STRING')					#min value in the list	G
>>>len('STRING')					#lenght of the list		6
>>>sum()

>>>int('12')						#type conversion functions
>>>float('12')
>>>str('12')

>>>import math
>>>math.log10(var)
>>>math.sin(radians)
>>>math.cos(radians)
>>>math.pi
>>>math.sqrt(value)

>>>import random
>>>random.random()					#number between 0.0 and 1.0
>>>random.randint(low,high)
>>>random.choice(t)					#t=[1, 2, 3]

# DEFINING USER FUNCTIONS

>>>def function(parameters):
...		statement1
...		statement2
...		return value
>>>
>>>value=function(arguments)

# STRINGS

>>>var='STRING'
>>>var[2]							#R
>>>len(var)							#6
>>>var[-2]							#N
>>>var[1:4]							#TRI
>>>var[3:]							#ING
>>>var[:3]							#STR
>>>var[:]							#STRING

>>>T in var 						#TRUE
>>>TRI in var 						#TRUE
>>>TIR in var 						#FALSE

>>>'APPLE'>'BANANA'					#FALSE
>>>'CUCUMBER'<'BANANA'				#FALSE
>>>'APPLE'=='CUCUMBER'				#FALSE
>>>'BANANA'=='banana'				#FALSE
>>>'BANANA'<'banana'				#TRUE

>>>var.upper()						
>>>var.find('a')					#returns index if found else -1
>>>var.find('abcd')					
>>>var.find('a',start_index)		
>>>var.strip()						#removes multiple white spaces and tab spaces
>>>var.rstrip()						#removes white space from right end
>>>var.startswith('abc')			
>>>var.lower()
>>>var.replace('old','new','count')	#count in optional by default it replaces all occurences						
#NOTE: u can apply multiple nethods: >>>var.lower().startswith('a')

>>>'In %g years I have spotted %d %s.' % (3.5, 14, 'camels')		#formating data into string

>>>import string
>>>string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


#Convert LIST to STRING
>>>str1=""
>>>for i in list1:
...		str1=str1+i
>>>print(str1)


# DATASTRUCTURES

## LISTS

>>>list1=['STRING',24,45.67,['ANOTHER LIST',100],var]		#set of value of any datatype

>>>list2=[10,20,35,40,50]
>>>list2[2]=30
>>>print(list2)
[10,20,30,40,50]

>>>40 in list2
True
>>>35 in list2
False

>>>a=[1,2]
>>>b=[3,4,5,6]
>>>print(a+b)
[1,2,3,4,5,6]

>>>print(a*3)
[1,2,1,2,1,2]

>>>b[:2]							#[3,4]
>>>b[2:]							#[5,6]
>>>b[1:2]=[1,2]						#[3,1,2,6]

>>>b.append(7)
>>>b.extend(anotherlist)
>>>b.sort()
>>>b.sort(reverse=True)
>>>b.pop(index)
>>>del b[index]
>>>b.remove(element)

>>>len(list1)
>>>max(list1)
>>>min(list1)
>>>sum(list1)

>>>s="random sentence"
>>>l=s.split()
>>>print(l)
['random','sentence']

>>>t=list(l[1])
>>>print(t)
['r','a','n','d','o','m']

>>>s='a-b-c-d-e'
>>>s.split('-')
['a','b','c','d','e']



## DICTIONARY
>>>dict1={'one':1,'two':2,'three':3}					#set of key-value pairs
>>>dict1['four']=4

>>>dict1['two']
2
>>>len(dict1)
4
>>>vals=list(dict1.values())
[1,2,3,4]
>>>dict1.get(two,0)
2
>>>dict1.get(five,0)
0

>>>for key in dict1:
...		print(key,dict1[key])
one 1
two 2
three 3
four 4

>>>l=list(dict1.items())
>>>print(l)
[('one',1),('two',2),('three',3),('four',4)]			#dictionary as a list of tuples



## TUPLES
>>>t='a','b','c','d'									#set of value of same datatype
>>>t=tuple('string')
('s','t','r','i','n','g')

>>>t[0]
s
>>>t[1:3]
('t','r')

>>>m=['1','2']
>>>x,y=m
>>>print(x)
1
>>>print(y)
2

>>>a,b=b,a 				# swap

## REGULAR EXPRESSIONS
>>>import re

>>>line='random long sentence to search for regular expressions'
>>>re.search('long',line)
True

>>>re.findall('s.+',line)
['sentence','search']

## CHARACTER SEQUENCES

ˆ 			Matches the beginning of the line.
$ 			Matches the end of the line.
. 			Matches any character.
\s 			Matches a whitespace character.
\S 			Matches a non-whitespace character.
* 			Applies to the immediately preceding character(s) and indicates to match zero or more times.
*? 			Applies to the immediately preceding character(s) and indicates to match zero or more times in “non-greedy mode”.
+ 			Applies to the immediately preceding character(s) and indicates to match one or more times.
+? 			Applies to the immediately preceding character(s) and indicates to match one or more times in “non-greedy mode”.
? 			Applies to the immediately preceding character(s) and indicates to match zero or one time.
?? 			Applies to the immediately preceding character(s) and indicates to match zero or one time in “non-greedy mode”.
[aeiou] 	Matches a single character as long as that character is in the speciﬁed set. In this example, it would match “a”, “e”, “i”, “o”, or “u”, but no other characters.
[a-z0-9] 	You can specify ranges of characters using the minus sign. This example is a single character that must be a lowercase letter or a digit.
[ˆA-Za-z] 	When the ﬁrst character in the set notation is a caret, it inverts the logic. This example matches a single character that is anything other than an uppercase or lowercase letter.
( ) 		When parentheses are added to a regular expression, they are ignored for the purpose of matching, but allow you to extract a particular subset of the matched string rather than the whole string when using findall().
\b 			Matches the empty string, but only at the start or end of a word.
\B 			Matches the empty string, but not at the start or end of a word.
\d 			Matches any decimal digit; equivalent to the set [0-9].
\D 			Matches any non-digit character; equivalent to the set [ˆ0-9].


# FILE HANDLING

>>>filehandler=open('file.txt')
>>>filevar=filehandler.read()

>>>fname='file.txt'
>>>try:
...		fhand=open(fname)
>>>except:
...		print('File '+fname+' cannot be opened')
...		exit()
>>>


>>>fout=open('file.txt', 'w')

>>>line='some random string to insert in file\n'
>>>fout.write(line)
37

>>>fout.close()




#NETWORK PROGRAMMING

>>>import socket
>>>mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>>mysock.connect(('data.pr4e.org', 80))
>>>cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()	#encode() converts request into a byte format
>>>mysock.send(cmd)
>>>while True: data = mysock.recv(512)
...		if len(data) < 1:
...			break
...		print(data.decode(),end='')										#decode() convert byte format to text
>>>mysock.close()

##RECIEVED DATA
HTTP/1.1 200 OK
Date: Wed, 11 Apr 2018 18:52:55
GMT Server: Apache/2.4.7 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22
GMT ETag: "a7-54f6609245537"
Accept-Ranges: bytes
Content-Length: 167
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain

But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief

#byte format for transfer over http
>>>b'Hello world'
b'Hello world'
>>>'Hello world'.encode()
b'Hello world'


# TIMER
>>>import time
>>>time.sleep(0.5)

# DATABASE CONNECTIONS
## Connection to a sqlite database
>>>import sqlite3

>>>conn=sqlite3.connect('database_name.sqlite')
>>>cur=conn.cursor()
>>>cur.execute('CREATE TABLE tablename (title TEXT, value INTEGER)')
>>>cur.execute('SELECT title,value FROM tablename')
>>>for row in cur:
...		print(row)
>>>cur.commit()
>>>conn.close()
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>

