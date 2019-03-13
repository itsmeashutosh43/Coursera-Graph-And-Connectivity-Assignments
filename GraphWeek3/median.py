from heapq import *
content=open('mediam.txt','r').readlines()

k=0

heap1=[]
heap2=[]
medianSum=0

for i in content:

	if k==0:
		heappush(heap1,int(i))

	elif k==1:
		heappush(heap2,int(i))

		if heap1[0]>heap2[0]:
			temp=heappop(heap1)
			temp2=heappushpop(heap2,temp)
			heappush(heap1,temp2)

	else:
		
		SmallestOf1=nsmallest(1,heap1).pop()
		LargestOf2=nlargest(1,heap2).pop()
		SmallestOf2=nsmallest(1,heap2).pop()
		LargestOf1=nlargest(1,heap1).pop()

		number=int(i)

		if number>=LargestOf2 :
			heappush(heap2,number)

		elif number<=SmallestOf1 :
			heappush(heap1,number)

		elif number<=LargestOf1:
			heappush(heap1,number)

		else:
			heappush(heap2,number)

		if k==5:
			print(heap1,heap2)

		if k%2!=0:

			diff=len(heap1)-len(heap2)

			if diff>0:
				LargestOf1=nlargest(1,heap1).pop()
				heappush(heap2,LargestOf1)
				heap1.remove(LargestOf1)

			elif diff<0:

				SmallestOf2=heappop(heap2)
				heappush(heap1,SmallestOf2)

			else:
				pass




	if k%2!=0:
		LargestOf1=nlargest(1,heap1).pop()
		medianSum+=LargestOf1
	else:

		if len(heap1)>len(heap2):
			Largest=nlargest(1,heap1).pop()

		else:
			Largest=nsmallest(1,heap2).pop()

		medianSum+=Largest

		

	k+=1


print(medianSum%10000)