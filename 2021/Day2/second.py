with open('input.txt') as f:
    lines = f.readlines()

class Submarine:
    horizontal = 0
    depth = 0
    aim = 0

    def forward(self, value):
        self.horizontal += value
        self.depth += self.aim * value

    def down(self, value):
        self.aim += value

    def up(self, value):
        self.aim -= value

    def returnMultiplied(self):
        return self.horizontal * self.depth

    def changeCourse(self, course, value):
        if course == 'forward':
            self.forward(value)
        elif course == 'down':
            self.down(value)
        elif course == 'up':
            self.up(value)


sub = Submarine()

for line in lines:
    split = line.split(' ')
    sub.changeCourse(split[0], int(split[1]))

print(str(sub.returnMultiplied()))
