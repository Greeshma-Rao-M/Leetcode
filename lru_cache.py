class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache=OrderedDict()  #--> self.cache={}

    def get(self,key:int)->int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)   #--> val=self.cache.pop(key)
        return self.cache[key]        #self.cache[key]=val
                                    #return val
        
    def put(self, key:int, value:int)->None:
        if key in self.cache:
            self.cache.move_to_end(key)  #self.cache.pop(key)
        self.cache[key]=value
        if len(self.cache)>self.capacity:
            lru=self.cache.popitem(last=False)  #lru=list(self.cache.keys())[0]
                                                #self.cache.pop(lru)
