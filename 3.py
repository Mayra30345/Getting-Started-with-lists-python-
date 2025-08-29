L=[1,4,5,8,6,4,7,3]
print("Original value is: ",L)
count=0
for i in L:

 count+=i
avg=count/len(L)

print("The sum is:  ",count)
print("The average is:  ",avg)

L.sort()
print("The smallest element is:  ",L[0])
print("The largest element is:  ",L[-1])
