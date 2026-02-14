#include "particle.hpp"
#include <cmath> //This is the module which has math functions like cos and sin

//"Particle:" tells c++ that this function belongs to the Particle class
Particle::Particle(double x, double y, double speed, double theta) {
    //"this->" is exactly like "self" from python
    this->x = x;
    this->y = y;
    this->speed = speed;
    this->theta = theta;
}

//making the 'move' method
void Particle::move(double dt) {
    //similar to python in the roles of the functions
    //calculating the speeds
    double vx = speed * std::cos(theta);
    double vy = speed * std::sin(theta);

    //updating the position
    x += vx * dt;
    y += vy * dt;
}