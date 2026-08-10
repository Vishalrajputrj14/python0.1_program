def greet(fx0):
    def mfx():
        print("good morning")
        fx0()
        print("thanks for using this function")
    return mfx

@greet
def hello():
    print("hello world")

def add(x,y):
    print(f"the sum of {x} and {y} is {x+y}")


hello()
add(5,10)