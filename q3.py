from graph import Graph
from random_solver import RandomSolver
from deterministic_solver import DetermininsticSolver
import sys
import math

def compute_accurace(a,b,eps):
	# print(a)
	# print(b)
	v = 0
	s = 0
	sv = 0
	vv = 0
	found = False
	vc = -1
	for i in range(len(a)-1,-1,-1):
		#print(i,a[i],b[i])
		sv = sv +  abs(a[i]-b[i])
		vv = a[i] + vv
		if(not found and b[i] <= (1+eps)*a[i] and b[i] >= (1-eps)*a[i]):
			s = s +  1
			found = True
			vc = (len(a) - i)+1
	return ((1-sv/vv)*100,(1-s/len(a))*100,vc)

for i in range(1300,5001,100):

	g = Graph()
	g.linear_graph(i)

	# print("n = " + str(g.vertices))
	# print("for deterministic")
	# print("time = "+ str(ds.time))
	# print("-------------")
	print("for n = "+ str(i))

	rs = RandomSolver(g,0.1)

	for eps in [0.1,0.05,0.001]:
		rs.change_eps(eps)
		rs.solve()
		sol = [i-j+1 for j in range(0,i)]
		a = compute_accurace(sol, rs.solution, math.sqrt(rs.eps))
		#a = compute_accurace(ds.solution, rs.solution, math.sqrt(rs.eps))
		print("for eps = "+ str(eps))
		print("time = "+str(rs.time))
		print("accuracy mse = "+ str(a[0]))
		print("accuracy (1+eps) = "+ str(a[1]))
		print("smallest set = "+str(a[2]))
		print("-------------")


# N = [1000
# 2000 
# 3000
# 5000
# 10000
# 15000
# ] A B C D E F
# 1000 79.3 90.08 98.75 14 25 112
# 2000 89.10 95.3 98.33 6 10 100 
# 3000 93.52 93.0 98.17 7 5 90
# 5000 94.22 93.97 98.39 32 9 744 
# 10000 93 91 98 9 22 88
# 15000 93 94 98 24 16 175
# g = Graph()
# g.read_from_mat(sys.argv[1])
# g.print_info()
# g.write_to_file("g4.txt")
# g.read_from_txt("g1.txt")
# g2 = g.reverse()
# g2.write_to_file("g1r.txt")
# g.print_info()
