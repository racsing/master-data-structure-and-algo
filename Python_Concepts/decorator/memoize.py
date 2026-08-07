

def memoize(func):
    cache = {}

    def wrapper(*args):
        key = tuple(sorted(args))
        print("Key: ", key, cache)

        if cache and key in cache:
            print(f"Cache Hit for {key}")
            return cache[key]

        res = func(*args)
        cache[key] = res
        return res
    
    return wrapper


@memoize
def add(a, b):
    return a+b

if __name__ == "__main__":
    add(2, 5)
    add(3, 5)
    add(5, 2)
    add(7, 7)