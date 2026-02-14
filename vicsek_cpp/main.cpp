#include <iostream>
#include "particle.hpp"

int main() {
    //This is the main function which is the code which is actually run
    //Making the particle
    Particle p(0.0, 0.0, 1.0, 0.0);

    //printing the intial state
    std::cout << "Initial position: " << p.x << ", "<< p.y << std::endl;

    //moving the particle for 1 second
    p.move(1.0);

    //print the new position
    std::cout << "New position:    " << p.x << ", " << p.y << std::endl;
    
    return 0;
    //return 0 is a thing used in c++ to show that no errors have been found
    // its used because in c++ main() must return an integer. 
}