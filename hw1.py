l1=[1,2,3,4,5,6,7,8]
print(l1)
l2=[]
cube = lambda n: n ** 2
for i in range(0, len(l1)):
    l2.append(cube(l1[i]))
print(l2)
print("squred list:", l2)
