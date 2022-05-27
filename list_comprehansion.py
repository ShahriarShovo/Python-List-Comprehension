# generate list between 1 to 100

n1 = [i for i in range(1,100+1)]
print(n1)
print('\n')

#Find all of the numbers from 1–1000 that are divisible by 8

n2 = [i for i in n1 if i%8==0]
print(n2)

print('\n')


#Find all of the numbers from 1–1000 that have a 6 in them
n3 = [i for i in n1 if  '6' in str(i)]
print(n3)

print('\n')

#Count the number of spaces in a string (use string above)
string= " I love Python and Django "
count= len([i for i in string if i==" "])
print(count)

print('\n')
#Remove all of the vowels in a string (use string above)

string= " I love Python and Django "
replace_vowel = "".join([i for i in string if i not in ["a", "e","i", "o","u"]])
print(replace_vowel)

print('\n')

#Find all of the words in a string that are less than 5 letters (use string above)

string= " I love Python and Django "
split = string.split()
word_count= [i for i in split if len(i)<5]
print(word_count)
print('\n')
#python program to print alphabets from a to z

var='a'
alph=[]
alph = [ (chr(ord(var)+i)) for i in range(26)]
print(alph)
print('\n')
#python program to print all even numbers from 1 to 100

even =[i for i in range(1,100+1) if i%2==0]
print(even)

print('\n')
#python program to print all odd numbers from 1 to 100

odd =[i for i in range(1,100+1) if i%2==1]
print(odd)
print('\n')

#program to find sum of natural numbers from 1 to 10

n= sum([i for i in range(1,10+1)])
print(n)































