a=[100,90,80,70,60,50,87]

for item in range(0,len(a)):
    for item1 in range(item+1,len(a)):
        if(a[item]>a[item1]):
            temp=a[item];
            a[item]=a[item1]
            a[item1]=temp

print(a);

# total=0
'''
for item in range(0,len(a)):
    print(a[item])


for key,item in enumerate(a):
    print(key,item);
'''
#print(total/len(a))