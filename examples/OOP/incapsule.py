<<<<<<< HEAD
#
class parent(object):
    def __init__(self):
        self.__f = 2
    def get(self):
        return self.__f

#
class child(parent):
    def __init__(self):
        self.__f = 1
        parent.__init__(self)
    def cget(self):
        return self.__f

    
=======
#
class parent(object):
    def __init__(self):
        self.__f = 2
    def get(self):
        return self.__f

#
class child(parent):
    def __init__(self):
        self.__f = 1
        parent.__init__(self)
    def cget(self):
        return self.__f

    
>>>>>>> 58c3053a3dcbb951d0bcfaf1043902fc235ecc6d
