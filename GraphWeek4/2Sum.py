'''
The goal of this problem is to implement a variant of the 2-SUM algorithm covered in this week's lectures.

The file contains 1 million integers, both positive and negative (there might be some repetitions!).This is your array of integers, with the ithi^{th}ith row of the file specifying the ithi^{th}ith entry of the array.

Your task is to compute the number of target values ttt in the interval [-10000,10000] (inclusive) such that there are distinct numbers x,yx,yx,y in the input file that satisfy x+y=tx+y=tx+y=t. (NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space provided.


'''




content=open('2Sum.txt','r').readlines()
from collections import defaultdict,Counter
from bisect import bisect

store=[]

for i in content:
	store.append(int(i))

store.sort()

validSums=[]

def find(store,t):
	first=0
	last=len(store)-1
	found = False
	while first<=last and not found:
		midpoint=(first+last)//2
		if store[midpoint]==t:
			found=True
		else:
			if t<store[midpoint]:
				last=midpoint-1
			else:
				first= midpoint+1
	return found

allList=[]
maximum=store[-1]
minimum=store[0]


record={}
for i in range(-10000,10001):
	record[i]=0

l=0
for x in store:
	maximum,minimum=10000-x,-10000-x
	
	ind1=bisect(store,minimum)
	ind2=bisect(store,maximum)

	for y in store[ind1-1:ind2]:

		l=x+y

		if l in record.keys():
			record[l]=1

		
		



print(record)
print(Counter(record.values()))		
