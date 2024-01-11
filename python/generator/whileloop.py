#   implementing a loop to make this generator return even number till a certain max number.

def even_generator(max):
        n=2

        while n<=max:
                yield n
                n+=2

numbers = even_generator(4)
print (next(numbers))         #<- 2 is printed first
print (next(numbers))         #<- Next, 4 is printed
print (next(numbers))          #<- Finally, the loop condition (n<=max) is false because max is 4 and n is 6.Hence, the stopiteration exception is raised     