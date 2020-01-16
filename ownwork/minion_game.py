
string="BANANA"

cf1=0
cf2=0
# for i in range(len(string)):
#     if string[i] in "AEIOU":
#         cf1+=(len(string)-i)
#     else:
#         cf2+=(len(string)-i)

# if cf1 > cf2:
#     print("Kevin", cf1)
# elif cf1 < cf2:
#     print("Stuart", cf2)
# else:
#     print("Draw")
    
for i in range(len(string)):
    for j in range(len(string)+1):
        if (string[i:j].startswith(('A','I','O','U','E'))):
            cf1+=1
        elif string[i:j]!="":
            cf2+=1


#print("Kevin"+str(cf1) if cf1>cf2 else "Stuart",cf2)    


print("Kevin"+str(cf1) if cf1>cf2 else "Stuart",cf2)    

# vowels = 'AEIOU'
# s="BANANA"
# kevsc = 0
# stusc = 0
# for i in range(len(s)):
#     if s[i] in vowels:
#         kevsc += (len(s)-i)
#     else:
#         stusc += (len(s)-i)
