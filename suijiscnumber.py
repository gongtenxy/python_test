import random
mind='y'
while mind=='y':
    n=random.randrange(1,220)
    print(n)
    number=int(input("请输入一个1到100间的数字"))
    print("开始游戏")
    t=0
    while number!=n:
        if number>n :
            print("数字太大")
            t=t+1
            number=int(input("请重新输入>>"))
        elif number<n :
            print("数字太小")
            t=t+1
            number=int(input("请重新输入>>"))
    print("数字正确")
    print("猜的次数:" ,t)
    mind=input("是否继续游戏：（y/n）")

    
