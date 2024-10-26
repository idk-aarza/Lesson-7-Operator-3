print('enter marks obtained in 3 subjects')
mark1=int(input())
mark2=int(input())
mark3=int(input())
total=mark1+ mark2+ mark3
average=total/3
if average >= 91 and average <= 100 :
    print('Your grade is A1')
elif average >= 81 and average <= 91:
    print('Your grade is A2')
elif average >= 71 and average <= 81:
    print('Your grade is B1')
else :
    print('invalid input')