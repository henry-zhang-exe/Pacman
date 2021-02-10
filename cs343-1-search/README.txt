Name 1: Henry Zhang
Name 2: Michael Rodriguez-Labarca
eid 1: hz3953
eid 2: mr55397

Description: 

Our implementations for DFS, BFS, UCS, A * search, and UCS
were all inspired by the pseudocode that can be found in the textbook.
However, BFS did need one helper function that we created ourselves to 
construct a route back to the from the leaf to the root. 

Our corners heuristic is based on the idea that we need to visit all of
the corners in the order of which corner is closest to our current position,
our current position is updated to the corner is visited. We continue to sum
the distances until all corners have been reached.

Our corners successor function simply found all adjacent coordinates that were
not walls. If a successor coordinate is a corner, we then need to update 
the state of the successor before returning it.

Our food heuristic is based on the idea that for any next move, the cost from 
that point onwards can be no worse than the longest maze distance from Pacman's
current position to each coordinate in the remaining foodGrid list.