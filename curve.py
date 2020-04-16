class Curve:
    click_count = 0
    line_coordinates = []
    SIZE = 8

    def __init__(self):
        for i in range(self.SIZE):
            self.line_coordinates.append(None)

    def empty_coordinates(self):
        for i in range(self.SIZE):
            self.line_coordinates[i] = None

    def motion(self, event):
        x, y = event.x, event.y
        print(str(x) + " " + str(y))
        if self.click_count == 0:
            self.empty_coordinates()
            self.line_coordinates[0] = x
            self.line_coordinates[1] = y
            self.click_count += 1
            return False
        elif self.click_count == 1:
            self.line_coordinates[2] = x
            self.line_coordinates[3] = y
            self.click_count += 1
            return False
        elif self.click_count == 2:
            self.line_coordinates[4] = x
            self.line_coordinates[5] = y
            self.click_count += 1
            return False
        elif self.click_count == 3:
            self.line_coordinates[6] = x
            self.line_coordinates[7] = y
            self.click_count = 0
            print(self.line_coordinates)
            return True

    def get_line_coordinates(self):
        return self.line_coordinates
