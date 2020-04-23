import sys
import math

# This code automatically collects game data in an infinite loop.
# It uses the standard input to place data into the game variables such as x and y.
# YOU DO NOT NEED TO MODIFY THE INITIALIZATION OF THE GAME VARIABLES.


# game loop
hasBoost = True


def moveX():
    beforeX = x
    return beforeX


def moveY():
    beforeY = y
    return beforeY


def decisionNextMove():
    destinationX = next_checkpoint_x
    destinationY = (next_checkpoint_y,)
    force = 100
    rad = math.radians(nextCheckpointAngle)
    if nextCheckpointAngle < 90:
        perfectforce = nextCheckpointDist * (math.cos(rad) * 0.15)
        if perfectforce > 100:
            force = 100
        elif perfectforce < 0:
            force = 0
        else:
            force = perfectforce
    else:
        force = 0
    thrust = force
    return thrust


def log():
    moved = math.sqrt(math.pow(x - (moveX()), 2) + math.pow((y - (moveY())), 2))
    print("Debug Messages : x = " + str(x) + ", y = " + str(y), file=sys.stderr)
    print("Debug Messages : moved = " + str(moved), file=sys.stderr)
    print("Debug Messages : Angle = " + str(nextCheckpointAngle), file=sys.stderr)


while True:
    # x: x position of your pod
    # y: y position of your pod
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    (
        x,
        y,
        next_checkpoint_x,
        next_checkpoint_y,
        nextCheckpointDist,
        nextCheckpointAngle,
    ) = [int(i) for i in input().split()]
    opponentX, opponentY = [int(i) for i in input().split()]
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    def debug(*args, **kwargs):
        print(*args, **kwargs, file=sys.stderr)

    nextCheckpointDistOpponent = math.sqrt(
        ((next_checkpoint_x - opponentX) ** 2) + ((next_checkpoint_y - opponentY) ** 2)
    )
    X = next_checkpoint_x - x
    Y = next_checkpoint_y - y
    if X < 0 and Y < 0:
        Nextpoint_x = 200 * (math.cos(math.pi / 4))
        Nextpoint_y = 200 * (math.sin(math.pi / 4))
        next_checkpoint_x = round(next_checkpoint_x + Nextpoint_x)
        next_checkpoint_y = round(next_checkpoint_y + Nextpoint_y)
    elif X > 0 and Y < 0:
        Nextpoint_x = 200 * (math.cos((3 * math.pi) / 4))
        Nextpoint_y = 200 * (math.sin((3 * math.pi) / 4))
        next_checkpoint_x = round(next_checkpoint_x + Nextpoint_x)
        next_checkpoint_y = round(next_checkpoint_y + Nextpoint_y)
    elif X > 0 and Y > 0:
        Nextpoint_x = 200 * (math.cos((-3 * math.pi) / 4))
        Nextpoint_y = 300 * (math.sin((-3 * math.pi) / 4))
        next_checkpoint_x = round(next_checkpoint_x + Nextpoint_x)
        next_checkpoint_y = round(next_checkpoint_y + Nextpoint_y)
    elif X < 0 and Y > 0:
        Nextpoint_x = 200 * (math.cos(-math.pi / 4))
        Nextpoint_y = 200 * (math.sin(-math.pi / 4))
        next_checkpoint_x = round(next_checkpoint_x + Nextpoint_x)
        next_checkpoint_y = round(next_checkpoint_y + Nextpoint_y)
    log()
    thrust = round(decisionNextMove())
    if hasBoost == True and nextCheckpointDist > 4500 and nextCheckpointAngle == 0:
        thrust = "BOOST"
        hasBoost = False

    moveX()
    moveY()
    # and thrust (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(thrust))
    debug(nextCheckpointDist, nextCheckpointAngle)
