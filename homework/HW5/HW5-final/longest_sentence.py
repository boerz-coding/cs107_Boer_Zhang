class LinkedList:

    def __init__(self, head, tail):
        assert isinstance(tail, LinkedList) or isinstance(tail, Nil), TypeError(
            'tail should either be a LinkedList or a Nil')
        self._head, self._tail = head, tail

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def __str__(self):
        return str(self._head) + ' -> ' + str(self._tail)

    def __repr__(self):
        return f'LinkedList({repr(self._head)}, {repr(self._tail)})'

    def __len__(self):
        return 1 + len(self._tail)

    def __getitem__(self, i):
        return self._head if i == 0 else self._tail[i-1]

    def prepend(self, val):
        return  LinkedList(val,self)

    def append(self, val):
        return  LinkedList(self._head, self._tail.append(val)) if self._tail else self.__init__(self._head, Nil.append(val))

    def for_each(self, fun):
        return  LinkedList(fun(self._head), self._tail.for_each(fun))

    def summation(self):
        return self._head + self._tail.summation() if self._tail else self._head

    def minimum(self):
        def smaller(a, b):
            return a if a < b else b
        return smaller(self._head, self._tail.minimum()) if self._tail else self._head

    def reduce_right(self, fun):
        return fun(self._head, self._tail.reduce_right(fun)) if self._tail else self._head
        

class Nil():

    def __str__(self): 
        return 'Nil'

    def __repr__(self):
        return 'Nil()'

    def __len__(self):
        return 0

    def __getitem__(self, i):
        raise IndexError('index out of range')

    def __bool__(self): 
        return False

    def prepend(self, val): 
        return LinkedList(val, Nil())

    def append(self, val):  
        return LinkedList(val, Nil())

    def for_each(self, fun):
        return Nil()
    
def get_list_of_sentences(chapter1='swansway-chapter1.txt'):
    def to_sentences(p):
            for delimiter in '.?!': p = p.replace(delimiter, '|')
            return [s.strip('\" ') for s in p.split('|')]
    with open(chapter1, 'r', encoding='UTF-8') as f:
        paragraphs = f.readlines()

    sentences = [s for p in paragraphs for s in to_sentences(p) if len(s) > 1]
    list_of_sentences = Nil()
    for s in sentences[::-1]:
        list_of_sentences = list_of_sentences.prepend(s)

    return list_of_sentences



def longest_sentence():
    def wordscount(mystr):
        return len(mystr.split()) 
        ##count words
    def larger(a, b): # our "combine" function
        return a if a > b else b
    list_of_sentences = get_list_of_sentences()
    list_of_lenghts=list_of_sentences.for_each(wordscount)
    return list_of_lenghts.reduce_right(larger)