class Numbers(object):
    def __init__(self, lst):
        self.list = lst

    def get_addends_indices_for(self, sum):
        addend_map = { }
        for index, addend in enumerate(self.list):
            required_addend = sum - addend
            
            if required_addend in addend_map:
                return (addend_map[required_addend], index)     # returns indices of both addends 
            
            addend_map[addend] = index
        
        return (None, None)
