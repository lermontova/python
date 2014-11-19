class Reverse(object):
    def __init__(self,data,sdvig):
        self.data=data
        self.index=len(data)
        self.sdvig=sdvig
        
    def __iter__(self):
        return self
    
    def next(self):
        if self.index<=self.sdvig:
            raise StopIteration
        self.index -=  self.sdvig
        return self.data[self.index]

r=Reverse('12345678912345935935935',12)
for i in r:
    print i, r.index
