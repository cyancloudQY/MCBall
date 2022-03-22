import random
import math


def parse_input_file(file_name):
    ball_info_file = open(file_name, 'r')
    lines = ball_info_file.readlines()
    info_list = []
    for line in lines:
        list_of_words = line.split()
        info_list.append(list_of_words)
    ball_number = info_list[0]
    info_list.pop(0)

    for i in range(len(info_list)):
        for j in range(len(info_list[i])):
            # noinspection PyTypeChecker
            info_list[i][j] = float(info_list[i][j])

    return info_list, ball_number


def project_points(background_info, n_points):
    """
    :param:  Provide the Framework in X-axis Length, Y-axis Length, Z-Length, Number of Points
    :return: A list with the coordinates of the points in [[x,y,z],[x,y,z],[x,y,z],...] form, and length should be
             equal to the number of points
    """
    coordinates = []
    for i in range(n_points):
        a = []  # Initialize the moment coordinate
        x = random.uniform(background_info[0], background_info[1])
        a.append(x)
        y = random.uniform(background_info[2], background_info[3])
        a.append(y)
        z = random.uniform(background_info[4], background_info[5])
        a.append(z)
        coordinates.append(a)

    return coordinates


def distance_calculator(coordinate1, coordinate2):
    """
    :param :  two coordinates in list form [x1,y1,z1]  [x2,y2,z2]
    :return:  the distance between the two points
    """

    distance = math.sqrt((coordinate1[0] - coordinate2[0]) ** 2 + (coordinate1[1] - coordinate2[1]) ** 2
                         + ((coordinate1[2] - coordinate2[2]) ** 2))
    return distance


def find_optimal_background(ball_info):
    """
    Find the background framework that fits the units of balls most
    Use the max/min axis value add or subtract the r_max to include all balls
    """
    r_max = max([i[3] for i in ball_info])
    x_min = min([i[0] for i in ball_info]) - r_max
    x_max = max([i[0] for i in ball_info]) + r_max
    y_min = min([i[1] for i in ball_info]) - r_max
    y_max = max([i[1] for i in ball_info]) + r_max
    z_min = min([i[2] for i in ball_info]) - r_max
    z_max = max([i[2] for i in ball_info]) + r_max
    background_info = [x_min, x_max, y_min, y_max, z_min, z_max]
    return background_info


def judge_inside_ball(point_info, ball_info):
    distance = distance_calculator(point_info, ball_info[:3])
    if distance <= ball_info[3]:
        return True
    else:
        return False


def Monte_Carlo_technique(ball_info, background_info, num_points):
    volume = 0
    points = project_points(background_info, num_points)
    a = 0
    print('Give me some time...')
    for i in points:
        result_list = []
        for j in ball_info:
            result = judge_inside_ball(i, j)
            result_list.append(result)
        if True in result_list:
            volume += 1

        a += 1


    volume_total = (background_info[1] - background_info[0]) * (background_info[3] - background_info[2]) \
                   * (background_info[5] - background_info[4])

    volume_balls = float(volume) / num_points * volume_total

    return volume_balls



