
def caching_fibonacci ():
    cache = dict()
    def fibonacci(n: int):
        if n <= 0: 
            return 0
        elif n == 1:
            return 1
        elif n in cache.keys():
            return cache[n]
        else:
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
            return cache[n]

    return fibonacci

fibonacci_result = caching_fibonacci()

print(fibonacci_result(5))
print(fibonacci_result(5))


        
