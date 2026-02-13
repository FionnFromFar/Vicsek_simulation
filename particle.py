class particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def report_position(self):
        print(f"I am a particle with position x:{self.x}, y:{self.y}")

my_bird = particle(5.0, 10.0)
my_bird.report_position()