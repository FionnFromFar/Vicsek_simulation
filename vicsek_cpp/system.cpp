#include "system.hpp"
#include <cmath>
#include <random> //for random numbers that numpy would've covered

//c++ random number setup
std::random_device rd; //generating the rd which is used to generate a seed
std::mt19937 gen(rd()); //uses rd to generate a seed
std::uniform_real_distribution<> dis(0.0, 1.0); //defining the prob distribution

System::System(int num_particles, double box_size, double radius, double noise) {
    this->box_size = box_size;
    this->radius = radius;
    this->noise = noise;

    for(int i = 0; i < num_particles; i ++) { //initialising the for loop
            double x = dis(gen) * box_size;
            double y = dis(gen) * box_size;
            double theta = dis(gen) * 2 * M_PI; //"M_PI is like np.pi"

            particles.push_back(Particle(x, y, 0.5, theta)); //appending the particles to the list
    }
}

void System::align() {
    std::vector<double> new_thetas; // create a list of variable type double
    for(const auto& p1 : particles) {
        double sum_sin = 0.0;
        double sum_cos = 0.0;
        int count = 0;

        for(const auto& p2 : particles) {
            double dx = p2.x - p1.x;
            double dy = p2.y - p2.y;

            //same boundry conditions as before (like pacman)
            if (dx > box_size / 2) dx -= box_size;
            if (dx < -box_size / 2) dx += box_size;
            if (dy > box_size / 2) dy -= box_size;
            if (dy < -box_size / 2) dy += box_size;

            double dist = std::sqrt(dx*dx + dy*dy);

            if (dist < radius) {
                sum_sin += std::sin(p2.theta);
                sum_cos += std::cos(p2.theta);
                count ++;
            }
            
        }

        double avg_theta = std::atan2(sum_sin/count, sum_cos/count);
        double noise_val = (dis(gen) - 0.5) * noise; //adding the noise (bird stupidity)

        new_thetas.push_back(avg_theta + noise_val);
    }
    //turning the birds
    for(size_t i = 0; i < particles.size(); i++) {
        particles[i].theta = new_thetas[i];

    }
}

void System::evolve(double dt) {
    for(auto& p : particles) {
        p.move(dt);
        p.x = std::fmod(p.x, box_size);
        if (p.x < 0) p.x += box_size;

        p.y = std::fmod(p.y, box_size);
        if (p.y < 0) p.y += box_size;
    }
}

//linking to python
std::vector<double> System::get_x_positions() {
    std::vector<double> xs;
    for(const auto& p : particles) xs.push_back(p.x);
    return xs;
}

std::vector<double> System::get_y_positions() {
    std::vector<double> ys;
    for(const auto& p : particles) ys.push_back(p.y);
    return ys;
}

