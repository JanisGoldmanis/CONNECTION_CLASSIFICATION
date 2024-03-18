import numpy as np
from skspatial.objects import Point, Line


def get_distance_to_line(line, point):
    distance = line.distance_point(point)
    return distance


def get_point_list_from_string(point_string):
    points = point_string.replace('{','').replace('}','').split('|')
    result = []
    try:
        for point in points:
            coordinates = [float(coordinate.rstrip()) for coordinate in point.split(',')]
            result.append(Point(coordinates))
        return result
    except:
        return None


def get_endpoint_distance(part1, part2):

    line = Line.from_points(part1.points[0], part1.points[1])
    distance1 = line.distance_point(part2.points[0])
    distance2 = line.distance_point(part2.points[1])

    return min(distance1, distance2)