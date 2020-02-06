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
# def fibs(n):
#     list =[]
#


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

# # extra check(failed 5555555555555555555)
# if a == fibs[t]:
#     print("After inspection,the output is precisely meet your need!")
# else:
#     print("hmm,the answer didn't match successfully.It seems to have sth wrong with my algorithm...")

"""method 3 : recursion"""

def fibs(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibs(n-1) + fibs(n-2)
result = fibs(int(input("Q3:input the rank you want:")))
print(result)






