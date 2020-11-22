from random import sample
from time import time
import P2 as myHeap
import heapq as pyHeap

class PriorityQueue:
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return len(self.elements) > 0

    def put(self, val):
        raise NotImplementedError # TODO

    def get(self):
        raise NotImplementedError # TODO

    def peek(self):
        raise NotImplementedError # TODO

def mergesortedlists(lists, pqclass=PriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists): 
        pq.put((l.pop(0), i))

    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i)) 

    return merged


def generatelists(n, length=20, dictionary_path='./words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists


def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=PriorityQueue, n_average=5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end   = time()
            timeaccum += end-start
        elapsed.append(timeaccum / n_average)
    return elapsed


class NaivePriorityQueue(PriorityQueue):
    def put(self, val):
        self.elements.append(val)
        if len(self.elements)>self.max_size:
            raise IndexError("Max size reached")

    def get(self):
        if len(self.elements) == 0:
            raise IndexError("Empty queue")
        minid=0
        minval=self.elements[0]
        for idx in range(0,len(self.elements)):
            if(self.elements[idx]<minval):
                minid=idx
                minval=self.elements[idx]
        self.elements.pop(minid)
        return minval

    def peek(self):
        if len(self.elements) == 0:
            raise IndexError("Empty queue")
        minid=0
        minval=self.elements[0]
        for idx in range(0,len(self.elements)):
            if(self.elements[idx]<minval):
                minid=idx
                minval=self.elements[idx]
        return minval
    
    
class HeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        super().__init__(max_size)
        self.heap=myHeap.MinHeap(self.elements)

        
    def put(self, val):
        if len(self.elements)==self.max_size:
            raise IndexError("Max size reached")
        self.heap.heappush(val)

    def get(self):
        if len(self.elements) == 0:
            raise IndexError("Empty queue")
        return self.heap.heappop()

    def peek(self):
        if len(self.elements) == 0:
            raise IndexError("Empty queue")
        return self.elements[0]
    

class PythonHeapPriorityQueue(PriorityQueue):

        
    def put(self, val):
        if len(self.elements)==self.max_size:
            raise IndexError("Max size reached")
        pyHeap.heappush(self.elements,val)

    def get(self):
        if len(self.elements) == 0:
            raise IndexError("Empty queue")
        
        return pyHeap.heappop(self.elements)

    def peek(self):
        if len(self.elements) == 0:
            raise IndexError("Empty queue")
        return self.elements[0]   
