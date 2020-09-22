n=5391; a=0; b=0; c=0; d=0
a=n%10
print(a)
b=n//10%10
print(b)
a=n//9
b=n%9
print(a,"câtul",b,"restul")
a=n%10
b=n//10%10
c=n//100%10
d=n//1000
a=a+b+c+d
print(a)
a=n%10
if n == 0:
   print(a)
else:
    n=n//10
while n>0:
    pass
    a=a*10+n%10
    n=n//10
else:
    pass 
    print(a)