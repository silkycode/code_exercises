""" This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr. """

# returns a reference to a function that takes another function as an argument
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# uses the remembered info from input function's context as arguments for an internal function that returns the pair element
def car(f):
    def first(a, b):
        return a
    return f(first)

def cdr(f):
    def second(a, b):
        return b
    return f(second)

# return pair(f) with (a, b) in context
pair_function = cons(3, 4) 

# car and cdr take this pair function with context of (a, b) to pass internally
print(car(pair_function))
print(cdr(pair_function))

# could use lambdas (?)
# closures, need to do more research but DONE