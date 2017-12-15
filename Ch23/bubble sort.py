#opt3 Jack Wu
list1=[2,4,1,65,23]

n=len(list1)-1


for i in range(n,0,-1):
    for j in range(i):
        if list1[j]>list1[j+1]:
            temp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp
   
print(list1)        
