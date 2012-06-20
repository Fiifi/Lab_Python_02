#Q5


theInput = input("Enter an integer: ")
#Your code here

if theInput%2==0:
   print 'Even'
else:
   print 'Odd'    

print '----------------------------------'

#Q6

primarySchoolAge = 4
legalVotingAge = 18
agePresident = 40
offRetirementAge = 60
personsAge = input("Enter an age: ")

if personsAge < 4:
   print 'too young'
elif personsAge >17:
   print 'Remember to vote'
   if personsAge >= 40:
      if personsAge >60:
        print "You can'tbe president"
        print 'Too old'
      else :
        print 'vote for me'
        
print '----------------------------------'

#Q7

i = 40
while i>0:
    i-=1
    if i%3==0:
        print i
        
print '----------------------------------'


#Q8

for i in range(7,30):
    if i%2!=0 and i%3!=0 and i%5!=0:
        print i

print '----------------------------------'

#Q9
n=1
while n>0:
    n+=1
    if 79*n%97==1:
        print n
        if n%2==0:
            break
