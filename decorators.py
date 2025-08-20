# def decor(func):
#     def inner(name):
#         if name == 'dhanush':
#             print("Hello Dhanush Bad Morning")
#         else:
#             func(name)
#     return inner
# @decor
# def wish(name):
#     print("Hello",name,"Good Morning")
# wish('ravi')
# wish('john')
# wish('dhanush')
def decor(func):   
    def inner(name):   
        if name=="Sunny":   
            print("Hello Sunny Bad Morning")   
        else:   
            func(name)   
    return inner   
  
def wish(name):   
    print("Hello",name,"Good Morning")   
decorfunction=decor(wish)       
wish("Durga") #decorator won’t be executed   
wish("Sunny")      
decorfunction("Durga")#decorator will be executed   
decorfunction("Sunny") 
