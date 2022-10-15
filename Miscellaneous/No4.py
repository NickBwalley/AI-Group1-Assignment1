import matplotlib.pyplot as plt
from collections import namedtuple

from utils import *
from npuzzle import NPuzzleState


def UCS(start_state, goal_state):
    
    frontier = PriorityQueue()
    node = Node(start_state, None, None, 0)
    frontier.push(node, 0)  # push node and its priority
    
    reached = dict() # a dictionary of (state, node)
    reached[start_state] = node
    
    num_generated = 0
    
    while not frontier.is_empty():
        # select a candidate node
        node = frontier.pop()
        
        # goal test
        if node.state == goal_state:
            return solution(node), num_generated
        
        # expand        
        for successor, action, step_cost in node.state.successors():
            num_generated += 1
            path_cost = node.cost + step_cost
            
            if successor not in reached or path_cost < reached[successor].cost:
                child_node = Node(successor, node, action, path_cost)
                reached[successor] = child_node
                frontier.push(child_node, path_cost)
    
    return None, num_generated  # if no solution found


# solution_path, N = UCS(start_state, goal_state)

# print(f"Number of generated nodes: {N}")
# show_solution(start_state, solution_path, ncols=6)





#-----------------------------------------------------------------------------------------------------------------------------


# def uniformCostSearch(problem):
#     """Search the node of least total cost first."""
#     nodes = PriorityQueue()
#     fringe = []
#     path = []
#     explored=set([]) # to ensure that the visited node cannot be repeated / re-added.
#     priority=0
#     dict={}
#     start_node = problem.getStartState()
#     if problem.isGoalState(start_node):
#         return 'already in goal'
#     else:
#         nodes.push((start_node, path),priority)
#         dict[start_node] = 0
#         explored.add(start_node)
#         while (nodes):
#             curr, path = nodes.pop()

#             if problem.isGoalState(curr):
#                 return path
#             else:
#                 next = problem.getSuccessors(curr)
#                 for node in nodes.heap:
#                     fringe.append(node[0])
#                 for states in next:
#                         if states[0] not in (key for key in dict):
#                             cost=problem.getCostOfActions(path + [states[1]])
#                             nodes.push((states[0], path + [states[1]]),cost)
#                             dict[states[0]]=cost
#                             explored.add(states[0])
#                         elif states[0] in (key for key in dict) and (problem.getCostOfActions(path + [states[1]]) < dict[states[0]]) :
#                             cost = problem.getCostOfActions(path + [states[1]])
#                             nodes.push((states[0], path + [states[1]]), cost)
#                             dict[states[0]] = cost
#                             explored.add(states[0])