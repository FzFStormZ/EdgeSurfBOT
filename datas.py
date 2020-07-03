avoid = 300 # black detect (can be change to up or down sensitivity)
earn = 300 # green detect (can be change to up or down sensitivity)
timeToEnergy = 30 # to avoid run energy command too early
timeToAvoidMonster = 45 # reset position of the surfer easier to detect monster behind him
lastControl = ''

class colors():

    # different colors used in games to know what the surfer do
    red = (255, 0, 0)
    green = (0, 255, 0)
    black = (0, 0, 0)
    blue = (0, 0, 255)
    sandcolor = (211, 230, 201)

class boxs():

    # coordinates of the black box of the surfer (not use, just use to test)
    black_box = (467, 462, 493, 488)

    # coordinates of the box around the surfer (not use, just use to test)
    box_around_surfer = (243, 371, 718, 584)

    # coordinates of the box behind the surfer (to avoid monster or other surfers)
    # box_behind = (431, 374, 535, 462) --> old coordinates
    box_behind = (380, 365, 580, 455)

    # coordinates of the left box of the surfer
    # box_left = (264, 490, 435, 586) --> old coordinates
    box_left = (245, 520, 410, 620)

    # coordinates of the right box of the surfer
    # box_right = (526, 490, 700, 586) --> old coordinates
    box_right = (550, 520, 720, 620)

    # coordinates of the box front of the surfer
    # box_front = (441, 490, 516, 586) --> old coordinates
    box_front = (440, 520, 520, 620)

    # coordinates of the box to avoid large obstacle
    # box_snipe = (350, 690, 610, 720) --> old coordinates
    box_snipe = (350, 690, 610, 750)

    # coordinates of the box to know if we have a boost or not
    box_energy = (550, 93, 630, 123)