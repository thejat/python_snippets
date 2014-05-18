# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <rawcell>

# You are given a rectangular grid of binary pixels, i.e., a bitmap where each of the pixels can be black or white. There is a number of black objects in the bitmap. You do not know their shape, size or position. If any part of two objects are on neighboring pixels, they are considered as one object. Write a program that takes the binary grid as input and returns the number of disjoint objects that can be found in the bitmap.
# 
# Example:
# 
# inputfile:
# . . . . . . . . . .
# . o . x . . . x . .
# . . . x . . . x . .
# . x x x . . . x x .
# . . . . . . . . . .
# . x . x . x x x x .
# . x . x . x x x x .
# . x . x . x x x x .
# . x x x . . . . . .
# . . . . . . . x x x 
# output: 5

# <codecell>

def numberOfComponents(arr2d,limits):
    visited = []#list of tuples (i,j) visited initially is 0
    count = 0 #initial number of connectd components is 0
    for i in range(limits[0]):
        for j in range(limits[1]):
            if((i,j) not in visited):
                visited.append((i,j))#irrespective of '.' or 'x', we have visited this position
                if arr2d[i][j] == '.':
                    continue
                visited = connected(arr2d,(i,j),visited,limits)#recursively find the component
                count+=1
    return count

def getNbhd(pos,limits):
    if pos[0]==0 and pos[1]==0:
        nbhd = [(pos[0]+x[0],pos[1]+x[1]) for x in [(1,0),(0,1),(1,1)]]
    elif pos[0]==limits[0]-1 and pos[1]==limits[1]-1:
        nbhd = [(pos[0]+x[0],pos[1]+x[1]) for x in [(-1,0),(0,-1),(-1,-1)]]
    elif pos[0]==0 and pos[1]==limits[1]-1:
        nbhd = [(pos[0]+x[0],pos[1]+x[1]) for x in [(1,0),(0,-1),(1,-1)]]
    elif pos[0]==limits[0]-1 and pos[1]==0:
        nbhd = [(pos[0]+x[0],pos[1]+x[1]) for x in [(-1,0),(0,1),(-1,1)]]
    elif pos[0]==0:
        nbhd = [(pos[0]+x[0],pos[1]+x[1]) for x in [(1,0),(0,1),(1,1),(0,-1),(1,-1)]]
    elif pos[0]==limits[0]-1:
        nbhd = [(pos[0]+x[0],pos[1]+x[1]) for x in [(-1,0),(0,-1),(-1,-1),(0,1),(-1,1)]]
    elif pos[1]==0:
        nbhd = [(pos[0]+x[0],pos[1]+x[1]) for x in [(-1,0),(1,0),(0,1),(-1,1),(1,1)]]
    elif pos[1]==limits[1]-1:
        nbhd = [(pos[0]+x[0],pos[1]+x[1]) for x in [(-1,0),(1,0),(0,-1),(-1,-1),(1,-1)]]
    else:
        nbhd = [(pos[0]+x[0],pos[1]+x[1]) for x in [(-1,0),(1,0),(0,-1),(0,1),(1,-1),(1,1),(-1,1),(-1,-1)]]
    return nbhd

#output of connected is a list of tuples visited upto this point 
def connected(arr2d,pos,visited,limits): #return the list of points visited while exploring this connected component
    nbhd = getNbhd(pos,limits)
    #print nbhd,pos
    for n in nbhd:
        if n in visited:
            continue
        visited.append(n) #append this position regardness of marking
        if arr2d[n[0]][n[1]] == 'x':
           visited = connected(arr2d,n,visited,limits)
    return visited 
      
def parseData(filename):
    limits = []
    #returns list of lists
    with open(filename,'rb') as fin:
        data = fin.read().split('\n')
        data = [x.split(' ') for x in data]
        if(data[-1][-1]==''):
            data[-1].pop()
        limits.append(len(data[1]))
        limits.append(len(data))
        return data,limits

arr2d,limits = parseData('data.md')
print 'Number of distinct connected components: ',numberOfComponents(arr2d,limits)

