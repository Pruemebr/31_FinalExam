"""
Final exam, problem 3.

Authors: David Mutchler, Dave Fisher, Matt Boutell, their colleagues,
         and Bryce Pruemer.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_shape()


def run_test_shape():
    """ Tests the    shape    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   SHAPE   function:')
    print('--------------------------------------------------')

    print()
    print('Test 1 of shape: n=5')
    shape(5)

    print()
    print('Test 2 of shape: n=3')
    shape(3)

    print()
    print('Test 3 of shape: n=14')
    shape(14)


def shape(n):
    ####################################################################
    # IMPORTANT: In solving this problem,
    #   You must NOT use string multiplication.
    ####################################################################
    """
    Prints a shape with numbers on the left side of the shape,
    other numbers on the right side of the shape,
    and stars in the middle,per the pattern in the examples below.
    When the pattern calls for a number with more than one digit,
    just use the last (rightmost) digit when you print that number.

    It looks like this example for n=5:
    1 ** 54321
   12 *** 4321
  123 **** 321
 1234 ***** 21
12345 ****** 1

    And this one for n=3:
  1 ** 321
 12 *** 21
123 **** 1


And this one for n=14:
             1 ** 43210987654321
            12 *** 3210987654321
           123 **** 210987654321
          1234 ***** 10987654321
         12345 ****** 0987654321
        123456 ******* 987654321
       1234567 ******** 87654321
      12345678 ********* 7654321
     123456789 ********** 654321
    1234567890 *********** 54321
   12345678901 ************ 4321
  123456789012 ************* 321
 1234567890123 ************** 21
12345678901234 *************** 1

    :type n: int
    """
    backgroup = ''
    for z in range(n, 0, -1): #Creates the initial row of the backwards group of numbers
        if z >= 10:
            z = z - 10
        backgroup = backgroup + str(z)
    print(backgroup)

    num = n
    row = ''
    val = 2
    group = '1'
    starstr = '**'
    for o in range(n):
        for k in range(num, 1, -1):
            row = row + ' ' #After this, you will have one row's worth of spaces
        num = num - 1 #number of spaces, setting up for next time around
        row = row + group
        group = group + str(val) #Adding the next number to group for the next go around
        if val == 9:
            val = 0
        val = val + 1
        row = row + ' '
        row = row + starstr
        starstr = starstr + '*'
        row = row + ' '
        row = row + backgroup
        temp = backgroup
        backgroup = '' #empties out backgroup to use again
        sizebg = len(temp)
        for g in range(1, sizebg):
            backgroup = backgroup + temp[g]
        #backgroup should now be reset with the front number missing

        print(row)
        row = ''

    # leftstr = ''
    # stars = '**'
    # holder = []
    # hvar2 = 0
    # spacecount = n
    #
    # for hvar in range(n):
    #     holder.append('')
    #     for var in range(spacecount, 0, -1):
    #         holder[1].append('')
    #     spacecount = spacecount - 1
    #
    #
    #
    # for k in range(1,n+1):
    #     if k >= 10:
    #         k = k - 10
    #     leftstr =leftstr + str(k)
    #     holder[hvar2]=holder[hvar2] + (leftstr)
    #     hvar2 = hvar2 + 1
    #
    #
    # for s in range(len(holder)):
    #     holder[s] = holder[s] + ''
    #
    # # for count in range(len(holder)):
    # #     holder[count] = holder[count] + stars
    # #     stars = stars + '*'
    #
    # for p in range(len(holder)):
    #     print(holder[p])






    # ------------------------------------------------------------------
    # TODO: Implement and test this function.
    #          Some tests are already written for you (above).
    ####################################################################
    # IMPORTANT: In solving this problem,
    #   You must NOT use string multiplication.
    ####################################################################
    #
    # HINT:
    #   If you're having trouble with the spaces on the left,
    #   print Xs for the spaces until you figure out where the problem is
    #   (and then change the Xs back to spaces).
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
