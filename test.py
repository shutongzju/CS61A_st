def is_prime(n):
    
    return prime_helper(n, n-1)

def prime_helper(n, i):
    
    if i == 1:
        return True

    elif n % i ==0:
        return False

    else:
        return prime_helper(n, i-1)

def merge(n1, n2):
    """ Merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10

def make_func_repeater(f, x):
    
    def repeat(n):
        if n == 1:
            return  f(x)
        return f(repeat(n-1))

    return repeat

def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0 or n == 1:
        return 1
    if n < 0:
        return 0
    
    return sum([count_k(n-x,k) for x in range(1,k+1)])

def check_mountain_number(n):
    def helper(alist):
        if len(alist) < 3 :
             return True
        if alist[0] < alist[1]:
            return helper(alist[1:])
        return alist[-1] < alist[-2] and helper(alist[:-1])
    return helper([int(x) for x in str(n)])

def merge(s1, s2):
    if len(s1) == 0:
        return s2
    if len(s2) == 0:
        return s1
    return ([s1[0]] + merge(s1[1:], s2[:]) if s1[0] < s2[0] else [s2[0]] + merge(s1[:], s2[1:]))


def mario_number(level):
    if level == '-':
        return 1
    if level[0] == 'P' or len(level) == 0:
        return 0

    if level[1] == '-':
        return mario_number(level[1:]) + mario_number(level[2:])

    return mario_number(level[2:])   
mario_number('---P----P-P---P--P-P----P-----P-')