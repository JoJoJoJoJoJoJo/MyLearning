class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
        
    def grade(self):
        if self.score >=80:
            return "A"
        elif self.score >=60:
            return "B"
        else:
            return "C"
        
    def print_re(self):
        print "%s,%s,%s"%(self.name,self.score,self.grade())# grade is not envolved in init,so here print it's func result
        
