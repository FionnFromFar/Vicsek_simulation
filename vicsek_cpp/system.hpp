#ifndef SYSTEM_HPP
#define SYSTEM_HPP

#include <vector>
#include "particle.hpp"

class system {
public:
//std::vector is the command to make a list
    std::vector<Particle> particles;

    //function parameters
    double box_size;
    double radius;
    double noise;

    //the constructor
    system(int num_particles, double box_size, double radius, double noise);

    //the main methods
    void align();
    void evolve(double dt);
    //again here the use of void means nothing is outputted at this point, im just calling these functions kinda

    //the output: outputting co-ordinates as vectors (lists)
    std::vector<double> get_x_positions();
    std::vector<double> get_y_positions();

};

#endif