import geometry_calculation

class Part:
    def __init__(self, guid, profile, material, tekla_class, width, length, height, points, cog):
        self.guid = guid
        self.profile = profile
        self.material = material
        self.tekla_class = tekla_class
        self.length = round(float(length),1)
        self.height = round(float(height),1)
        self.width = round(float(width),1)
        self.points = geometry_calculation.get_point_list_from_string(points)
        self.cog_x = ""
        self.cog_y = ""
        self.cog_z = ""
        self.assign_cog_coordinates(cog)
        self.start_x = ""
        self.start_y = ""
        self.start_z = ""
        self.end_x = ""
        self.end_y = ""
        self.end_z = ""

        if self.points is not None:
            self.assign_start_end_coordinates(self.points)

    def assign_cog_coordinates(self, cog):
        coordinates = [x.strip() for x in cog.replace("{", "").replace("}", "").split(",")]
        self.cog_x = coordinates[0]
        self.cog_y = coordinates[1]
        self.cog_z = coordinates[2]


    def assign_start_end_coordinates(self, points):
        # Start
        point = points[0]
        self.start_x = point[0]
        self.start_y = point[1]
        self.start_z = point[2]

        # End
        point = points[1]
        self.end_x = point[0]
        self.end_y = point[1]
        self.end_z = point[2]


