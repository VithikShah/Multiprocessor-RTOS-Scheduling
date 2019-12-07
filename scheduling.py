import random
import math


def randomize(l , n):
	if n>=len(l):
		return l
	else:
		ans=[]
		for _ in range(n):
			index = math.floor( random.random()*len(l) )
			ans.append(l.pop(index))
		return ans	


def getCAD(l,cm,d,t):
	CAD = 0
	for i in l:
		CAD += (t+cm[i]) - d[i]
	return CAD


def main():
	#hard coded inputs
	ar = [0,3,1,5,10,12,15,18,20,25,0,0,0,10,10,25,18,20,20,23]
	cm = [5,2,2,5,5,2,5,2,5,5,3,2,3,5,5,3,2,3,1,5]
	d = [7,5,10,12,17,20,21,24,27,31,5,6,10,17,22,28,23,25,25,30]

	#taking input from user abt the number of processors
	np = int(input("Enter the number of processors:"))

	#setting up the tracking variables and counters
	isBusy = [-1] * np
	finishTime = [0] * np
	t = 0
	missed = 0


	while len(d)!=d.count(-1):
		#free the processors which should end
		for i in range(np):
			if t==finishTime[i] and t!=0:
				print(isBusy[i],"\t",t,"\t",d[ isBusy[i] ])
				#check if deadline is passed
				if t>d [ isBusy[i] ]:
					missed += 1
				#set the process as dead
				d[ isBusy[i] ] = -1
				#set the processor as free
				isBusy[i]=-1


		#utilise the free ones
		#get the count of free processors
		freeProcs = isBusy.count(-1)
		#prioritise on the number of free procssors over the ready processes
		if freeProcs!=0:
			readyIndexes = []#stores the indexes of ready processes
			for i in range(len(ar)):
				if ar[i]<=t and ar[i]!=-1:
					readyIndexes.append(i)

			#if any free processes
			if len(readyIndexes)>0:
				#nos is number of combinations we try
				nos = 500
				min_cad = 100000000000000
				finalProcess = [] #stores the chosen processes' indexes
				for _ in range(nos):
					choices = randomize( readyIndexes, freeProcs ) #selects freeProcs number of processes from readyIndexes
					cad = getCAD(choices,cm,d,t) #calculates thier CAD
					if cad<min_cad:
						min_cad = cad
						finalProcess = choices
				j = 0
				#allocating the processes
				for i in finalProcess:
					#setting processor trackers
					proc = isBusy.index(-1)
					finishTime[proc] = t + cm[i]
					isBusy[proc] = i
					#setting process trackers
					ar[i] = -1
		t+=1
	print("Deadlines missed:",missed)

if __name__ == '__main__':
	main()
