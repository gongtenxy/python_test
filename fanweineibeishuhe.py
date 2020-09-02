sum=0
for n in range(1,100):
    if n%3==0 or n%5==0:
        print(n)
        sum=sum+n
print("和为" , sum)
