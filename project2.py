#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
import time
import math


# In[23]:


## define node strucutre
class Node:
    def __init__(self,parent,position):
        self.parent = parent
        self.position = position
        self.f = 0
        self.g = 0
        self.h = 0
        # project 2 vars
        self.visited = False 
        self.status = 0 
        self.N = 0
        self.C = 0
        self.B = 0
        self.E = 0
        self.H = 0
    def __lt__(self,other):
        return self.f <= other.f

        


# In[24]:



def blank_space_a_star(know_base,start,end,cost,grid):
    '''
    know_base: [[Node,Node,...], [Node,Node,...],[Node,Node,...]]
    start: [0,0]
    end: [5,5]
    cost:1
    grid:[[0, 1, 0, 0, 0, 0], 
            [0, 1, 0, 1, 0, 0], 
            [0, 0, 0, 1, 0, 0], 
            [0, 1, 0, 1, 0, 0], 
            [0, 0, 0, 1, 0, 0], 
            [0, 0, 0, 1, 0, 0]]
    

    return: [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]
    '''
    ## know_base is already nodify --> all nodes 
#     print("grid",grid)
    start_node = know_base[start[0]][start[1]]
    end_node =  know_base[end[0]][end[1]]
    print(start_node.position)

    open_lst = []
    close_lst = []
    
    open_lst.append(start_node)
    current_node = open_lst[0]
    
    n_row,n_col = np.shape(grid)
    n_row = n_row -1
    n_col = n_col -1
    
    ## put start node into open_lst
    ## loop control, if open lst is not empty
    while len(open_lst)>0:

        
        open_lst.sort()

        current_node = open_lst.pop(0)
        close_lst.append(current_node)
        if current_node.position == end_node.position:
            return path_finder(current_node,grid,start_node,end_node)
        ## get current_node children
        child_loc = [
            [0,-1], ## moving left
            [0,1],  ## moving right
            [1,0],  ## moving down
            [-1,0] ## moving up
        ]
        
        for child in child_loc:

            mving_child = [current_node.position[0]+child[0],current_node.position[1]+child[1]]
            if mving_child not in [x.position for x in open_lst]:
                if mving_child not in [y.position for y in close_lst]:
                    if 0<=mving_child[0] <= n_row and 0<=mving_child[1] <=n_col:
                        if grid[mving_child[0]][mving_child[1]] == 1:
                            know_base[mving_child[0]][mving_child[1]].B = 1
                        else:
                            ## create new node
                            mving_node = Node(current_node,mving_child)
                            open_lst.append(mving_node)
        
        
        ## caluclate f,g,h
        ## heuristic: manhattan 
        for children in open_lst:
            children.g = children.g + cost 
            children.h = abs(children.position[0]-end_node.position[0])+ abs(children.position[1]-end_node.position[1])
            children.f = children.g + children.h
            
#         print("close_lst",[x.position for x in close_lst])
#         print("open_lst",[x.position for x in open_lst])
#         print("f value",[x.f for x in open_lst])
#         print("current_node",current_node.position)
#         print("---------------------")
    
    return path_finder(current_node,grid,start_node,end_node)


# In[25]:



def know_grid_star(know_base,start,end,cost,grid):
    '''
    know_base: [[Node,Node,...], [Node,Node,...],[Node,Node,...]]
    start: [0,0]
    end: [5,5]
    cost:1
    grid:[[0, 1, 0, 0, 0, 0], 
            [0, 1, 0, 1, 0, 0], 
            [0, 0, 0, 1, 0, 0], 
            [0, 1, 0, 1, 0, 0], 
            [0, 0, 0, 1, 0, 0], 
            [0, 0, 0, 1, 0, 0]]
    

    return: [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]
    '''
    ## know_base is already nodify --> all nodes 

    start_node = know_base[start[0]][start[1]]
    end_node =  know_base[end[0]][end[1]]
#     print(start_node.position)

    open_lst = []
    close_lst = []
    
    open_lst.append(start_node)
    current_node = open_lst[0]
    
    n_row,n_col = np.shape(grid)
    n_row = n_row -1
    n_col = n_col -1
    
    ## put start node into open_lst
    ## loop control, if open lst is not empty
    while len(open_lst)>0:

        
        open_lst.sort()
#         print("open_lst",[x.position for x in open_lst])
#         print("open_lst after sort",[x.position for x in open_lst])
#         print("f value",[x.f for x in open_lst])
#         for x in range(n_row):
#             for y in range(n_col):
#                 print("know_base[x][y].B",know_base[x][y].B)
#         print('-------->')
        current_node = open_lst.pop(0)
        close_lst.append(current_node)
        if current_node.position == end_node.position:
            return path_finder(current_node,grid,start_node,end_node)
        ## get current_node children
        child_loc = [
            [0,-1], ## moving left
            [0,1],  ## moving right
            [1,0],  ## moving down
            [-1,0] ## moving up
        ]
        
        for child in child_loc:

            mving_child = [current_node.position[0]+child[0],current_node.position[1]+child[1]]
            if mving_child not in [x.position for x in open_lst]:
                if mving_child not in [y.position for y in close_lst]:
                    if 0<=mving_child[0] <= n_row and 0<=mving_child[1] <=n_col:
                        if know_base[mving_child[0]][mving_child[1]].B != 1:
                            mving_node = Node(current_node,mving_child)
                            open_lst.append(mving_node)
        
        
        ## caluclate f,g,h
        ## heuristic: manhattan 
        for children in open_lst:
            children.g = children.g + cost 
            children.h = abs(children.position[0]-end_node.position[0])+ abs(children.position[1]-end_node.position[1])
            children.f = children.g + children.h
            
#         print("close_lst",[x.position for x in close_lst])
#         print("open_lst",[x.position for x in open_lst])
#         print("f value",[x.f for x in open_lst])
#         print("current_node",current_node.position)
#         print("---------------------")
    
    return path_finder(current_node,grid,start_node,end_node)


# In[26]:



# blank_route = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
def blind_folded(grid,start,end,cost,blank_route,know_base):
    '''
    know_base: [[Node,Node,...], [Node,Node,...],[Node,Node,...]]
    start: [0,0]
    end: [5,5]
    cost:1
    grid:[[0, 1, 0, 0, 0, 0], 
            [0, 1, 0, 1, 0, 0], 
            [0, 0, 0, 1, 0, 0], 
            [0, 1, 0, 1, 0, 0], 
            [0, 0, 0, 1, 0, 0], 
            [0, 0, 0, 1, 0, 0]]
    
    blank_route: [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]


    return: [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]
    '''

    final_lst = []
    if blank_route != 'Path is not found':
        while True:

            for x in know_base:
                print([y.B for y in x])
            if final_lst and final_lst[-1] == end:
                break 
            for step in blank_route:
                if grid[step[0]][step[1]] == 0:
                    final_lst.append(step) 
                else:
                    know_base[step[0]][step[1]].B = 1
                    break
            start = final_lst[-1]
#             print("start before new repeated_a_result",start)
            repeated_a_result = blank_space_a_star(know_base,start,end,cost,grid)
#             repeated_a_result = know_grid_star(know_base,start,end,cost,grid)

            ## [[5, 2], [4, 2], [4, 3], [4, 4], [5, 4], [5, 5]]
#             print("repeated_a_result--->",repeated_a_result)
            blank_route = repeated_a_result
            
    
            print("------- iteration -----------")
        return final_lst
    else:
        return 'No path'


# In[27]:


# blank_route = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
def repeated_a_star(grid,start,end,cost,blank_route,know_base):
    '''
    know_base: [[Node,Node,...], [Node,Node,...],[Node,Node,...]]
    start: [0,0]
    end: [5,5]
    cost:1
    grid:[[0, 1, 0, 0, 0, 0], 
            [0, 1, 0, 1, 0, 0], 
            [0, 0, 0, 1, 0, 0], 
            [0, 1, 0, 1, 0, 0], 
            [0, 0, 0, 1, 0, 0], 
            [0, 0, 0, 1, 0, 0]]
    
    blank_route: [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]


    return: [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]
    '''
    child_loc = [
            [0,-1], ## moving left
            [0,1],  ## moving right
            [1,0],  ## moving down
            [-1,0] ## moving up
        ]
    
    n_row,n_col = np.shape(grid)
    n_row = n_row -1
    n_col = n_col -1
    
    final_lst = []
    if blank_route != 'Path is not found':
        while True:

            for x in know_base:
                print([y.B for y in x])
            if final_lst and final_lst[-1] == end:
                break 
            for step in blank_route:
                if grid[step[0]][step[1]] == 0:
                    final_lst.append(step)
                    print("type(step)",type(step))
                    print("step",step)
                    for child in child_loc:
                        mving_child = [step[0]+child[0],step[1]+child[1]]
                        if 0<=mving_child[0] <= n_row and 0<=mving_child[1] <=n_col:
                            if know_base[mving_child[0]][mving_child[1]].B != 1:
                                know_base[mving_child[0]][mving_child[1]].E = 1
                else:
                    know_base[step[0]][step[1]].B = 1
                    break
            start = final_lst[-1]
#             print("start before new repeated_a_result",start)
            repeated_a_result = blank_space_a_star(know_base,start,end,cost,grid)
#             repeated_a_result = know_grid_star(know_base,start,end,cost,grid)

            ## [[5, 2], [4, 2], [4, 3], [4, 4], [5, 4], [5, 5]]
#             print("repeated_a_result--->",repeated_a_result)
            blank_route = repeated_a_result
            
    
            print("------- iteration -----------")
        return final_lst
    else:
        return 'No path'


# In[28]:


def path_finder(current_node,grid,start_node,end_node):
    '''
    current_node: Node
    grid:[[0, 1, 0, 0, 0, 0], 
            [0, 1, 0, 1, 0, 0], 
            [0, 0, 0, 1, 0, 0], 
            [0, 1, 0, 1, 0, 0], 
            [0, 0, 0, 1, 0, 0], 
            [0, 0, 0, 1, 0, 0]]
    
    current_node: Node
    end_node: Node


    return: [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]
    '''
    path = []
    
    current = current_node
    
    while current:
        
        path.append(current.position)
        
        current = current.parent
        
    path = path[::-1]
    
    if path[0] == start_node.position and path[-1] == end_node.position:
        return path
    else:
        return "Path is not found"


# In[29]:




def inference(blank_route,grid,start,end,cost,child_loc,know_base):
    
    final_lst = []
    if blank_route != 'Path is not found':
        while True:
            repeated_a_blank_path = [Node(None,x) for x in blank_route]
            print("blank_route-->",blank_route)
            print("final_lst--->",final_lst)
            if final_lst and final_lst[-1].position == end:
                break 
                
                
                
             ## sensing part    
            for step in repeated_a_blank_path:
                current_node = step
                ## sense 8 blocks
                for child in child_loc:
                    child_lst = []
        #             print("current_node.position",current_node.position)
                    mving_child = [current_node.position[0]+child[0],current_node.position[1]+child[1]]


                    ## check if the child is valid
                    if 0<=mving_child[0] < n_row and 0<=mving_child[1] <n_col:
                        child_lst.append(know_base[mving_child[0]][mving_child[1]])
                        current_node.N +=1

                        # check agent neighbors sensed to be blocked
                        if grid[mving_child[0]][mving_child[1]] == 1:
            #                     print("mving_child is 1",mving_child)
                            current_node.C +=1 

                        # check agent neighbors confirmed to be blocked
                        if know_base[mving_child[0]][mving_child[1]].B == 1:
                            current_node.B +=1 
                            current_node.status+=1
                        # check agent neighbors confirmed to be empty
                        if know_base[mving_child[0]][mving_child[1]].E == 1:
                            current_node.E +=1
                            current_node.status+=1
                    current_node.H = [x.status for x in child_lst].count(0)

                    
                    
                    
                    ## inference
                    if current_node.C == current_node.B:
                        for children in child_lst:
                            children.E = 1 
                    if current_node.N - current_node.C == current_node.E:
                        for children in child_lst:
                            children.B = 1 
#                 print("current node after inferrence -----> ",current_node.position)







                ## planning (infer a block --> a star)
#                 print("repeated_a_blank_path after inference",repeated_a_blank_path)
                b_check_path = [x.B for x in repeated_a_blank_path]
                ## if any block in the blank_route is blocked --> replan 
                ## if it's not walkable in true grid --> replan
                if (1 in b_check_path) or (grid[current_node.position[0]][current_node.position[1]] == 1):
                    print("inferred grid is not walkable")
                    lst_final_lst = [x.position for x in final_lst]
                    print("lst_final_lst pass into repeated_a",lst_final_lst[-1])
                    new_know_path = blank_space_a_star(know_base,lst_final_lst[-1],end,cost,grid)
                    blank_route = new_know_path
                    
                ## else add to the final list 
                else:
                    print("advance to the next node")
                    final_lst.append(current_node) 
                print("blank_route",blank_route)
                print("current node",current_node.position)
                print('final_lst',[x.position for x in final_lst])
                for x in know_base:
                    print([y.E for y in x])
        return final_lst
                


        


# In[30]:


def inference_agent4(blank_route, grid, start, end, cost, child_loc, know_base):
    final_lst = []
    if blank_route != 'Path is not found':
        while True:
            repeated_a_blank_path = [Node(None, x) for x in blank_route]
            print("blank_route-->", blank_route)
            print("final_lst--->", final_lst)
            if final_lst and final_lst[-1].position == end:
                break

                ## sensing part
            for step in repeated_a_blank_path:
                current_node = step
                ## sense 8 blocks
                for child in child_loc:
                    child_lst = []
                    hychild_1st = []
                    #             print("current_node.position",current_node.position)
                    mving_child = [current_node.position[0] + child[0], current_node.position[1] + child[1]]

                    ##------agent4-hy_child-----
                    hy_child = [mving_child[0] + child[0], mving_child[1] + child[1]]

                    ## check if the child is valid
                    if 0 <= mving_child[0] < n_row and 0 <= mving_child[1] < n_col:
                        child_lst.append(know_base[mving_child[0]][mving_child[1]])
                        current_node.N += 1

                        ##----check if the hychild is valid----
                    if 0 <= hy_child[0] < n_row and 0 <= hy_child[1] < n_col:
                        hychild_1st.append(know_base[hy_child[0]][hy_child[1]])

                        # check agent neighbors sensed to be blocked
                        if grid[mving_child[0]][mving_child[1]] == 1:
                            #                     print("mving_child is 1",mving_child)
                            current_node.C += 1

                            # check agent neighbors confirmed to be blocked
                        if know_base[mving_child[0]][mving_child[1]].B == 1:
                            current_node.B += 1
                            current_node.status += 1
                        # check agent neighbors confirmed to be empty
                        if know_base[mving_child[0]][mving_child[1]].E == 1:
                            current_node.E += 1
                            current_node.status += 1
                    current_node.H = [x.status for x in child_lst].count(0)

                    ## inference
                    if current_node.C == current_node.B:
                        for children in child_lst:
                            children.E = 1
                    if current_node.N - current_node.C == current_node.E:
                        for children in child_lst:
                            children.B = 1
                        #                 print("current node after inferrence -----> ",current_node.position)

                    ## duplicate a new knowledge base
                    know_base_new = know_base
                    ## the number of cells sensed to be blocked != confirmed --> have unrevealed neighbors
                    if current_node.C != current_node.B:
                        for children in child_lst:
                            children.B = 1
                            know_base_new[mving_child[0]][mving_child[1]].B = 1
                        for children in hychild_1st:
                            ## contradiction --> hypothetical cell is empty
                            if know_base_new[mving_child[0]][mving_child[1]].B > know_base_new[mving_child[0]][mving_child[1]].C:
                                children.B = 0
                                know_base_new[mving_child[0]][mving_child[1]].E = 1,
                                know_base_new[mving_child[0]][mving_child[1]].B = 0,
                                know_base = know_base_new
                            ## else cannot know whether the hypothetic cell is block or not

                ## planning (infer a block --> a star)
                #                 print("repeated_a_blank_path after inference",repeated_a_blank_path)
                b_check_path = [x.B for x in repeated_a_blank_path]
                ## if any block in the blank_route is blocked --> replan
                ## if it's not walkable in true grid --> replan
                if (1 in b_check_path) or (grid[current_node.position[0]][current_node.position[1]] == 1):
                    print("inferred grid is not walkable")
                    lst_final_lst = [x.position for x in final_lst]
                    print("lst_final_lst pass into repeated_a", lst_final_lst[-1])
                    new_know_path = blank_space_a_star(know_base, lst_final_lst[-1], end, cost, grid)
                    blank_route = new_know_path

                ## else add to the final list
                else:
                    print("advance to the next node")
                    final_lst.append(current_node)
                print("blank_route", blank_route)
                print("current node", current_node.position)
                print('final_lst', [x.position for x in final_lst])
                for x in know_base:
                    print([y.E for y in x])
        return final_lst


# In[31]:


if __name__ == "__main__":
    grid = [[0,1,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,1,0,0],
            [0,1,0,0,0,0],
            [0,0,0,1,0,0],
            [0,0,0,0,0,0]]
    start = [0,0]
    end = [5,5]
    cost = 1
    child_loc = [
            [0,-1], ## moving left
            [-1,-1], ## top left relative to mid 
            [0,1],  ## moving right
            [1,-1], ## top right relative to mid
            [-1,1],  ##bottom left relative to mid
            [1,1],  ## bottom right relative to mid 
            [1,0],  ## moving down
            [-1,0] ## moving up
        ]
    n_row,n_col = np.shape(grid)
    know_base = [[0 for j in range(n_row)]for i in range(n_col)]
    for x in range(n_row):
        for y in range(n_col):
#             print("x,y",x,y)
            know_base[x][y] = Node(None,[x,y])
    
    ## create blank_route
    blank_route = know_grid_star(know_base,start,end,cost,grid)
    
    ## Agent 1
    blind_fold = blind_folded(grid,start,end,cost,blank_route,know_base)
    
    ## Agent 2
    repeated_result = repeated_a_star(grid,start,end,cost,blank_route,know_base)
    
    ## Agent 3 
    Agent_3 = inference(blank_route,grid,start,end,cost,child_loc,know_base)

    ## Agent 4
    Agent_4 = inference_agent4(blank_route, grid, start, end, cost, child_loc, know_base)


# In[ ]:


import random

## maze function --> 101 x 101 
## '0' walkable
## '1' block
def create_maze(nx,ny,p_val):
    ##empty maze, all values are 0
    maze = [[0 for j in range(nx)]for i in range(ny)]
    
    ## loop each cell, calculate p value, resign val
    for i in range(nx):
        for j in range(ny):
            prob_test_for_each_blck = random.uniform(0, 1)
            if prob_test_for_each_blck <= p_val:
                maze[i][j] = 1 
    maze[0][0] = 0
    maze[100][100] = 0
    return maze


# In[ ]:


#agent 1,2,3,4 in dim(101)
if __name__ == "__main__":
    grid = create_maze(nx,ny,p_val)
    start = [0,0]
    end = [100,100]
    cost = 1
    child_loc = [
            [0,-1], ## moving left
            [-1,-1], ## top left relative to mid 
            [0,1],  ## moving right
            [1,-1], ## top right relative to mid
            [-1,1],  ##bottom left relative to mid
            [1,1],  ## bottom right relative to mid 
            [1,0],  ## moving down
            [-1,0] ## moving up
        ]
    n_row,n_col = np.shape(grid)
    know_base = [[0 for j in range(n_row)]for i in range(n_col)]
    for x in range(n_row):
        for y in range(n_col):
#             print("x,y",x,y)
            know_base[x][y] = Node(None,[x,y])
    
    ## create blank_route
    blank_route = know_grid_star(know_base,start,end,cost,grid)
    
    ## Agent 1
    blind_fold = blind_folded(grid,start,end,cost,blank_route,know_base)
    
    
    ## Agent 2
    repeated_result = repeated_a_star(grid,start,end,cost,blank_route,know_base)
    
    ## Agent 3 
    Agent_3 = inference(blank_route,grid,start,end,cost,child_loc,know_base)
   
    ## Agent 4
    Agent_4 = inference_agent4(blank_route, grid, start, end, cost, child_loc, know_base)


# In[ ]:


###total trajectory
def total_traj(nx,ny,p_val,know_base,start,end,cost,child_loc,grid):
    return_result = []
    pass_lst = []
#     #for x in range(5):
#     grid = create_maze(nx,ny,p_val)
#     start = [0,0]
#     end = [100,100]
#         maze = [[0 for j in range(nx)]for i in range(ny)]
    blank_route = know_grid_star(know_base,start,end,cost,grid)
    #test = inference(blank_route,grid,start,end,cost,child_loc,know_base)
#      ## Agent 1
#     blind_fold = blind_folded(grid,start,end,cost,blank_route,know_base)
    
    
#     ## Agent 2
#     repeated_result = repeated_a_star(grid,start,end,cost,blank_route,know_base)
    
    ## Agent 3 
    Agent_3 = inference(blank_route,grid,start,end,cost,child_loc,know_base)
    print(len(Agent_3[0]))
    #repeated_result = repeated_a_star(grid,start,end,cost,blank_route)
#     if Agent_3[-1] != 'Path is not found':
    pass_lst.append(int(len(Agent_3[0]) + len(Agent_3[-1])))
#         else:
#             pass_lst.append(0)
#     print(pass_lst)

     ## Agent 4 
#    Agent_4 = inference_agent4(blank_route, grid, start, end, cost, child_loc, know_base)
#    print(len(Agent_4[0]))
    #repeated_result = repeated_a_star(grid,start,end,cost,blank_route)
#     if Agent_4[-1] != 'Path is not found':
#    pass_lst.append(int(len(Agent_4[0]) + len(Agent_4[-1])))
    
    solv_result = sum(pass_lst)
    
    return [p_val,solv_result]


# In[ ]:


###full path length
def shortest_final_grid(nx,ny,p_val,know_base,start,end,cost,child_loc,grid):
    return_result = []
    avg_solv = []
    solv_result = []
    pass_lst = []
#     for x in range(5):
# #         for y in range(5):
#     grid = create_maze(nx,ny,p_val)
#     start = [0,0]
#     end = [100,100]
#     maze = [[0 for j in range(nx)]for i in range(ny)]
    blank_route = know_grid_star(know_base,start,end,cost,grid)
    #test = inference(blank_route,grid,start,end,cost,child_loc,know_base)
#     ## Agent 1
#     blind_fold = blind_folded(grid,start,end,cost,blank_route,know_base)
    
    
#     ## Agent 2
#     repeated_result = repeated_a_star(grid,start,end,cost,blank_route,know_base)
    
    ## Agent 3 
    Agent_3 = inference(blank_route,grid,start,end,cost,child_loc,know_base)

    ## Agent 4
#    Agent_4 = inference_agent4(blank_route, grid, start, end, cost, child_loc, know_base)
    
    #repeated_result = repeated_a_star(grid,start,end,cost,blank_route)
#     if Agent_3[-1] != 'Path is not found':
#             print('repeated_result',repeated_result)
    pass_lst.append(int(len(Agent_3[0]) + len(Agent_3[-1])))
#     else:
#         continue 
    print("pass_lst before calculation",pass_lst)                
    solv_result.append(min(pass_lst))
#     print("pass_lst",pass_lst)
#     print("solve_result",solv_result)
    
    return [p_val,solv_result]


# In[ ]:


###total planing time
def time_planning(nx,ny,p_val,know_base,start,end,cost,grid,child_loc):
    return_result = []
    solv_result = []
    #for x in range(5):
#         for y in range(5):
    grid = create_maze(nx,ny,p_val)
    start = [0,0]
    end = [100,100]
#         maze = [[0 for j in range(nx)]for i in range(ny)]
    blank_route = know_grid_star(know_base,start,end,cost,grid)
    #test = inference(blank_route,grid,start,end,cost,child_loc,know_base)
#     ## Agent 1
#     blind_fold = blind_folded(grid,start,end,cost,blank_route,know_base)
    
    
#     ## Agent 2
#     repeated_result = repeated_a_star(grid,start,end,cost,blank_route,know_base)
    
    ## Agent 3 
    Agent_3 = inference(blank_route,grid,start,end,cost,child_loc,know_base)
    repeated_result = repeated_a_star(grid,start,end,cost,blank_route,know_base)
        #repeated_a_star(grid,start,end,cost,blank_route)   
        
    ## Agent 4
#    Agent_4 = inference_agent4(blank_route, grid, start, end, cost, child_loc, know_base)
#    repeated_result = repeated_a_star(grid,start,end,cost,blank_route,know_base)

    time_now=time.time()
    solv_result.append(time_now)
#     print("pass_lst",pass_lst)
#     print("solve_result",solv_result)
    
    return [p_val,solv_result]


# In[ ]:


if __name__ == "__main__":
    grid = create_maze(nx,ny,p_val)
    start = [0,0]
    end = [100,100]
    cost = 1
    child_loc = [
            [0,-1], ## moving left
            [-1,-1], ## top left relative to mid 
            [0,1],  ## moving right
            [1,-1], ## top right relative to mid
            [-1,1],  ##bottom left relative to mid
            [1,1],  ## bottom right relative to mid 
            [1,0],  ## moving down
            [-1,0] ## moving up
        ]
    n_row = 101
    n_col = 101
    know_base = [[0 for j in range(n_row)]for i in range(n_col)]
    for x in range(n_row):
        for y in range(n_col):
#             print("x,y",x,y)
            know_base[x][y] = Node(None,[x,y])
    
    result_lst = []
    result_lst_sfd = []
    result_lst_time =[]
    nx,ny = 101,101
    for x in np.arange(0,0.33,0.05):
        p_val = float("{0:.2f}".format(x))
        result_lst.append(total_traj(nx,ny,p_val,know_base,start,end,cost,grid,child_loc))
        result_lst_sfd.append(shortest_final_grid(nx,ny,p_val,know_base,start,end,cost,grid,child_loc))
        result_lst_time.append(time_planning(nx,ny,p_val,know_base,start,end,cost,grid,child_loc))


# In[ ]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

x = [x[0] for x in result_lst]
y = [y[1] for y in result_lst]

fig, ax = plt.subplots()
ax.set_title("Total Trajectory Length vs Density", fontsize='16')
ax.plot(x, y)
# plt.set_title('Run Time Between Three Functions')
ax.xaxis.set_label_text("Density",fontsize='13')
ax.yaxis.set_label_text("total Trajectory Length",fontsize='13')
plt.grid()
plt.show()


# In[ ]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

x = [x[0] for x in result_lst_time]
y = [y[1] for y in result_lst_time]

fig, ax = plt.subplots()
ax.set_title("Total planning time vs Density", fontsize='16')
ax.plot(x, y)
# plt.set_title('Run Time Between Three Functions')
ax.xaxis.set_label_text("Density",fontsize='13')
ax.yaxis.set_label_text("total planning time",fontsize='13')
plt.grid()
plt.show()


# In[ ]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

x = [x[0] for x in result_lst_sfd]
y = [y[1] for y in result_lst_sfd]

fig, ax = plt.subplots()
ax.set_title("final path length vs Density", fontsize='16')
ax.plot(x, y)
# plt.set_title('Run Time Between Three Functions')
ax.xaxis.set_label_text("Density",fontsize='13')
ax.yaxis.set_label_text("final path length",fontsize='13')
plt.grid()
plt.show()

