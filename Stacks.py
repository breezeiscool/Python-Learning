# Palindrome numbers test
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



# p.s. without stack:
a = list(input('(without stack)input the number you wanna test:'))
if a == a[::-1]:
    print("true")
else:
    print("false")

