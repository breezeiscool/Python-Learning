# Student:Coco
# Assistant:Peter
# Scores:97
# P.S. Done great ! You successfully finish the assignments but three points are deducted because you didn't use an expected function.
# btw, your hard work makes me hang my head in shame.
# Precise:
# As we all know：fibs(0)=0,fibs(1)=1,
#                 fibs(n)=fibs(n-1)+fibs(n-2)

"""method 1 : using list to present the n-th number in fibs seq."""
fibs = [1, 1]
n = int(input("Q1:How many fibs numbers do you want:"))
for i in range(0, n):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs[0:n])

# Thinking:how to use the func.
'''
def fibs(n):
    list=[1,1]
    if n<=2:
        return 1
    for i in range(n):
        list.append(list[i]+list[i+1])
    return list[n-1]
print(fibs(4))

'''


"""method 2 : simple multiple work"""
c, d = 0, 1
t = int(input("Q2:In what rank of number in the fibs seq do you want to know:"))
i = 1
while i <= t:
#    print(b, end=",") # if you want the result to print in a row.
    c, d = d, c+d
    i = i+1
else:
    print(c)

# # extra check(failed 5555555555555555555) # Piggy just'cause the list fibs[]'s index start from 0....
if c == fibs[t-1]:  # decrease t by 1
    print("After inspection,the output is precisely meet your need!")
else:
    print("hmm,the answer didn't match successfully.It seems to have sth wrong with my algorithm...")

"""method 3 : recursion"""


def fibs(n):  # Pretty! it's quite a masterpiece for u since recursion is such a difficulty for a neophyte.
    if n == 1 or n == 2:
        return 1
    else:
        return fibs(n-1) + fibs(n-2)
result = fibs(int(input("Q3:input the rank you want:")))
print(result)
