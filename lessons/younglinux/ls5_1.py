class One(object):
    def __init__(self, a):
        self.a = a**2
        print self.a

class Two(object):
    def __init__(self, a):
        self.a = a * 2
        print self.a

a = int(input("Istert number! "))

if -100 < a < 100:
    ob = One(a)
else:
    ob = Two(a)


 
