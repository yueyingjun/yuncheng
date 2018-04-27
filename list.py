def order(a,type=1):
    for item in range(0,len(a)):
        for item1 in range(item+1,len(a)):
            if type==1:
                if(a[item]>a[item1]):
                    temp=a[item];
                    a[item]=a[item1]
                    a[item1]=temp
            elif type==2:
                if (a[item] < a[item1]):
                    temp = a[item];
                    a[item] = a[item1]
                    a[item1] = temp
    return a;


