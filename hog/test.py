import hog
always_one = hog.make_test_dice(1)
always_two = hog.make_test_dice(2)
always_three = hog.make_test_dice(3)
always = hog.always_roll
# swap after feral hogs
s0, s1 = hog.play(always(2), always(1), score0=17, score1=6, goal=21, dice=hog.make_test_dice(1, 2))
