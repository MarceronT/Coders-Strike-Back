import sys
import math


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

    # Edit this line to output the target position
    if nextCheckpointAngle > 90 or nextCheckpointAngle < -90:
        thrust = 0
    else:
        thrust = "BOOST"
    # and thrust (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(thrust))

