class A(object):
    def __init__(self,name,models=None):
        self.name=name
        self.models=models or 'empty'

    def foo(self):
        print self.name
        print self.models

class B(A):
    def __init__(self,models):
        super(B,self).__init__(name=None,models=None)
        self.models = 'not empty'

a=A('1')
a.foo()
b=B('2')
b.foo()
