

def count_calls(func):
    print("Decorator executed")

    def wrapper(*args, **kwargs):
        print("Wrapper executer")
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper
    
@count_calls
def greet(name):
    return f"Hello, {name.title()}"

print("Before main")

if __name__ == "__main__":
    print("Inside main")
    print(greet('rachana'))
    print(greet('shiv'))
    print(greet.count)
    