# Student:Coco
# Assistant:Peter
# Score:97
# Time:2020.2.7
# Pay more attention to what happened in the computer hardware when running your code can help you gain more glimpse into it.
# Palindrome numbers test （bug existing version）
num = []
n = int(input('(with stack)input the number you wanna test:'))
m = n % 10
while m != n:
    num.append(m)
    n = (n - m)/10
    m = int(n % 10)
else:
        num.append(m)
print("res1",num)
num_check = num
print(num_check)
num_final = []
while num != []:
    num_final.append(num.pop())

if num_check == num_final:
    print("Terrific!This is a palindrome number!")
else:
    print("Sorry,this is not a palindrome number!")
print(num_final)

# Palindrome numbers test (modification version)
def numlist(n):
    num = []
    m = n % 10
    while m != n:
        num.append(m)
        n = (n - m) / 10
        m = int(n % 10)
    else:
        num.append(m)
    return num
num = numlist(int(input("the number you wanna test is:")))
num_check = num[:] #or list[] or import copy →“=” means the congruent relationship between the two list even when the list“num” changes
print(num_check)
num_final = []
while num != []:
    num_final.append(num.pop())



# p.s. without stack:
a = list(input('(without stack)input the number you wanna test:'))
if a == a[::-1]:
    print("true")
else:
    print("false")

