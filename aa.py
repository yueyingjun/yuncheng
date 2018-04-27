# 99乘法表
#  100-200   3...1     4....2    5....3
#  鸡兔同笼  35头  94只脚
#  杨辉三角
'''
for num in range(100,201):
    if num%3==1 and num%4==2 and num%5==3:
        print(num);


head=35
foot=94
for ji in range(1,36):
    tu=35-ji
    if ji*2+tu*4==94:
        print(ji,tu)







rows=21

for row in range(1,rows):
    str=""
    for space in range(1,rows-row):
        str+=" "
    for star in range(1,row*2-1+1):
        str+="*"
    print(str)
'''

rows = 10
for row in range(1, rows):
    space = ""
    for col in range(1, row + 1):
        if (col == 2 and row == 3) or (col == 2 and row == 4):
            space = "  "
        else:
            space = " "
        print("%s*%s=%s" % (col, row, row * col), end=space)
    print("")
