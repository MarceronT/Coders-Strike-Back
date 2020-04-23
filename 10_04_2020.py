import sys
import math

# This code automatically collects game data in an infinite loop.
# It uses the standard input to place data into the game variables such as x and y.
# YOU DO NOT NEED TO MODIFY THE INITIALIZATION OF THE GAME VARIABLES.


# game loop
hasBoost = True
var_angle = 1
r = 600

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

    if var_angle == 1 and y > next_checkpoint_y:
        alpha = math.acos((x - next_checkpoint_x) / nextCheckpointDist)
        teta = alpha
        var_angle = 0
    elif var_angle == 1 and y < next_checkpoint_y:
        alpha = math.acos((x - next_checkpoint_x) / nextCheckpointDist)
        teta = -alpha
        var_angle = 0
    if nextCheckpointDist < 1200:
        var_angle = 1
    else:
        Nextpoint_x = r * (math.cos(teta))
        Nextpoint_y = r * (math.sin(teta))
        next_checkpoint_x = round(next_checkpoint_x + Nextpoint_x)
        next_checkpoint_y = round(next_checkpoint_y + Nextpoint_y)

    if abs(nextCheckpointAngle) >= 80:
        thrust = 10
    else:
        thrust = 100
    if hasBoost == True and nextCheckpointDist > 5000 and abs(nextCheckpointAngle) <= 2:
        thrust = "BOOST"
        hasBoost = False
    # and thrust (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(thrust))
    debug(nextCheckpointDist, nextCheckpointAngle)
    debug(X, Y)
    debug(math.degrees(alpha))
