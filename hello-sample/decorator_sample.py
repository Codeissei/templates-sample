def outer(func):
    def inner():
        print("開始")
        func()
        print("終了")
    return inner

def a():
    print("Aですわ")
    
test = outer(a)
test()
