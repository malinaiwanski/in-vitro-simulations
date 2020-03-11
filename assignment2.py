
import matplotlib.pyplot as plt
import numpy as np

def gillespie(X,t):
#Function to update time/state vectors.

	a_1 = alpha[int(X[0])]	#Represents production of protein rate
	a_2 = X[1]/tau		#Represents degradation of protein rate
	a_3 = K/tau 			#Represents switching of states rate
	a = [a_1,a_2,a_3]
	a_0 = np.sum(a)

	nu_1 = [0,1]			#production
	nu_2 = [0,-1]		#degradation
	nu_3 = [1-2*X[0],0]	#switching of states 
	nu = [nu_1,nu_2,nu_3]

#Now we must make a couple of random #s, one to compute the time it takes for the reaction to complete, and one to decide which type of reaction we sample.

	random_time = np.random.random() 
	random_number = np.random.random() 
	
#Generation of reaction time (dividing by a0)
	time = np.log(1/random_time)/a_0 	

	j=0
	test=a[0]/a_0						
	while test<random_number:
		j+=1
		test += a[j]/a_0
		
	t += time 				#Update time
	X += nu[j]				#Update state 

	return X,t



#Initialize parameters and arrays
Nstep = 200
tau = 0.1
K = 100
alpha = [10,100]
X = np.zeros((Nstep,2)) 
t = np.zeros(Nstep)		
m = np.zeros(Nstep)		
off = np.zeros(Nstep)	


for i in range(0,Nstep-1): #Proceed through as many steps as we wish
	X[i+1,:],t[i+1] = gillespie(X[i,:],t[i]) #Run gillespie algorithm to update time and state vectors.
	m[i] = (alpha[0]-alpha[1])*tau*(np.exp(-t[i]/tau)-np.exp(-2*K*t[i]/tau))/(2*(2*K-1)) - (alpha[0]+alpha[1])*tau*(np.exp(-t[i]/tau)-1)/2
	off[i] = (1-np.exp(-2*K*t[i]/tau))/2
m[Nstep-1] = m[Nstep-2]
off[Nstep-1] = off[Nstep-2]