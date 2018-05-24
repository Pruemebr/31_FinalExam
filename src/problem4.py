"""
Final exam, problem 4.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Bryce Pruemer.  May 2018.

"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
# TODO: 2.
#   In this problem, you will go through the methods of the  Pig  class
#   that is defined below, one by one, in the order that they appear.
#   For each method:
#      (a) Read the method's doc-string (i.e., specification in double-quotes).
#            If you do not understand WHAT the method is to do,
#            ask your instructor to clarify it.
#      (b) Implement the method.
#      (c) Write at least SOME code  in  main  that tests your code.
#
###############################################################################

def main():
    porky = Pig(100)
    print(porky.get_weight())
    porky.eat(50)
    print(porky.get_weight())
    porky.eat_for_a_year()
    print(porky.get_weight())

    second_pig = Pig(100)
    porky.heavier_pig(second_pig)
    best_pig = porky.new_pig(second_pig)
    print('reached')
    print(best_pig.get_weight())

    """ Tests the  Pig  class. """
    # -------------------------------------------------------------------------
    # WRITE CODE HERE AS NEEDED to TEST the code that you write
    #   in the  Pig  class.  At the least, you must:
    #     -- Construct two Pig objects
    #     -- Call each method that you implement below.
    # -------------------------------------------------------------------------


class Pig(object):
    def __init__(self, weight):
        """
        What comes in:  The Pig's weight (in pounds).
        Side effects: Sets instance variables as needed by the other methods.
        """
        self.weight = weight
        # DONE: Implement and test this method.

    def get_weight(self):
        """ Returns this Pig's weight. """
        return self.weight
        # DONE: Implement and test this method.

    def eat(self, pounds_of_slop):
        """
        Increments this Pig's weight by the given pounds_of_slop.
        """
        self.weight = self.weight + pounds_of_slop
        # DONE: Implement and test this method.

    def eat_for_a_year(self):
        for k in range(1,366):
            self.eat(k)
        """
        Calls the   eat   method as many times as needed to make this Pig:
          -- eat 1 pound of slop, then
          -- eat 2 pounds of slop, then
          -- eat 3 pounds of slop, the
          -- eat ... [4 pounds, then 5, then 6, then ... ]
          -- eat 364 pounds of slop, then
          -- eat 365 pounds of slop.
        """
        # DONE: Implement and test this method.

    def heavier_pig(self, other_pig):
        """
        Returns either this Pig object or the other given Pig object,
        whichever is heavier.
        """
        if self.weight > other_pig.weight:
            return self
        else:
            return other_pig
        # DONE: Implement and test this method.

    def new_pig(self, other_pig):
        """
        Returns a new Pig whose weight is the weight of the heavier
          of this Pig and the other_Pig.
        """
        new_pig = Pig(self.heavier_pig(other_pig).get_weight())
        return new_pig
        # DONE: Implement and test this method.


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
