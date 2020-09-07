user= input("user_name>>")
passwd=input("请输入密码>>")
if passwd=="123" :
    print("欢迎登录%s  " %user)
    print("*******************")
    print("1.创建新角色角色")
    print("2.使用已有角色")
    print("3.离开")
    print("*******************")
    choose_one=input("请据需要选择>>")
    if choose_one=='1' :
        name=input("请输入角色名")
        if name=="" :
            name="user1"
        list_1=[name,"hero","血值：",100,"攻击力：",100]   
        print('user:', user)
        print(list_1)
        wmap=['*','*','*','\n','*','*','*','\n','*','*','*']
        point=0
        while 1 :
            wmap[point]='0'
            print("".join(wmap))
            action=input("r or l or s or x or q>>")
            if action=='r'and (point-2<0 or point-5<0 or point-8<0) :
                wmap[point]='*'
                point+=1
            elif action=='l'and (point>0 or point-3>0 or point-6>0):
                wmap[point]='*'
                point-=1
            elif action=='s'and (point!=0 or point!=1 or point!=2):
                wmap[point]='*'
                point=point-3
            elif action=='x'and (point!=6 or point!=7 or point!=8):
                wmap[point]='*'
                point=point+3
            elif action=='q':
                break
else:print("password is wrong!!!")


