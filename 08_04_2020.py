import sys
import math

# This code automatically collects game data in an infinite loop.
# It uses the standard input to place data into the game variables such as x and y.
# YOU DO NOT NEED TO MODIFY THE INITIALIZATION OF THE GAME VARIABLES.


# game loop
hasBoost = True
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
    alpha = math.acos((x - next_checkpoint_x) / nextCheckpointDist)
    X = next_checkpoint_x - x
    Y = next_checkpoint_y - y

    if X < 0 and Y < 0 and nextCheckpointDist < 4000:
        Nextpoint_x = r * (math.cos(alpha))
        Nextpoint_y = r * (math.sin(alpha))
        next_checkpoint_x = round(next_checkpoint_x + Nextpoint_x)
        next_checkpoint_y = round(next_checkpoint_y + Nextpoint_y)
    elif X < 0 and Y < 0 and nextCheckpointDist > 4000:
        Nextpoint_x = r * (math.cos(alpha - (math.pi)))
        Nextpoint_y = r * (math.sin(alpha - (math.pi)))
        next_checkpoint_x = round(next_checkpoint_x + Nextpoint_x)
        next_checkpoint_y = round(next_checkpoint_y + Nextpoint_y)

    if X > 0 and Y < 0 and nextCheckpointDist < 4000:
        Nextpoint_x = r * (math.cos(alpha))
        Nextpoint_y = r * (math.sin(alpha))
        next_checkpoint_x = round(next_checkpoint_x + Nextpoint_x)
        next_checkpoint_y = round(next_checkpoint_y + Nextpoint_y)
    elif X > 0 and Y < 0 and nextCheckpointDist > 4000:
        Nextpoint_x = r * (math.cos(alpha - (math.pi)))
        Nextpoint_y = r * (math.sin(alpha - (math.pi)))
        next_checkpoint_x = round(next_checkpoint_x + Nextpoint_x)
        next_checkpoint_y = round(next_checkpoint_y + Nextpoint_y)

    if X > 0 and Y > 0 and nextCheckpointDist < 4000:
        Nextpoint_x = r * (math.cos(-alpha))
        Nextpoint_y = r * (math.sin(-alpha))
        next_checkpoint_x = round(next_checkpoint_x + Nextpoint_x)
        next_checkpoint_y = round(next_checkpoint_y + Nextpoint_y)
    elif X > 0 and Y > 0 and nextCheckpointDist > 4000:
        Nextpoint_x = r * (math.cos(alpha - (math.pi)))
        Nextpoint_y = r * (math.sin(alpha - (math.pi)))
        next_checkpoint_x = round(next_checkpoint_x + Nextpoint_x)
        next_checkpoint_y = round(next_checkpoint_y + Nextpoint_y)

    if X < 0 and Y > 0 and nextCheckpointDist < 4000:
        Nextpoint_x = r * (math.cos(-alpha))
        Nextpoint_y = r * (math.sin(-alpha))
        next_checkpoiny_x = round(next_checkpoint_x + Nextpoint_x)
        next_checkpoint_y = round(next_checkpoint_y + Nextpoint_y)
    elif X < 0 and Y > 0 and nextCheckpointDist > 4000:
        Nextpoint_x = r * (math.cos(alpha - (math.pi)))
        Nextpoint_y = r * (math.sin(alpha - (math.pi)))
        next_checkpoint_x = round(next_checkpoint_x + Nextpoint_x)
        next_checkpoint_y = round(next_checkpoint_y + Nextpoint_y)

    dist = math.sqrt(
        ((next_checkpoint_x + Nextpoint_x) - x) ** 2
        + ((next_checkpoint_y + Nextpoint_y) - y) ** 2
    )
    if abs(nextCheckpointAngle) <= 150:
        thrust = round(100 * (1 - (abs(nextCheckpointAngle) / 150)))
    elif abs(nextCheckpointAngle) >= 150:
        thrust = 0
    if dist < 600:
        thrust = 70
    if hasBoost == True and dist > 4500 and abs(nextCheckpointAngle) <= 5:
        thrust = "BOOST"
        hasBoost = False
    # and thrust (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(thrust))
    debug(nextCheckpointDist, nextCheckpointAngle)
    debug(X, Y)
    debug(nextCheckpointDist, dist)
    debug(math.degrees(alpha), nextCheckpointDistOpponent)
