# Graph Search, Shortest Paths, and Data Structures
# Stanford University

Coursera Courses Assignment Solution

## Question 1

The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). 

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph.

Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer 
should be "400,300,100,0,0" (without the quotes). (Note also that your answer should not have any spaces in it.)



## Question2

The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200. Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200. The rest of the pairs of this row 
indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) 
as the source vertex, and to compute the shortest-path distances between 1 and every other vertex of 
the graph. If there is no path between a vertex vvv and vertex 1, we'll define the shortest-path distance 
between 1 and vvv to be 1000000.

You should report the shortest-path distances to the following ten vertices, 
in order: 7,37,59,82,99,115,133,165,188,197. You should encode the distances as a 
comma-separated string of integers. So if you find that all ten of these vertices except 115 are at 
distance 1000 away from vertex 1 and 115 is 2000 distance away, then your answer should be 1000,1000,1000,1000,1000,
2000,1000,1000,1000,1000. Remember the order of reporting DOES MATTER, and the string should be in the same order 
in which the above ten vertices are given. The string should not contain any spaces. Please type your answer in the 
space provided.

## Question3

The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 3 lecture on heap applications). The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one. 
In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). T
## Question4

The goal of this problem is to implement a variant of the 2-SUM algorithm covered in this week's lectures.

The file contains 1 million integers, both positive and negative (there might be some repetitions!).This is your array of integers, with the ithi^{th}ith row of the file specifying the ithi^{th}ith entry of the array.

Your task is to compute the number of target values ttt in the interval [-10000,10000] (inclusive) such that there are distinct numbers x,yx,yx,y in the input file that satisfy x+y=tx+y=tx+y=t. (NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space provided.
