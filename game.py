from sys import exit

def gold_room():
    print 'This room is full of gold, how much do you want?'

    nex=raw_input('...')
    if '0' in nex or '1' in nex:
        #if you type 3 or 4 or something else you die
        how_much=int(nex)
    else:
        dead('type a number!!')

    if how_much<500:
        print 'Good guy,you are not greedy,you win!'
        exit(0)
    else:
        dead('You die of greedy!')

def bear_room():
    print '''There is a bear here
The bear has a bunch of honey
The fat bear is in front of another door
How are you going to moving the bear?'''
    bear_moved=False

    while True:
        nex = raw_input('...')

        if nex == 'take honey':
            dead('The bear looks at you then slaps your face off')
        elif nex == 'taunt bear' and not bear_moved:
            print 'The bear moved from the door.You can go through it now'
            bear_moved=True
        elif nex == 'taunt bear' and bear_moved:
            dead ('The bear gets pissed off and chews your legs off')
        elif nex == 'open door' and bear_moved:
            gold_room()
        else:
            print 'WHAT DOES IT MEAN?'
def Devil_room():
    print 'Here you see the great Devil\nHe,it, whatever stares at you and you go insane.\nDo you flee for your life or eat your head?'

    nex =raw_input('...')

    if 'flee'in nex:
        start()
    elif 'head' in nex:
        dead('That\'s tasty!')
    else:
        Devil_room()

def dead(why):
    print why,'Game over!'
    exit(0)

def start():
    print 'You are in a dark room'
    print 'There is a door to your left and right'
    print 'Which one do you take?'

    nex =raw_input ('...')

    if nex == 'left':
        bear_room()
    elif nex == 'right':
        Devil_room()
    else:
        dead('You stumble around the room until you starve')
