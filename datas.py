avoid = 300 # black detect (can be change to up or down sensitivity)
earn = 300 # green detect (can be change to up or down sensitivity)

class colors():

    # different colors used in games to know what the surfer do
    red = (255, 0, 0)
    green = (0, 255, 0)
    black = (0, 0, 0)
    blue = (0, 0, 255)

class boxs():

    # coordinates of the black box of the surfer (not use, just use to test)
    black_box = (467, 462, 493, 488)

    # coordinates of the box around the surfer (not use, just use to test)
    box_around_surfer = (243, 371, 718, 584)

    # coordinates of the box behind the surfer (to avoid monster or other surfers)
    box_behind = (431, 374, 535, 462)

    # coordinates of the left box of the surfer
    box_left = (264, 490, 435, 586)

    # coordinates of the right box of the surfer
    box_right = (426, 490, 700, 586)

    # coordinates of the box front of the surfer
    box_front = (441, 490, 516, 586)