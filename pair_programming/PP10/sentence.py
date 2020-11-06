# Coder: Ju Chulakadabba
# Listener: Kevin Hare, Boer Zhang


class Sentence: # An iterable
    def __init__(self, text): 
        self.text = text
        self.words = text.split()

    def __iter__(self):
        for word in self.words:
            yield word
        
        #return SentenceIterator(self.words)

    def __len__(self):
        return len(self.words)
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
if __name__ == "__main__":
    print('Example Sentence: the dogs will save the world.')
    s = Sentence("the dogs will save the world.")

    print('Print words in sentence:')
    for x in s:
        print(x)

    print('Manually use iter to iterate through words; end with StopIteration')
    it = iter(s)
    for x in range(len(s)+1):
        print(next(it))