#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    
    #First check to see if v is a valid vertex
    if v is None: 
        return 0
    
    #If it is a valid vertex, recursively move down the right and left branches adding 1 every time 
    #you encounter a valid vertex
    v.size = 1 + calculate_sizes(v.left) + calculate_sizes(v.right)
    return v.size
    
    #Reasoning for why this solution is of O(n) complexity:
    #Big O calculates the time complexity in terms of the worst-case scenario. This solution has O(n)
    #time complexity because in the worst-case scenario (when the binary tree is very deep) it will take
    #linear time to calculate the sizes of all subtrees within. This is because the solution calculates
    #each height level of the tree in one iteration since we are calculating the size of the left and 
    #right branches in one equation.

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r): 
    
    #First, let's define a variable to represent 'at most n/2 vertices'
    maxSize = r.size/2

    #Let's check for the validity of r
    if r is None:
        return 0

    #Let's also check for the case that r is the only node 
    if (r.right is None) and (r.left is None):
        return r

    #Now, assuming we have a tree of a height of at least 2
    while r.right or r.left:
        
        #If both children of r exist
        if r.right and r.left:

            #If the tree is balanced
            if (r.right.size <= maxSize) and (r.left.size <= maxSize):
                return r
            #If the tree is right-heavy
            elif r.right.size > r.left.size:
                r = r.right
            #If the tree is left-heavy
            else:
                r = r.left
        
        #If right child exists, but no left
        if r.right and (not r.left):
            r = r.right
        
        #If left child exists, but no right
        if r.left and (not r.right):
            r = r.left
    
    return r

    #Reasoning for why this solution is O(h) complexity:
    #This solution is O(h) complexity because in the worst-case scenario (when the height of 
    #the tree is large), the algorithm will iteratively go through each height level,
    #and at some point reach h, before it finds its needed vertex.