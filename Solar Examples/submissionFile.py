import numpy
import os
import math
import sys

def getNumProcs(numAtoms):
	n = int(numAtoms)
	N = 0
	m = 0
	for m in range(0, m < n, 2):
		N = N + (2**(n - m)) * math.factorial(n) / (math.factorial(m) * math.factorial(n - m)) * math.factorial(m) / (math.factorial(m / 2) * math.factorial(m / 2))
	if(N < 8100):
		return 1
	elif(N >= 8100 and N <= 16000):
		return 4
	elif(N > 16000 and N <= 30000):
		return 6
	elif (N > 30000 and N <= 70000):
		return 12
	elif (N > 70000 and N <= 100000):
		return 24
	elif(N > 100000):
		return 48

def main(): 
	counter = 0
	for a in numpy.arange(2.5848457320184783,4.00484573202,.02):
		numP = getNumProcs(4)
		try:
			os.makedirs('/home/sebennett/Solar/Data/firstTestRunSolar/'+str(counter))
			paramFilePath = '/home/sebennett/Solar/Data/firstTestRunSolar/'+str(counter)+'/'
			pFile = os.path.join(paramFilePath, 'params.txt')
			paramFile = open(pFile, 'w')
			paramFile.write('Electric Field at run -> '+str(a)+', 9,.01, 2.5848457320184783,3.9848457320184783,.02, 1, firstTestRunSolar, /home/sebennett/Solar, /home/sebennett/Solar/Results, numProb, 30, 0, 0, 573, 587, 398, 421, 0, 0, 40, 1, 2, 0,120,40')
			paramFile.close()
		except OSError:
			pass
		for b in range(0,160,40):
			os.system("sbatch -N 1 -n "+str(numP)+" -p nodes -o /home/sebennett/Solar/Output/firstTestRunSolar-%j.out --nice=0 -J /home/sebennett/Solar Solar.sh "+str(numP)+" /home/sebennett/Solar/Exec/nn-avgmb-spps /home/sebennett/Solar/Data/firstTestRunSolar/"+str(counter)+" "+str(b)+" 40 /share/states/spps/spps_N_4.nc 4 9 .01 "+str(a)+" 1 30 0 0 573 587 398 421 0 0 40 1 2 0 120 40")
		counter += 1
if __name__ =='__main__': 
  main()