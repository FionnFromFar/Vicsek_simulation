import numpy as np

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

#new system class to manage all the birds
class system:
    def __init__(self, num_particles, box_size):
        self.box_size = box_size
        self.particles = []

        #spawning all the birds
        for i in range(num_particles):
            #making sure the intial positions are within the box
            x = np.random.uniform(0, box_size)
            y = np.random.uniform(0, box_size)
            #making sure that the initial speeds don't vary too much from bird to bird
            vx = np.random.uniform(-1.0, 1.0)
            vy = np.random.uniform(-1.0, 1.0)

            #making the bird and adding it to the list
            new_bird = particle(x, y, vx, vy)
            self.particles.append(new_bird)

    def evolve(self, dt):
        #getting all the birds to move
        for p in self.particles:
            p.move(dt)

            #making sure the birds dont fly off to infinity
            p.x = p.x % self.box_size
            p.y = p.y % self.box_size

#testing the new class
my_flock = system(num_particles=10, box_size=10)

print("Starting positions of the first 3 birds:")
for i in range(3):
    print(f"Bird {i}: x={my_flock.particles[i].x:.2f}, y={my_flock.particles[i].y:.2f}")

my_flock.evolve(dt=5)#evolution of 5 seconds

print("\nPositions after 5 seconds:")
for i in range(3):
    print(f"Bird {i}: x={my_flock.particles[i].x:.2f}, y={my_flock.particles[i].y:.2f}")