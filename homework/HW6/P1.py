from enum import Enum

class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if not node: 
            return BSTNode(key, val)
        if   key < node.key:
            node.left  = self._put(node.left,  key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if   key < node.key:
            return self._get(node.left,  key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    @staticmethod
    def _size(node):
        return node.size if node else 0
    
    
    ####my functions begin from here
    def _removemin(self,node):
        if not node:
            return None       
        elif node.left:
            node.left=self._removemin(node.left)
            node.size=1+ self._size(node.left) + self._size(node.right)
            return node
        else:
            return node.right
    
    def _findmin(self,node):
        if not node:
            return None       
        elif node.left:
            return _findmin(node.left)
        else:
            return node.key,node.val
     
    def remove(self, key):
        self._root = self._remove(self._root, key)
    
    
    def _remove(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if(key<node.key):
            node.left = self._remove(node.left, key)
        elif(key>node.key):
            node.right= self._remove(node.right, key)
        else:
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            
            node.key,node.val=self._findmin(node.right)
            node.right=self._removemin(node.right)
            
        node.size=1+ self._size(node.left) + self._size(node.right)
        return node
            


class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):

        self.index=0
        self.nodes_sorted=[]
        if traversalType is DFSTraversalTypes.PREORDER :
            self.preorder(tree)
        if traversalType is DFSTraversalTypes.INORDER :
            self.inorder(tree)
        if traversalType is DFSTraversalTypes.POSTORDER :
            self.postorder(tree)

    def __iter__(self):
        return self
    
    def __next__(self):  
        try:
            node = self.nodes_sorted[self.index]
        except IndexError:
            raise StopIteration()
        self.index+=1
        return node
        
        

    def inorder(self, bst:BSTTable):
        self._inorder(bst._root)
        
    
    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            self.nodes_sorted.append(node)
            self._inorder(node.right)

    def preorder(self, bst:BSTTable):
        self._preorder(bst._root)
        
    def _preorder(self,node):
        if node:
            self.nodes_sorted.append(node)
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self, bst:BSTTable):
        self._postorder(bst._root)
        
        
    def _postorder(self,node):    
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            self.nodes_sorted.append(node)