# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
finalPath = []

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def dfsHelper(problem, visited, currPath, currState):

    if(problem.isGoalState(currState)):
        print(currPath)
        return currPath[:]
    path = []
    for x in problem.getSuccessors(currState):
        if(x[0] in visited):
            continue
        currPath.append(x[1])
        visited.add(x[0])
        result = dfsHelper(problem, visited, currPath, x[0])
        if (result != []):
            path = result
        currPath.pop()
        visited.remove(x[0])
    return path

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    currState = problem.getStartState()
    visited = set()
    visited.add(currState)
    currPath = []
   
    result = dfsHelper(problem, visited, currPath, currState)

    return result

def bfsHelper(startCoordinate, finalCoordinate, parentDictionary, directionDictionary):
    path = util.Stack()
    while True:
        path.push(directionDictionary[finalCoordinate])
        finalCoordinate = parentDictionary[finalCoordinate]
        print(finalCoordinate)
        if(finalCoordinate == startCoordinate):
            break
    result = []
    while(not path.isEmpty()):
        result.append(path.pop())
    print(result)
    return result

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    currState = problem.getStartState()
    startCoordinate = currState
    frontier = util.Queue()
    frontier.push(currState)
    visited = set()
    visited.add(currState)
    finalCoordinate = (0,0)
    currPath = []
    parentDictionary = {}
    directionDictionary = {}
    while(not frontier.isEmpty()):
        #print("here")
        currState = frontier.pop()
        
        for x in problem.getSuccessors(currState):

            #print(x)
            #check later if in frontier
            if(x[0] not in visited):

                parentDictionary[x[0]] = currState
                directionDictionary[x[0]] = x[1]
                visited.add(x[0])
                if(problem.isGoalState(x[0])):
                    finalCoordinate = x[0]
                    print("found it")
                    break
                frontier.push(x[0])
    print(parentDictionary)
    print(directionDictionary)
    print(finalCoordinate)
    
                
    return bfsHelper(startCoordinate, finalCoordinate, parentDictionary, directionDictionary)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    currState = problem.getStartState()
    currCost = 0
    currPath = []
    frontier = util.PriorityQueue()
    frontier.push((currState, currCost, currPath), 0)
    visited = set()

    while not frontier.isEmpty():
        node = frontier.pop()
        currState = node[0]
        currCost = node[1]
        currPath = node[2]
        if(problem.isGoalState(currState)):
            return currPath
        visited.add(currState)
        for x in problem.getSuccessors(currState):
            print(x)
            successorState = x[0]
            successorPath = x[1]
            successorCost = x[2]
            
            if(successorState not in visited):
                print(currCost)
                print(successorCost)
                frontier.push((successorState, currCost + successorCost, currPath + [successorPath]), currCost + successorCost)
                
    return []
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
