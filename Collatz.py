number=int(input("输入数字>>"))
while number!=1:
  if number%2==0 :
      number=number/2
      number=int(number)
      print(number)
  elif number%2==1 :
      number=number*3+1
      print(number)
      
