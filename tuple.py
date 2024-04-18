#a=(10,"hari",20.5,'h')
#b=(10,"hari",20.5,'h')
c=(10,25,30,45,5,60)
'''print(a)

print(a[1])
print(a[:-1])
print(a[3])
print(a==b)
print(len(a))
print(max(c))
print(min(c))

d=a+c
print(d)

for i in a:
    if i not in c:
        c.append(i)
print(c)

sum=0
for i in c:
    sum+=i
print(sum)'''

for i in c:
    if i%10==5:
        print(i)