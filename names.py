names="harindra"
vowels="aeiou"
result=[chr for chr in names if chr in vowels]
print(result)
print(names[::-1])
print(names[::-3])
print(names[0:-4])
for i in range(0,len(names)):
    if i%4!=0:
        print("_",end=" ")
    else:
        print(names[i],end=" ")
print()
print(names[0],names[len(names)-1])


