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
    
    if v is None: 
        return 0
    
    v.size = 1 + calculate_sizes(v.left) + calculate_sizes(v.right)
    return v.size
    #Add comments later here!
    
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
    
    #Through experimentation I have found that if the tree is balanced (i.e. both the right and left branches
    #are of the same height and contain the same amount of nodes) then the vertex that would make the disjoint
    #trees all of at most size n/2 is the root node
    while r and r.right or r.left:
        if r.right.size == r.left.size:
            return r
        #Else, we want to find the subtree that is deeper (i.e. higher) and move down it, setting the new r to be
        #the vertext at which that subtree is rooted; here we assume it is the right subtree
        elif r.right and r.right.size > r.left.size:
            r = r.right
        #Here, we assume it is the left subtree
        else:
            r = r.left
    return r
    #The reason we want to move down the deeper of the two subtrees is because removing the root vertex of the deeper
    #of the two subtrees will result in disjoint trees that all have the size of at most n/2.
    #Moving down the more shallow of the two subtrees and removing its root vertex will create at least one disjoint 
    #tree that has a size greater than n/2; we do not want that.
