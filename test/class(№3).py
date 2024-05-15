import math

class Point():

    def __init__(self, abscissa, ordinate):
        self.abscissa = abscissa
        self.ordinate = ordinate

    def distance(self, abscissa, ordinate):

        return math.sqrt((self.ordinate - ordinate)**2 + (self.abscissa - abscissa)**2)

    def change_coord(self, abscissa, ordinate):
        self.abscissa = abscissa
        self.ordinate = ordinate

    def info(self):
        return (self.abscissa, self.ordinate)





