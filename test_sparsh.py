from graph import Graph
from random_solver import RandomSolver
from deterministic_solver import DetermininsticSolver
from estimator_mean import EstimatorMean
import sys
import math

def compute_accurace(a,b,eps):
	# print(a)
	# print(b)
	v = 0
	s = 0
	for i in range(0,len(a)):
		if(b[i] <= (1+eps)*a[i] and  b[i] >= (1-eps)*a[i]):
			s = s + 1
	return (s/len(a))*100

def compute_std(a,b,eps):
	ans = 0
	n = len(a)
	for i in range(0,len(a)):
		ans += (a[i]-b[i])*(a[i]-b[i])/n
	
	return math.sqrt(ans)


g = Graph()
filename = sys.argv[1]
if( filename[-3:] == 'mat'):
	g.read_from_mat(filename)
else:
	g.read_from_txt(filename)
  
for i in range(20):
	print(i,g.adj_list[i])


ds = DetermininsticSolver(g)
ds.solve()

print("n = " + str(g.vertices))
print("for deterministic")
print("time = "+ str(ds.time))
print("-------------")

for i in range(20):
	print(i,ds.solution[i])


rs = RandomSolver(g,0.1)
em = EstimatorMean(g,0.1)

for eps in [0.1,0.05,0.001]:
	rs.change_eps(eps)
	rs.solve()
  
	
	a = compute_accurace(ds.solution, rs.solution, math.sqrt(rs.eps))
	b = compute_std(ds.solution, rs.solution, math.sqrt(rs.eps))
	
	print("for randomised estimator")
	print("for eps = "+ str(eps))
	print("time = "+str(rs.time))
	print("accuracy = "+ str(a))
	print("variance = "+ str(b))
	print("-------------")
	for i in range(20):
		print(i,rs.solution[i])

  
	em.change_eps(eps)
	em.solve()
	
	a = compute_accurace(ds.solution, em.solution, em.eps)
	b = compute_std(ds.solution, em.solution, math.sqrt(em.eps))
	
	print("for mean estimator")
	print("for eps = "+ str(eps))
	print("time = "+str(em.time))
	print("accuracy = "+ str(a))
	print("variance = "+ str(b))
	print("-------------")
	
	for i in range(20):
		print(i,em.solution[i])
	
