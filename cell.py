class Cell:

    def __init__(self, life):
        self.age = 0
        self.age_color = [220, 0, 0, 220, 0, 0, 220, 0, 0, 220, 0, 0]
        self.alive = life

    def set_alive(self, b):
        self.alive = b

    def aging(self):
        if not self.alive:
            self.age = 0
            self.age_color = [220, 0, 0, 220, 0, 0, 220, 0, 0, 220, 0, 0]
        else:
            self.age += 1
            if self.age_color[0] > 0:
                self.age_color[0] -= 10
                self.age_color[3] -= 10
                self.age_color[6] -= 10
                self.age_color[9] -= 10
                self.age_color[1] += 10
                self.age_color[4] += 10
                self.age_color[7] += 10
                self.age_color[10] += 10
                self.age_color[2] += 2
                self.age_color[5] += 2
                self.age_color[8] += 2
                self.age_color[11] += 2

        return self.age
