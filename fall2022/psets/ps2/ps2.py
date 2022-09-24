class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            ind = ind - left_size - 1
            return self.right.select(ind)
        return None

    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    

    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''
    def insert(self, key):
        if self.key is None:
            self.key = key
        elif self.key > key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
            self.size = self.size + 1
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)
            self.size = self.size + 1
        #self.calculate_sizes()
        return self
    
    ####### Part b #######

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate_left(self):
        # Using CLRS diagram for reference:
        #create a temp variable for easy manipulation of tree
        temporaryTree = BinarySearchTree(self.debugger)
        #set the temp tree's right child to be the original right child (i.e. parent 'y' with children 'beta' and 'gamma')
        temporaryTree.right = self.right

        #if subtree 'y' exists
        if self.right:
            #if the subtree 'y' has a left child 'beta'
            if self.right.left:
                #we will update our rotated tree's x node to have 'beta' be its right child
                self.right = self.right.left
            #otherwise, if the subtree 'y' does NOT have a left child 'beta'
            else:
                #then our rotated tree's node x will not have a right child, simple as that
                self.right = None
            if self.right:
                self.right.size = self.right.sizing()
            if temporaryTree.right:
                temporaryTree.right.size = temporaryTree.right.sizing()
            
            #change the temp tree's left side to now be original node 'x' with children 'alpha' and 'beta'
            temporaryTree.right.left = self
        
        return temporaryTree.right
    
    def rotate_right(self):
        # Using CLRS diagram for reference:
        #create a temp variable for easy manipulation of the tree 
        temporaryTree = BinarySearchTree(self.debugger)
        #set the temp's left child to be the original left child (i.e. paren 'x' with children 'alpha' and 'beta')
        temporaryTree.left = self.left

        #if subtree 'x' exists
        if self.left:
            #if the subtree 'x' has a right child 'beta'
            if self.left.right:
                #we will update our rotated tree's 'y' node to have 'beta' be its left child
                self.left = self.left.right
            #otherwise, if the subtree 'x' does NOT have a child 'beta'
            else:
                #then our rotated tree's node 'y' will not have a left child, simple as that
                self.left = None
            if self.left:
                self.left.size = self.left.sizing()
            if temporaryTree.left:
                temporaryTree.left.size = temporaryTree.left.sizing()

            #change the temp tree's right side to now be original node 'y' with children 'beta' and 'gamma'
            temporaryTree.left.right = self
        
        return temporaryTree.left
    
    def sizing(self):
        sizeOfTree = 0
        #if both sides exist, the size of the tree will be the sizes of the two branches combined
        if self.right and self.left:
            sizeOfTree = self.right.size + self.left.size
        #if only the right side exists
        elif self.right and not self.left:
            sizeOfTree = self.right.size
        #if only the left side exists
        elif self.left and not self.right:
            sizeOfTree = self.left.size
        #if the tree is a single node
        else:
            sizeOfTree = 1
        
        return sizeOfTree


    def rotate(self, direction, child_side):
        # First case: rotate("R", "R")
        if child_side == "R" and self.right:
            if direction == "R":
                #do the correct right rotation
                self.right = self.right.rotate_right()

                #adjust the sizes
                self.right.calculate_sizes()
            # Second case: rotate("L", "R")
            else:
                #do the correct left rotation
                self.right = self.right.rotate_left()
                
                #adjust the sizes
                self.right.calculate_sizes()
        # Third case: rotate("R", "L")
        elif child_side == "L" and self.left:
            if direction == "R":
                #do the correct right rotation
                self.left = self.left.rotate_right()
                
                #adjust the sizes 
                self.left.calculate_sizes()
            # Fourth case: rotate("L", "L")
            else:
                #do the correct left rotation
                self.left = self.left.rotate_left()

                #adjust the sizes
                #self.size = self.left.size + self.right.size
                self.size = self.left.size + self.right.size
        # Return the updated tree
        return self


# Testing trees
    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self

T = BinarySearchTree()
T.insert(5)
T.insert(6)
T.insert(7)
T.insert(1)
T.print_bst()
print("checking for correctness of select:")
print(T.select(0))