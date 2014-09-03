class Point:
    def __init__(self, x, y, z):
        self.coord = (x, y, z)
    def __repr__(self):
        return "Point (%s,%s, %s)" % self.coord

#second class Line
class Line:
    def __init__(self, p1, p2):
        self.line = (p1, p2)

    def __del__(self):
        print "Видаляється лінія %s - %s" % self.line
