class Student(Person):
    def calculate(self):
        a=sum(self.scores)/len(self.scores)
        if a>89:
            return 'O'
        elif a>79:
            return 'E'
        elif a>69:
            return 'A'
        elif a>54:
            return 'P'
        elif a>39:
            return 'D'
        else:
            return 'T'
    def __init__(self,first,last,idnum,score):
        self.firstName=first
        self.scores=score
        self.lastName=last
        self.idNumber=idnum
    