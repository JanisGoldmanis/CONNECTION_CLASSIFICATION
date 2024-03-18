import geometry_calculation
import part


class Connection:
    def __init__(self,
                 connection_id,
                 guid1, guid2,
                 profile1, profile2,
                 material1, material2,
                 class1, class2,
                 angle_XX, angle_XY, angle_XZ,
                 angle_YX, angle_YY, angle_YZ,
                 angle_ZX, angle_ZY, angle_ZZ,
                 part1_tekla_width, part2_tekla_width,
                 part1_tekla_height, part2_tekla_height,
                 part1_tekla_length, part2_tekla_length,
                 part1_points, part2_points,
                 connection_start, connection_end,
                 cog_1, cog_2,
                 plane1_x_start, plane1_x_overlap, plane1_x_end,
                 plane1_y_start, plane1_y_overlap, plane1_y_end,
                 plane1_z_start, plane1_z_overlap, plane1_z_end,
                 plane2_x_start, plane2_x_overlap, plane2_x_end,
                 plane2_y_start, plane2_y_overlap, plane2_y_end,
                 plane2_z_start, plane2_z_overlap, plane2_z_end,
                 global_z_bottom, global_z_overlap, global_z_top
                 ):
        self.part1 = part.Part(guid1, profile1, material1, class1,
                               part1_tekla_width, part1_tekla_length, part1_tekla_height, part1_points, cog_1)
        self.part2 = part.Part(guid2, profile2, material2, class2,
                               part2_tekla_width, part2_tekla_length, part2_tekla_height, part2_points, cog_2)

        self.angle_XX = float(angle_XX)
        self.angle_XY = float(angle_XY)
        self.angle_XZ = float(angle_XZ)
        self.angle_YX = float(angle_YX)
        self.angle_YY = float(angle_YY)
        self.angle_YZ = float(angle_YZ)
        self.angle_ZX = float(angle_ZX)
        self.angle_ZY = float(angle_ZY)
        self.angle_ZZ = float(angle_ZZ)

        self.plane1_x_start = round(float(plane1_x_start), 1)
        self.plane1_x_overlap = round(float(plane1_x_overlap), 1)
        self.plane1_x_end = round(float(plane1_x_end), 1)

        self.plane1_y_start = round(float(plane1_y_start), 1)
        self.plane1_y_overlap = round(float(plane1_y_overlap), 1)
        self.plane1_y_end = round(float(plane1_y_end), 1)

        self.plane1_z_start = round(float(plane1_z_start), 1)
        self.plane1_z_overlap = round(float(plane1_z_overlap), 1)
        self.plane1_z_end = round(float(plane1_z_end), 1)

        self.plane2_x_start = round(float(plane2_x_start), 1)
        self.plane2_x_overlap = round(float(plane2_x_overlap), 1)
        self.plane2_x_end = round(float(plane2_x_end), 1)

        self.plane2_y_start = round(float(plane2_y_start), 1)
        self.plane2_y_overlap = round(float(plane2_y_overlap), 1)
        self.plane2_y_end = round(float(plane2_y_end), 1)

        self.plane2_z_start = round(float(plane2_z_start), 1)
        self.plane2_z_overlap = round(float(plane2_z_overlap), 1)
        self.plane2_z_end = round(float(plane2_z_end), 1)

        self.global_z_bottom = round(float(global_z_bottom), 1)
        self.global_z_overlap = round(float(global_z_overlap), 1)
        self.global_z_top = round(float(global_z_top), 1)

        self.connection_id = connection_id
        self.part_guids = f'{self.part1.guid} {self.part2.guid}'

        if self.part1.points is not None and self.part2.points is not None:
            self.part1_endpoint_distance = geometry_calculation.get_endpoint_distance(self.part2, self.part1)
            self.part2_endpoint_distance = geometry_calculation.get_endpoint_distance(self.part1, self.part2)
        self.connection_start = connection_start
        self.connection_end = connection_end
        self.connection_type = ""
