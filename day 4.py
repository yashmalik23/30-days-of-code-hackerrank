class Person:
    a=int()
    def __init__(self,initialAge):
        self.a=initialAge
    def amIOld(self):
        if self.a<0:
            print('Age is not valid, setting age to 0.')
            self.a=0
        if self.a in range(0,13):
            print('You are young.')
        if self.a in range(13,18):
            print('You are a teenager.')
        if self.a >17:
            print('You are old.')
    def yearPasses(self):
        self.a+=1