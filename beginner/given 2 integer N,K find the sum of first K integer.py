x=int(input('Enter the N value:'))
y=int(input("enter the k value:"))
l=[int(input()) for i in range(0,x)]
if y<x:
    l=l[:y]
    s=sum(l)
    print(s)
else:
    print("wrong input:")
