import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

coor_Checkpoint = []
pods = []
t = 0

laps = int(input())
checkpoint_count = int(input())
for i in range(checkpoint_count):
    checkpoint_x, checkpoint_y = [int(j) for j in input().split()]
    checkpoint = [checkpoint_x, checkpoint_y]
    coor_Checkpoint.append(checkpoint)

var_angle = 1
r = 600
boost = True
# game loop
while True:
    for i in range(2):
        # x: x position of your pod
        # y: y position of your pod
        # vx: x speed of your pod
        # vy: y speed of your pod
        # angle: angle of your pod
        # next_check_point_id: next check point id of your pod
        x, y, vx, vy, angle, next_check_point_id = [int(j) for j in input().split()]
        data = [x, y, next_check_point_id, angle]
        pods.append(data)

    for i in range(2):
        # x_2: x position of the opponent's pod
        # y_2: y position of the opponent's pod
        # vx_2: x speed of the opponent's pod
        # vy_2: y speed of the opponent's pod
        # angle_2: angle of the opponent's pod
        # next_check_point_id_2: next check point id of the opponent's pod
        x_2, y_2, vx_2, vy_2, angle_2, next_check_point_id_2 = [
            int(j) for j in input().split()
        ]
    """
    PODS 1
    """

    x_pod_1 = pods[t][0]
    y_pod_1 = pods[t][1]
    number_cp_id_pod_1 = pods[t][2]
    angles_pod_1 = pods[t][3]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr
    for i in range(len(coor_Checkpoint)):
        if number_cp_id_pod_1 == i:
            nextCheckpointDist = math.sqrt(
                (coor_Checkpoint[i][0] - x_pod_1) ** 2
                + (coor_Checkpoint[i][1] - y_pod_1) ** 2
            )
            if var_angle == 1 and y_pod_1 > coor_Checkpoint[i][1]:
                alpha = math.acos(
                    (x_pod_1 - coor_Checkpoint[i][0]) / nextCheckpointDist
                )
                teta = alpha
                var_angle = 0
            elif var_angle == 1 and y_pod_1 < coor_Checkpoint[i][1]:
                alpha = math.acos(
                    (x_pod_1 - coor_Checkpoint[i][0]) / nextCheckpointDist
                )
                teta = -alpha
                var_angle = 0
            if nextCheckpointDist < 1200:
                var_angle = 1
            else:
                Nextpoint_x = r * (math.cos(teta))
                Nextpoint_y = r * (math.sin(teta))
                checkpoint_x = round(coor_Checkpoint[i][0] + Nextpoint_x)
                checkpoint_y = round(coor_Checkpoint[i][1] + Nextpoint_y)
    t = t + 2
    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_check_point_id), file=sys.stderr)
    print(circuit, file=sys.stderr)
    print(str(nextCheckpointDist), file=sys.stderr)
    print(str(checkpoint_x), str(checkpoint_y), "100")
    print(str(x_2), str(y_2), "100")
