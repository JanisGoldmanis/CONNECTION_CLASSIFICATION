import rules
from skspatial.objects import Point, Line
import geometry_calculation


def FirstIsHCS(connection, list_dict):
    hcs_profiles = list_dict['hcs_profiles']
    if connection.part2.profile in hcs_profiles and connection.part1.profile not in hcs_profiles:
        connection.part1, connection.part2 = connection.part2, connection.part1
        swap_plane_information_when_sorting(connection)
        return True


def FirstIsVertical(connection, list_dict):
    if rules.PartIsVertical(connection, {"Part": "part2"}, {}, {}):
        connection.part1, connection.part2 = connection.part2, connection.part1
        swap_plane_information_when_sorting(connection)
        return True


def BottomFirst(connection, list_dict):
    part1 = connection.part1
    part2 = connection.part2

    if part2.cog_z < part1.cog_z:
        connection.part1, connection.part2 = connection.part2, connection.part1
        swap_plane_information_when_sorting(connection)
        return True


def ClosestEndPointFirst(connection, list_dict):
    part1 = connection.part1
    part2 = connection.part2

    part1_endpoint = part1.points[1]
    part2_endpoint = part2.points[1]

    connection_start = geometry_calculation.get_point_list_from_string(connection.connection_start)
    connection_end = geometry_calculation.get_point_list_from_string(connection.connection_end)

    line = Line.from_points(connection_start[0], connection_end[0])

    distance1 = geometry_calculation.get_distance_to_line(line, part1_endpoint)
    distance2 = geometry_calculation.get_distance_to_line(line, part2_endpoint)

    if distance2 < distance1:
        connection.part1, connection.part2 = connection.part2, connection.part1
        swap_plane_information_when_sorting(connection)
        return True


def swap_plane_information_when_sorting(connection):

    connection.plane1_x_start, connection.plane2_x_start = connection.plane2_x_start, connection.plane1_x_start
    connection.plane1_x_overlap, connection.plane2_x_overlap = connection.plane2_x_overlap, connection.plane1_x_overlap
    connection.plane1_x_end, connection.plane2_x_end = connection.plane2_x_end, connection.plane1_x_end

    connection.plane1_y_start, connection.plane2_y_start = connection.plane2_y_start, connection.plane1_y_start
    connection.plane1_y_overlap, connection.plane2_y_overlap = connection.plane2_y_overlap, connection.plane1_y_overlap
    connection.plane1_y_end, connection.plane2_y_end = connection.plane2_y_end, connection.plane1_y_end

    connection.plane1_z_start, connection.plane2_z_start = connection.plane2_z_start, connection.plane1_z_start
    connection.plane1_z_overlap, connection.plane2_z_overlap = connection.plane2_z_overlap, connection.plane1_z_overlap
    connection.plane1_z_end, connection.plane2_z_end = connection.plane2_z_end, connection.plane1_z_end

    connection.part1_endpoint_distance, connection.part2_endpoint_distance = connection.part2_endpoint_distance, connection.part1_endpoint_distance
