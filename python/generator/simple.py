# To create iterators using generators 

def even_generator():
        n=0

        n+=2
        yield n

        n+=2
        yield n

        n+=2
        yield n

numbers = even_generator()
print (next(numbers))    
print (next(numbers))
print (next(numbers))    