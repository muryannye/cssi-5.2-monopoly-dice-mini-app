import random #imports random library.

#Write your monopoly dice roller app here!
#You can make use of random.randint()
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
total = dice1 + dice2
if dice1 == dice2:
    print "Doubles! Move %d spaces and roll again." % (total)
else:
    print "Move %d spaces. Next player's turn!" % (total)
