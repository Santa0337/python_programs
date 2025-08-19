def decor(func):
    def inner(name):
        if name == 'dhanush':
            print("Hello Dhanush Bad Morning")
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("Hello",name,"Good Morning")
wish('ravi')
wish('john')
wish('dhanush')