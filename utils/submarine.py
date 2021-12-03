#from utils.submarine import submarine

class submarine:
    def __init__(self) -> None:
        self.depth = 0
        self.position = 0
        self.aim = 0

    def drive(self, cmd, qbad = 0):

        dir, steps = cmd.strip().rsplit()
        steps = int(steps)
        if dir == 'forward':
            self.position += steps
        elif dir == 'down':
            self.depth += steps
        elif dir == 'up':
            self.depth -= steps
        else:
            qbad = 1

        return qbad

    def drive_aim (self, cmd, qbad = 0):
        dir, steps = cmd.strip().rsplit()
        steps = int(steps)
        if dir == 'forward':
            self.depth += self.aim * steps
            self.position += steps
        elif dir == 'down':
            self.aim += steps
        elif dir == 'up':
            self.aim -= steps
        else:
            qbad = 1
            
        return qbad