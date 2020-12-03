import P3 as mypq
import matplotlib.pyplot as plt
ns=(10, 20, 50, 100, 200, 500)
tNaive=mypq.timeit(ns, mypq.NaivePriorityQueue)
tmyHeap=mypq.timeit(ns, mypq.HeapPriorityQueue)
tPython=mypq.timeit(ns, mypq.PythonHeapPriorityQueue)
plt.plot(ns,tNaive,label='NaivePQ')
plt.plot(ns,tmyHeap,label='MyHeapPQ')
plt.plot(ns,tPython,label='PythonHeapPQ')
plt.xlabel('Number of Lists Merged')
plt.ylabel('Elapsed time in seconds')
plt.legend()
plt.title('The running time of `mergesortedlists` with different heap implementations')
plt.show()