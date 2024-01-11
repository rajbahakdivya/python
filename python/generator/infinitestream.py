# Generator to produce an infinte stream of fibonacci number(number where next element is the sum of last two element)

def generator_fibonacci():
        n1=0
        n2=1
        while True:
                yield n1
                n1,n2= n2,n1+n2

seq= generator_fibonacci()

print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))


