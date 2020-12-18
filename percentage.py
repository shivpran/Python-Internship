n=int(input("Enter Number of Subjects:-"))
l=[]
for i in range(0,n):
    y=int(input("Enter Marks of Subject:-"))
    l.append(y)
    s=sum(l)
p=s/n
print("Percentage is:-",p,"%")
