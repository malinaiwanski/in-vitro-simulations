import random
import numpy as np
import matplotlib.pyplot as plt
import math

def main():
###### INITIALIZE OUR PARAMETERS ######
	E=float(1) 
	alpha=float(0.01)
	iterations=1000000
	delt=0.01
	time=np.multiply(range(0,iterations+1),delt)
	y=range(0,iterations+1)
	y[0]=-1

	##### PERFORM EQUATION 1 for a large # of iterations and 4 different values of E ######

	for i in range(0,iterations):
	    g=random.gauss(0,1)
	    y[i+1] = y[i]+(alpha*E*(y[i])*(1-((y[i])**2)))+(math.sqrt(alpha/2)*g)
	    
	plt.plot(time,y)
	plt.show()
	plt.figure()
	plt.hist(y,50,normed='True')
	plt.show()


	########## SECOND TIME ##########
	y=range(0,iterations+1)
	y[0]=-1
	E=float(2) 

	for i in range(0,iterations):
	    g=random.gauss(0,1)
	    y[i+1] = y[i]+(alpha*E*(y[i])*(1-((y[i])**2)))+(math.sqrt(alpha/2)*g)
	    
	plt.plot(time,y)
	plt.show()
	plt.figure()
	plt.hist(y,50,normed='True')
	plt.show()

	########## THIRD TIME ###########
	y=range(0,iterations+1)
	y[0]=-1
	E=float(3) 

	for i in range(0,iterations):
	    g=random.gauss(0,1)
	    y[i+1] = y[i]+(alpha*E*(y[i])*(1-((y[i])**2)))+(math.sqrt(alpha/2)*g)
	    
	plt.plot(time,y)
	plt.show()
	plt.figure()
	plt.hist(y,50,normed='True')
	plt.show()

	####### FOURTH TIME (this one gives a "too large error")########
	y=range(0,iterations+1)
	y[0]=-1
	E=float(4) 

	for i in range(0,iterations):
	    g=random.gauss(0,1)
	    y[i+1] = y[i]+(alpha*E*(y[i])*(1-((y[i])**2)))+(math.sqrt(alpha/2)*g)
	    
	plt.plot(time,y)
	plt.show()
	plt.figure()
	plt.hist(y,50,normed='True')
	plt.show()


if __name__ == "__main__":
    x = main()
