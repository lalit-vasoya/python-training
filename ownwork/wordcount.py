# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

tns,inf=int(input()),input().split()
t=namedtuple("student",inf)

std=[t(*input().split()) for i in range(tns)]

a=sum([int(i[1]) for i in std])
b=a/len(std)
# print(b)
print("{0:.2f}".format(int(b)))



# -----------------------------------
# # a="ABCDCDC"
# # b="CDC"

# # ind=0
# # count=0
# # for i in range(len(a)):
# #     if a[i]==b[ind] and a[i:i+len(b)]==b:
# #         count+=1
        

# # print(count)

# # Enter your code here. Read input from STDIN. Print output to STD
# a=input()
# u=""
# l=""
# o=""
# e=""

# for i in a:
#     if i.isupper():
#         u+=i
#     if i.islower():
#         l+=i
#     if i.isdigit():
#         if int(i)%2==0:
#             e+=i
#         else:
#             o+=i


# print(sorted(l)+sorted(u)+sorted(o)+sorted(e))