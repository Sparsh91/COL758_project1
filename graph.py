import scipy.io
import numpy as np
import sys

class Graph:

	def __init__(self):
		self.vertices = 0
		self.edges = 0

	def read_from_mat(self,filename):
		file_data = scipy.io.loadmat(filename)
		adj_mat = file_data['Problem'][0][0][2]
		self.vertices = adj_mat.shape[0]
		self.adj_list = [[] for i in range(0,self.vertices)]
		adj_dict = adj_mat.todok().items()
		for e in adj_dict:
			(self.adj_list[e[0][0]]).append(e[0][1])
		self.edges = len(adj_dict)

	def write_to_file(self,filename):
		f = open(filename,"w")
		f.write(str(self.vertices) + "\n")
		f.write(str(self.edges) + "\n")
		for i in range(0,self.vertices):
			for j in self.adj_list[i]:
				f.write(str(i) + " "+ str(j))
				f.write('\n')
		f.close()

	def read_from_txt(self,filename):
		f = open(filename,"r")
		self.vertices = int(f.readline())
		self.edges = int(f.readline())
		self.adj_list = [[] for i in range(0,self.vertices)]
		for i in range(0,self.edges):
			l = f.readline().split(' ')
			self.adj_list[int(l[0])].append(int(l[1]))

	def print_info(self):
		print("Vertices: "+str(self.vertices))
		print("Edges: "+str(self.edges))

	def reverse(self):
		g = Graph()
		g.vertices = self.vertices
		g.edges = self.edges
		g.adj_list = [[] for i in range(0,self.vertices)]
		for i in range(0,self.vertices):
			for j in self.adj_list[i]:
				g.adj_list[j].append(i)
		return g
		
	def linear_graph(self,n):
		self.vertices = n
		self.edges = n-1
		self.adj_list = [[] for i in range(0,n)]
		for i in range(0,n-1):
			(self.adj_list[i]).append(i+1)

# g = Graph()
# g.read_from_mat(sys.argv[1])
# g.print_info()
# g.write_to_file("g4.txt")
# g.read_from_txt("g1.txt")
# g2 = g.reverse()
# g2.write_to_file("g1r.txt")
# g.print_info()
