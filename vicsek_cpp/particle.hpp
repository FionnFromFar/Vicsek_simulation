#ifndef PARTICLE_HPP
//this is a header guard and it stops the compiler from defining the classes twice as that would cause an error
#define PARTICLE_HPP

class Particle {
public: //public makes the data accessible to be changed throghout (in python this is automatic but not in cpp)
//making the class like the one in the python script but for cpp this time
//First, initialise all the variables
    double x;
    double y;
    double speed;
    double theta;

    //Secondly define the constructor (similar to the function in python)
    Particle(double x, double y, double speed, double theta);

    //Finally the method ie. what the function does
    void move(double dt);
    //void is an instruction which tells the constructor not to output anything, just to do calculations
};

#endif