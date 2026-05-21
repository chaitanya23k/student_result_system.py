# Assignment — Student Result System

user = input("What is student name? ")

student = {
    'Maths': int(input("Enter maths marks: ")),
    'science': int(input("Enter science marks: ")),
    'English' : int(input("Enter English marks: "))
    }

total = student['Maths'] + student['science'] + student['English']
average = total/3

if total > 80:
    print(f'{user} got A grade :)')
elif total > 70 :
    print(f'{user} got B grade :)')
elif total > 40:
    print(f'{user} got c grade :(')
else:
    print(f'{user} got failed. Re-write the exam again')
        
        
print('Total: ', total)        
    