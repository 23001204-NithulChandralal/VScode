def addlist(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    result = []

    if len1 > len2:
        max_len = len1
    else:
        max_len = len2

    for i in range(max_len):
        if i < len1 and i < len2:
            result.append(list1[i] + list2[i])
        elif i < len1:
            result.append(list1[i])
        else:
            result.append(list2[i])
        return result

list1=[]
list2=[]
len1=int(input("enter a number:"))

while len1!=-1:
    list1.append(len1)
    len1=int(input("enter a number:"))
    len2=int(input("enter a number:"))

while len2!=-1:
    list2.append(len2)
    len2=int(input("enter a number:"))
ans= addlist(list1,list2)
print(ans)