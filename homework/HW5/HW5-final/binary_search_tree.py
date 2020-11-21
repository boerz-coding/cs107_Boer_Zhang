class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = None
        self.right = None
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
        if node:
            if key<node.key:
                node.left=self._put(node.left,key,val)
                node.size+=1
            elif key>node.key:
                node.right=self._put(node.right,key,val)
                node.size+=1
            else:  ##key==node.key
                node.val=val
            return node
        else:
            return BSTNode(key,val)

    def _get(self, node, key):
        #print(node)
        if node:
            #print('here')
            if key<node.key:
                #print('left')
                return self._get(node.left,key)
            elif key>node.key:
                #print('right')
                return self._get(node.right,key)
            else:  ##key==node.key
                return node.val           
        else:
            raise KeyError('No such node is found')
            return None

    @staticmethod
    def _size(node):
        return node.size if node else 0