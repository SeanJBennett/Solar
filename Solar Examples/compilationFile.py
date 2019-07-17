import os
import numpy
import sys

def main(): 
	counter = 0
	try:
		os.makedirs('/home/sebennett/Solar/Results/firstTestRunSolar')
	except OSError:
		pass
	for x in numpy.arange(2.5848457320184783,4.00484573202,.02):
		os.system("java -classpath $CLASSPATH:/opt/share/rydberg/jar/mtj.jar:/opt/share/rydberg/jar/StarkMapper.jar:/opt/share/rydberg/jar/netcdfAll-4.0.jar:/data DDSimulator.DDDataReader /home/sebennett/Solar/Data/firstTestRunSolar/"+str(counter)+"/data_ 120 numProb /home/sebennett/Solar/Results/firstTestRunSolar/firstTestRunSolar_"+str(counter)+".txt 2")
		resFilePath = '/home/sebennett/Solar/Results/firstTestRunSolar/'
		joinString = 'firstTestRunSolar_'+str(counter)+'.txt'
		rFile = os.path.join(resFilePath,joinString)
		resFile = open(rFile,'a')
		resFile.write(',{'+str(x)+',9,.01, 2.5848457320184783,3.9848457320184783,.02, 1, firstTestRunSolar, /home/sebennett/Solar, /home/sebennett/Solar/Results, numProb, 30, 0, 0, 573, 587, 398, 421, 0, 0, 40, 1, 2, 0,120,40}}')
		resFile.close()
		resFile = open(rFile,'r')
		data = resFile.read()
		resFile.close()
		resFile = open (rFile,'w')
		resFile.write('{'+ data)
		resFile.close()
		counter += 1
	os.chdir('/home/sebennett/Solar/Results')
	os.system("tar czf firstTestRunSolar.tz.gz firstTestRunSolar")
if __name__ =='__main__': 
  main()