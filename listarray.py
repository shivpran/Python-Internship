list=[1,2,3,4,5,"six","seven","eight","nine",10]
print(list)
for x in list:
    print(x)
print(len(list))
print(list[7])
list[1]="Two"
if "Two" in list:
    print("Found")
else:
    print("Not Found")
list.insert(9,"ten")
list.append(11)
list.remove(10)
list.pop()
del list[1]
myli=list.copy()
print(list)
print(myli)
list.remove("seven")
print(list)
list.clear()
print(list)
