from math import floor
from typing import List

class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.build_heap()

    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'
            #buf = buf + str(self.elements[idx]) + '\n' #use if above doesn't work

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                    self.to_string(new_prefix, self.left(idx), True) + \
                    self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> int:
        return self.size

    # TODO: override this in your dervied classes
    def compare(self, a: int, b: int) -> bool:
        raise NotImplementedError

    def heapify(self, idx: int) -> None:
        # TODO: your solution from the previous question can go here
        #       but remember to use your new "self.compare(a, b)" instead
        #       of raw comparisons
        newroot=idx
        l=self.left(idx)
        r=self.right(idx)
        if l < self.size and self.compare(self.elements[l],self.elements[newroot]):
            newroot=l
        
        if r < self.size and self.compare(self.elements[r],self.elements[newroot]):
            newroot=r
            
        if newroot != idx:
            self.elements[idx], self.elements[newroot]= self.elements[newroot], self.elements[idx]
            
            self.heapify(newroot)

    def build_heap(self) -> None:
        # TODO: your solution from the previous question can go here
        id0=self.size//2-1
        for i in range(id0,-1,-1):
            self.heapify(i)

    def heappush(self, key: int) -> None:
        # TODO: your solution from the previous question can go here
        #       but remember to use your new "self.compare(a, b)" instead
        #       of raw comparisons
        self.elements.append(key)
        self.size=len(self.elements)
        idn=self.size-1
        parentid=self.parent(idn)
        
        
        while parentid>=0 and self.compare(self.elements[idn],self.elements[parentid]):   
            self.elements[idn],self.elements[parentid]=self.elements[parentid],self.elements[idn]
            idn=parentid
            parentid=self.parent(idn)

    def heappop(self) -> int:
        # TODO: your solution from the previous question can go here
        if not self.elements:
            raise IndexError("Empty heap!")
        topvalue=self.elements[0]
        self.elements[0]=self.elements[self.size-1]
        self.elements.pop()
        self.size=self.size-1
        if self.size>0:
            self.heapify(0)
        return topvalue

class MinHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        return a<b    

class MaxHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        return a>b 