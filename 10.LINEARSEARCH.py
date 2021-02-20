n=int (input ("Enter the no. of element"))
i=0
a= [i for i in range(n)]
for i in range (0, n):
 a[i]=int (input ("enter the array element"))
for i in range (0, n):
 print (a[i])
key=int (input ("Enter the key element to be searched"))
for i in range (0, n):
 if a[i]==key:
  print ("key found")