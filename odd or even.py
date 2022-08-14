
n=int(input('Enter your range of element'))
l=[]
for i in range(n):
    a=int(input('Enter the elements'))
    l.append(a)
print(l)

odd = 0
even = 0
for x in l:
        if x%2==0:
            even=even+1
        else:
            odd=odd+1
print("Number of even numbers :",even)
print("Number of odd numbers :",odd)



