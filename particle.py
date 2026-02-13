import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class particle:
    def __init__(self, x, y, speed, theta):
        self.x = x
        self.y = y
        self.speed = speed
        self.theta = theta
    
    def move(self, dt):
        #changing calculations to get vx and vy using trig
        vx = self.speed * np.cos(self.theta)
        vy = self.speed * np.sin(self.theta)

        #updating the position like normal
        self.x = self.x + (vx * dt)
        self.y = self.y + (vy * dt)

    def report_position(self):
        print(f"I am a particle with position x:{self.x:.2f}, y:{self.y:.2f}")

#new system class to manage all the birds
class system:
    #giving the birds the gift of vision and hearing :)
    def __init__(self, num_particles, box_size, radius, noise):
        self.box_size = box_size
        self.radius = radius
        self.noise = noise
        self.particles = []

        #spawning all the birds
        for i in range(num_particles):
            #making sure the intial positions are within the box
            x = np.random.uniform(0, box_size)
            y = np.random.uniform(0, box_size)

            #making sure that the initial speeds are all the same
            speed = 1
            #giving the birds a random angle between 0 and 2pi
            theta = np.random.uniform(0, 2 * np.pi)

            #making the bird and adding it to the list (pretty much the same as before)
            new_bird = particle(x, y, speed, theta)
            self.particles.append(new_bird)

    def align(self):
        #the first step is to calc all the angles for every bird before any of them actually turn
        new_thetas = []

        for p1 in self.particles:

            sum_sin = 0.0
            sum_cos = 0.0
            neighbour_count = 0

            for p2 in self.particles:
                #calculating the distance between bird 1 and 2
                dx = p2.x - p1.x
                dy = p2.y - p1.y

                #If the distance is more than half the box then look across to the other edge
                dx = dx - self.box_size * np.round(dx/self.box_size)
                dy = dy - self.box_size * np.round(dy/self.box_size)

                #pythagorean distance calc
                dist = np.sqrt(dx**2 + dy**2)

                #checking inside the vision radius
                if dist < self.radius:
                    sum_sin += np.sin(p2.theta)
                    sum_cos += np.cos(p2.theta)
                    neighbour_count += 1

            #average angle of all the neighbours
            avg_theta = np.arctan2(sum_sin / neighbour_count, sum_cos/neighbour_count)
            
            #adding a lil bit of noise
            random_error = np.random.uniform(-self.noise/2, self.noise/2)

            new_thetas.append(avg_theta + random_error)

        for i, p in enumerate(self.particles):
            p.theta = new_thetas[i]

    def evolve(self, dt):
        #getting all the birds to move
        for p in self.particles:
            p.move(dt)

            #making sure the birds dont fly off to infinity
            p.x = p.x % self.box_size
            p.y = p.y % self.box_size

#setting up the simulation and animation

box_size = 10
my_flock = system(num_particles=50, box_size=box_size, radius=1.5, noise=2) #50 birbs ;)
#increasing the noise is like removing their brains, they dont know how to calibrate a correct turn

#making the canvas
fig, ax = plt.subplots()
ax.set_xlim(0, box_size)
ax.set_ylim(0, box_size)
ax.set_aspect("equal")
ax.set_title("50 flying birds with vision and hearing")

#extracting positions as lists
x_vals = [p.x for p in my_flock.particles]
y_vals = [p.y for p in my_flock.particles]

#making the birds blue dots
scatter = ax.scatter(x_vals, y_vals, c="blue", s=15)

#animating!
def update(frame):
    #first the birds look
    my_flock.align()
    #THEN they turn and move
    my_flock.evolve(dt=0.05)

    #fetching new positions
    new_x = [p.x for p in my_flock.particles]
    new_y = [p.y for p in my_flock.particles]

    #updating the frame
    scatter.set_offsets(np.c_[new_x, new_y])
    return scatter,

ani = animation.FuncAnimation(fig, update, frames=500, interval=30, blit=True)

#saving the animation as a gif
print("Rendering animation...")
ani.save("flock3.gif", writer="pillow")
print("Done! The birds are flying in flock3.gif")

