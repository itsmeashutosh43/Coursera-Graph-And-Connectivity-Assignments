'''
The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 3 lecture on heap applications). The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one. Letting xix_ixi​ denote the iiith number of the file, the kkkth median mkm_kmk​ is defined as the median of the numbers x1,…,xkx_1,\ldots,x_kx1​,…,xk​. (So, if kkk is odd, then mkm_kmk​ is ((k+1)/2)((k+1)/2)((k+1)/2)th smallest number among x1,…,xkx_1,\ldots,x_kx1​,…,xk​; if kkk is even, then mkm_kmk​ is the (k/2)(k/2)(k/2)th smallest number among x1,…,xkx_1,\ldots,x_kx1​,…,xk​.)

In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). That is, you should compute (m1+m2+m3+⋯+m10000)mod10000(m_1+m_2+m_3 + \cdots + m_{10000}) \bmod 10000(m1​+m2​+m3​+⋯+m10000​)mod10000.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and search-tree-based implementations of the algorithm.

'''




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