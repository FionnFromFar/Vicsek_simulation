import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

#setting up the simulation and animation

box_size = 10
my_flock = system(num_particles=50, box_size=box_size)#50 birbs ;)

#making the canvas
fig, ax = plt.subplots()
ax.set_xlim(0, box_size)
ax.set_ylim(0, box_size)
ax.set_aspect("equal")
ax.set_title("50 flying birds")

#extracting positions as lists
x_vals = [p.x for p in my_flock.particles]
y_vals = [p.y for p in my_flock.particles]

#making the birds blue dots
scatter = ax.scatter(x_vals, y_vals, c="blue", s=15)

#animating!
def update(frame):
    my_flock.evolve(dt=0.1)

    #fetching new positions
    new_x = [p.x for p in my_flock.particles]
    new_y = [p.y for p in my_flock.particles]

    #updating the frame
    scatter.set_offsets(np.c_[new_x, new_y])
    return scatter,

ani = animation.FuncAnimation(fig, update, frames=200, interval=30, blit=True)

#saving the animation as a gif
print("Rendering animation...")
ani.save("flock1.gif", writer="pillow")
print("Done! The birds are flying in flock1.gif")

