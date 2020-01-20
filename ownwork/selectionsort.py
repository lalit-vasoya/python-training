
arr=[12,14,22,8,1,6,0]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]

print(*arr)       

# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]

# print(*arr)

# arr.sort()
# a=int(input("Enter new Number"))
# for i in range(len(arr)):
#     if arr[i]>a:
#         arr.insert(arr.index(arr[i]),a)
#         break

# print(*arr)
    