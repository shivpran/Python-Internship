D={"Name":"Shivam","Email":"adcd@gmail.com","Contact":123456789}
print(D)
for x in D:
    print(x)
print(len(D))
#print(D[1])
D["Add"]="Amt"
if "Amt" in D:
    print("Found")
else:
    print("Not Found")
print(D)
#D.insert(4,"ten")
#D.append(11)
#D.remove("Amt")
D.pop(3,"Amt")
del D["Add"]
print(D)
myli=D.copy()
print(D)
print(myli)
#list.remove("seven")
#print(list)
