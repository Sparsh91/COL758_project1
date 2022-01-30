from sklearn.metrics import accuracy_score
from graphGenerator_G_n_p import G
from graph import Graph
from random_solver import RandomSolver
from deterministic_solver import DetermininsticSolver
from estimator_mean import EstimatorMean
import sys

def compute_accurace(a,b,eps):
	eps = eps**0.5
	v = 0
	s = 0
	for i in range(0,len(a)):
		v = v + abs(a[i]-b[i])**2
		if(b[i] <= (1+eps)*a[i] and  b[i] >= (1-eps)*a[i]):
			s = s + 1
		
	return (s/len(a))*100

p = 0.001
accuracy_random_1 = []
accuracy_random_2 = []
accuracy_random_3 = []
probabs = []
time_determin = []
time_random_1 = []
time_random_2 = []
time_random_3 = []

while(p<=0.3):
		G(1000,p)
		probabs.append(p)
		p = p*1.25
		g = Graph()
		g.read_from_txt('g1.txt')
		ds = DetermininsticSolver(g)
		ds.solve()
		time_determin.append(ds.time)
		rs = RandomSolver(g,0.1)
		for i,eps in enumerate([0.1,0.05,0.001]):
			rs.change_eps(eps)
			rs.solve()
			a = compute_accurace(ds.solution, rs.solution, rs.eps)
			if(i==0):
					time_random_1.append(rs.time)
					accuracy_random_1.append(a)
			if(i==1):
					time_random_2.append(rs.time)
					accuracy_random_2.append(a)
			if(i==2):
					time_random_3.append(rs.time)
					accuracy_random_3.append(a)

import matplotlib.pyplot as plt
plt.plot(probabs,accuracy_random_1, label = "eps = 0.1")
plt.plot(probabs,accuracy_random_2, label = "eps = 0.05")
plt.plot(probabs,accuracy_random_3, label = "eps = 0.001")
plt.xlabel('probabilities -- p in G(1000,p)')
plt.ylabel('accuracy in percentage')
plt.title('accuracy as a function of probabilities for G(1000,p)')
plt.legend()
plt.show()

import matplotlib.pyplot as plat
plat.plot(probabs,time_determin,label = 'deterministic time')
plat.plot(probabs,time_random_1, label = "eps = 0.1")
plat.plot(probabs,time_random_2, label = "eps = 0.05")
plat.plot(probabs,time_random_3, label = "eps = 0.001")
plat.xlabel('probabilities -- p in G(1000,p)')
plat.ylabel('time in sec')
plat.title('time taken as a function of probabilities for G(1000,p)')
plat.legend()
plat.show()

# print("probabs:-")
# print(*probabs)
# print()
# print("time:- ")
# print(*time_determin)
# print(*time_random_1)
# print(*time_random_2)
# print(*time_random_3)
# print()
# print("accuracy:- ")
# print(*accuracy_random_1)
# print(*accuracy_random_2)
# print(*accuracy_random_3)


