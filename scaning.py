# -- coding: utf-8 --
class scaning(object):

    def __init__(self,direction,verb,stop,noun,number):
        self.direction=direction
        self.verb=verb
        self.stop=stop
        self.noun=noun
        self.number=number
        

    def scan(self,status):
        l=[]
        words=status.split()
		
        for i in words:
            try :
                int(i)
                l.append(('number',i))#l=l.append(),则l为None.()里的对象视为元素，不加方括号
            except ValueError:
                if i in self.direction:
                    l.append(('direction',i))
                elif i in self.verb:
                    l.append(('verb',i))
                elif i in self.stop:
                    l.append(('stop',i))
                elif i in self.noun:
                    l.append(('noun',i))
                else:
                    l.append(('Error',i))

        return l
                
lexicon=scaning(['north','south','east','west','down','up','left','right','back'],
                ['go','stop','kill','eat'],
                ['the','in','of','from','at','it'],
                ['door','bear','princess','cabinet'],
                range(0,10))
#需要先实例化否则将会报错：未绑定的方法对象需传递一个实例
