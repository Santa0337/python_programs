s = "Python is a high level language"
 x = re.search("Python",s)
 print(x) 
print(x.group())    
print(x.start())    
print(x.end())      
print(x.span())     
# returns the matched group   
# returns the start index of matched string
 # returns the end index of matched string 
# returns the start & end indices of string in the form of tuple
