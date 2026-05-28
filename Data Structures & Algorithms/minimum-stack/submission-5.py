class MinStack:

    def __init__(self):
        self.stack = [] #stack of tuples
        ordered_list = []
        self.local_min = None

    def push(self, val: int) -> None:
        temp =  0
        if self.local_min is None: #first element of the stack, establish local min
            self.local_min = val
            self.stack.append((val, self.local_min)) #then the first element points to itself
        elif val < self.local_min: #if value is less than local min, append it with val, local_min #creating a chain 
            self.stack.append((val, self.local_min))
            self.local_min = val
        else: #neither the smallest, or the first element
            self.stack.append((val, None))



    def pop(self) -> None:
        if(self.stack[-1][1] is not None): #there is a chain, update it to the next 
            if len(self.stack) == 1: #if it's the last element, set the min to None
                self.local_min = None
                #self.stack.pop()
            else:
                self.local_min = self.stack[-1][1] #update local min
                #self.stack.pop()
        #else: #it's an element that's in between, just remove it
            #self.stack.pop()
        self.stack.pop()

        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.local_min
        
