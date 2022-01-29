from graph import Graph
import time
import sys

class DetermininsticSolver:

	def __init__(self,g):
		self.graph = g
		self.solution = [-1 for i in range(0,self.graph.vertices)]
		self.time = 0.0

	def solve(self):
		#iterate over each vertice
		start_time = time.time()
		for v in range(0,self.graph.vertices):
			visited = [0 for j in range(0,self.graph.vertices)]
			stk = [v]
			visited[v] = 1
			vscore = 0
			while(len(stk) != 0):
				vp = stk.pop()		
				vscore = vscore + 1
				for vc in self.graph.adj_list[vp]:
					if(visited[vc] == 0):
						visited[vc] = 1
						stk.append(vc)
			self.solution[v] = vscore
		end_time = time.time()
		self.time = end_time-start_time
		return(self.solution,self.time)

# g = Graph()
# g.read_from_txt(sys.argv[1])
# s = DetermininsticSolver(g)
# s.solve()
# print(s.solution, s.time)


