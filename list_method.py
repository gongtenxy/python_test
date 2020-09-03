act='s'
list_1=[]
while act!='q' :
    information=input("请输入一系列值(输入q时退出)>>>")
    act=information
    list_1.append(information)
print(list_1)
list_2=[]
while list_1!=[] :
    for i in list_1 :
        i=list_1.pop ()
        list_2.append(i)
print("倒序列表为：")
print(list_2)
