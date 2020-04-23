import sys
import math

# This code automatically collects game data in an infinite loop.
# It uses the standard input to place data into the game variables such as x and y.
# YOU DO NOT NEED TO MODIFY THE INITIALIZATION OF THE GAME VARIABLES.


# game loop
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
    nextCheckpointDistOpponent_Adjc = math.sqrt(
        ((next_checkpoint_x - opponentX) ** 2) + ((opponentY - opponentY) ** 2)
    )
    nextCheckpointAngleOpponent = math.acos(
        abs(nextCheckpointDistOpponent_Adjc) / (nextCheckpointDistOpponent)
    )
    DistBetweenShip = math.sqrt(((opponentX - x) ** 2) + ((opponentY - y) ** 2))
    # Edit this line to output the target position
    if nextCheckpointAngle > 90 or nextCheckpointAngle < -90:
        thrust = 40
    elif 1000 <= nextCheckpointDist <= 1500:
        thrust = 40
    elif 90 >= abs(nextCheckpointAngle) >= 60:
        thrust = 84
    elif 60 >= abs(nextCheckpointAngle) >= 40:
        thrust = 88
    elif 40 >= abs(nextCheckpointAngle) >= 30:
        thrust = 92
    elif 30 >= abs(nextCheckpointAngle) >= 20:
        thrust = 96
    elif 10 >= abs(nextCheckpointAngle) and nextCheckpointDist < 3500:
        thrust = 90
    else:
        thrust = 100
    if nextCheckpointDist >= 6000 and abs(nextCheckpointAngle) <= 25:
        thrust = "BOOST"
    elif DistBetweenShip <= 900:
        next_checkpoint_x = opponentX
        next_checkpoint_y = opponentY
        thrust = "BOOST"

    # and thrust (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(thrust))
    debug(nextCheckpointDist, nextCheckpointAngle)
    debug(nextCheckpointDistOpponent, math.degrees(nextCheckpointAngleOpponent))
    debug(DistBetweenShip)
