#include <iostream>
#include "particle.hpp"

int main() {
    //This is the main function which is the code which is actually run
    //Making the particle
    Particle p(0.0, 0.0, 1.0, 0.0);

    //setting up the simulation
    double dt = 1.0;
    int total_steps = 10;

    std::cout << "--- Starting Simulation ---" << std::endl;

    //printing the intial state
    std::cout << "Initial position: " << p.x << ", "<< p.y << std::endl;

    //making the loop
    for (int t = 1; t<= total_steps; t++) {
        //moving the particle by dt
        p.move(dt);

        //printint new position
        std::cout << "Step " << t << ": " << p.x << ", " << p.y << std::endl;
    }
    
    std::cout << "--- Simulation Complete ---" << std::endl;

    return 0;
    //return 0 is a thing used in c++ to show that no errors have been found
    // its used because in c++ main() must return an integer. 
}