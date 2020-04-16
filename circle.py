class Circle:
    click_count = 0
    radius_coordinates = []

    def __init__(self):
        for i in range(4):
            self.radius_coordinates.append(None)

    def motion(self, event):
        x, y = event.x, event.y
        print(str(x) + " " + str(y))
        if self.click_count == 0:
            self.radius_coordinates[0] = x
            self.radius_coordinates[1] = y
            self.click_count += 1
            return False
        elif self.click_count == 1:
            self.radius_coordinates[2] = x
            self.radius_coordinates[3] = y
            self.click_count = 0
            print(self.radius_coordinates)
            return True

    def get_radius_coordinates(self):
        return self.radius_coordinates