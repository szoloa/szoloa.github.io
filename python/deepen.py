import os
import rand_s

class deepen:
    def __init__(self,path) -> None:
        self.path = path
    def run(self):
        print('mima:')
        print(rand_s.rands(36).string)
        print('content:')
        for i in os.walk(self.path):
            print(i)