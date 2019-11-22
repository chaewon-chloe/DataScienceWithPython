class Trie:
    '''Reperesents a Trie data structure'''
    
    def __init__(self):
        self.root = dict()
        
    
    def add(self,s):
        
        ### Defining a helper method
        def add_helper(s):
            if s == "":
                return {"" : None}
            return {s[0] : add_helper(s[1:])}
        
        ### Implementing the method 'add'
        if not isinstance(s, str):
            raise TypeError('"add" method only takes a string as input.')
            
        if len(s) ==0:
            raise ValueError('An empty string cannot be added to the Trie object.')
            
        x = self.root
        i = 0
        while True:
            if i == len(s):
                x[''] = None
                break
            elif s[i] not in x:
                x[s[i]] = add_helper(s[i+1:])
                break
            x = x[s[i]]
            i +=1

    def contains(self, s):
                    
        ### Defining a helper method
        def contains_helper(s,d):
            if s[0] not in d:
                return False
            else:
                if len(s)==1:
                    if('' in d[s[0]]):
                        return True
                    else: return False
                else:
                    return contains_helper(s[1:], d[s[0]])
        
        ### Implementing the method 'contains'
        d = self.root
        if not isinstance(s, str):
            raise TypeError('Please enter a string as input.')        
        if len(s) == 0:
            raise ValueError('An empty string is not valid.')
        else:
            return contains_helper(s,d)
        
    def __repr__(self):
        return "%s" % self.root
        
        
  def wordlist2trie(data):
    
    t = Trie()
    
    ### Error checking
    if type(data)!= type([]):
        raise TypeError('This function only takes a list of strings as input.')
    if not all(isinstance(i, str) for i in data):
        raise TypeError('All the elements in the input list must be strings.')
    
    ### 
    for i in data:
        t.add(i)
    
    return t    
    
    
import urllib.request
import re
url = 'http://www.greenteapress.com/thinkpython/code/words.txt'
request = urllib.request.urlopen(url)
response = request.read().decode('utf-8')
words = re.findall(r'\w+', response)
