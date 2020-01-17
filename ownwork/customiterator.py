

class Counter:

    def __init__(self,start,end,step=1):
        self.current=start 
        self.end=end
        self.step=step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current<self.end:
            num=self.current
            self.current+=self.step
            return num
        raise StopIteration

for i in Counter(10,20,2):
    print(i)