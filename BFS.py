#Breadth first search simple implementation

##Complexity analysis:
##    Q is an array but acts like a queue where only the last element is accessed
##    visited is a dictionary which is accessed in constant time
##
##    While Q runs V times
##    for n in G[p] runs E times altogether as it runs
##    for every edge connected to each node
##
##    total runtime: V + E
##    space complexity: Q + visited

def BFS(G, s):

    #This is the queue that will visit every node
    Q = []

    #This is the visited dictionary to let us know if it has been visited
    visited = {}

    #Since we are starting at s, we will mark it as visted
    #And add it to the queue to visit all it's neighbours
    visited[s] = True
    Q.append(s)

    #While the Q is not empty, keep popping elements and
    #enqueueing their neighbours
    while Q:
        
        #Access the last element of Q and visit it's neighbours
        #If not already visted
        p = Q.pop()
        print( str(p) + " ")

        #Every edge connected to p
        for n in G[p]:
            #For every neighbour / adj node connected to p node
            if n not in visited:
                #You have visited it and now can add it to Q
                #To examine all it's nieghbours
                visited[n] = True
                Q.append(n)

#Recursive implementation of BFS
def recursiveBFS(G, Q, V):
    if not Q:
        return

    p = Q.pop()
    print( str(p) + " ")

    for n in G[p]:
        if n not in V:
            V[n] = True
            Q.append(n)
            
    recursiveBFS(G, Q, V)

graph = {0:[1,2], 1: [2], 2: [3, 4], 3: [1,2], 4: [0]}

#BFS(graph,0)

Q = [0]
V = {0:True}

recursiveBFS(graph, Q, V)


    
        
        
    

    
