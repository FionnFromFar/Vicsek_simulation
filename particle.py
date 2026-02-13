class particle:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    def move(self, dt):
        #addition of function which uses velocity to update position
        self.x = self.x + (self.vx * dt)
        self.y = self.y + (self.vy * dt)
    
    def report_position(self):
        print(f"I am a particle with position x:{self.x:.2f}, y:{self.y:.2f}")

#testing the new physics with start position 0 and some initial velocity
my_bird = particle(x=0.0, y=0.0, vx=2.0, vy=1.0) 

print("Time t=0:")
my_bird.report_position()

my_bird.move(dt=0.5)

print("Time t=0.5:")
my_bird.report_position()