from graph import Graph
from random_solver import RandomSolver
from deterministic_solver import DetermininsticSolver
import sys

def compute_accurace(a,b,eps):
	# print(a)
	# print(b)
	v = 0
	s = 0
	for i in range(0,len(a)):
		if(b[i] <= (1+eps)*a[i] and  b[i] >= (1-eps)*a[i]):
			s = s + 1
	return (s/len(a))*100


g = Graph()
filename = sys.argv[1]
if( filename[-3:] == 'mat'):
	g.read_from_mat(filename)
else:
	g.read_from_txt(filename)


ds = DetermininsticSolver(g)
ds.solve()

print("n = " + str(g.vertices))
print("for deterministic")
print("time = "+ str(ds.time))
print("-------------")

rs = RandomSolver(g,0.1)

for eps in [0.1,0.05,0.001]:
	rs.change_eps(eps)
	rs.solve()
	a = compute_accurace(ds.solution, rs.solution, rs.eps)
	print("for eps = "+ str(eps))
	print("time = "+str(rs.time))
	print("accuracy = "+ str(a))
	print("-------------")
