from graph import Graph
import time
import sys
import math
import numpy as np 
#k = c(log(n))/eps
c = 1
class RandomSolver:

	def __init__(self,g,eps=0.01):
		self.orig_graph = g
		self.graph = g.reverse()
		self.solution = [-1 for i in range(0,self.graph.vertices)]
		self.time = 0.0
		self.eps = eps
		self.k = c*(int(math.log(self.graph.vertices)/self.eps) + 1)
		self.index = min(self.k - round(self.k/math.e),self.k-1)

	def solve(self):
		#iterate over each vertice
		start_time = time.time()

		#guess tracker (n*k)
		guess_tracker = [[-1.0 for i in range(0,self.k)] for j in range(0,self.graph.vertices)]

		#run random guessing
		for trial in range(0,self.k):
			
			#guess the natrual number for each vertice
			reward = []
			for v in range(0,self.graph.vertices):
				reward.append((np.random.random(),v))

			#sort the result
			reward.sort()

			#run the dfs from lowest number
			for (score,v) in reward:
				if(guess_tracker[v][trial] != -1.0):
					continue
				#run DFS
				stk = [v]
				guess_tracker[v][trial] = score
				while(len(stk) != 0):
					vp = stk.pop()
					for vc in self.graph.adj_list[vp]:
						if(guess_tracker[vc][trial] == -1):
							guess_tracker[vc][trial] = score
							stk.append(vc)

		#time to find soltion
		for v in range(0,self.graph.vertices):
			(guess_tracker[v]).sort()
			self.solution[v] = math.floor(1/guess_tracker[v][self.index])

		#done
		end_time = time.time()
		self.time = end_time - start_time
		return (self.solution,self.time)

	def change_eps(self,eps):
		self.solution = [-1 for i in range(0,self.graph.vertices)]
		self.time = 0.0
		self.eps = eps
		self.k = c*int(math.log(self.graph.vertices)/self.eps) + 1
		self.index = min(self.k - round(self.k/math.e),self.k-1)


# g = Graph()
# g.read_from_txt(sys.argv[1])
# s = RandomSolver(g,0.05)
# s.solve()
# print(s.solution, s.time)
# print(s.k,s.index)

