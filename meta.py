'''def to_index(name,parent,attr):
    new_attr = {}
    for key,value in attr.items():
        index = attr.keys().index(key)
        new_attr['attr'+str(index)] = value
    return type(name,parent,new_attr)

__metaclass__ = to_index

class A():
    a=1
    b=2
    c=3'''

class IndexMetaClass(type):

    def __new__(cls,name,parent,attr):

        new_attr = {}

        for key,value in attr.items():
            index=attr.keys().index(key)
            new_attr['x'+str(index)]=value

        return super(IndexMetaClass,cls).__new__(cls,name,parent,new_attr)

