'''
#q1

a=(input("Enter a number "))
print(a[:-1])
'''
#q2
'''
print(a[-1:])
'''
#q3
'''
a=25
b=27
print("Before swapping the value of a and b is respectively :")
print(a,b)
temp=a
a=b
b=temp
print("after swapping the value of a and b is :")
print(a,b)
'''
#q4
'''
x=int(input("Enter the value of x "))
y=int(input("Enter the value of y "))
print(pow(x,y))
'''
#q5
'''
a=int(input("Enter a three digit  number "))
print((a//100))

'''
#q6
'''
a=int(input("Enter a three digit  number "))
print((a%100)//10)
'''
#q7
'''
a=int(input("Enter a three digit  number "))
print((a%10))
'''
#q8
'''
l=["shubham",20,"Btech","amazon"]
s="amazon"
if s in l:
        print(f'{s} is in the list ')
else:
    print(f'{s} is not in the list')
'''
#q9
'''
l=["shubham",20,"Btech","amazon"]
s="microsoft"
if s in l:
        print(f'{s} is  not in the list ')
else:
    print(f'{s} is  in the list')
    '''
#q10
'''
a=100
b=200
print(a is b )
'''