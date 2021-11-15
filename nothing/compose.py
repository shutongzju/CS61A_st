def compose(n):
    """Return a function that, when called n times repeatedly on unary
    functions f1, f2, ..., fn, returns a function g(x) equivalent to
    f1(f2( ... fn(x) ... )).
    >>> add1 = lambda y: y + 1
    >>> compose(3)(abs)(add1)(add1)(-4) # abs(add1(add1(-4)))
    2
    >>> compose(3)(add1)(add1)(abs)(-4) # add1(add1(abs(-4)))
    6
    >>> compose(1)(abs)(-4) # abs(-4)
    4
    """
    assert n > 0
    if n == 1:
        return lambda f: lambda x: f(x)

    def call(f):
        def on(g):
            return f(compose(n-1)(g))
        return on
    return call
