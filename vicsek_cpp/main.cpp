#include <iostream>
#include <fstream> //this is for writing into the csv file 
#include <vector>
#include "system.hpp" //changing from particle to system 

int main() {
    //This is the main function which is the code which is actually run
    //Adding the parameters
    int N = 50; //50 birds
    double box_size = 10.0;
    double radius = 1.0;
    double noise = 0.1;
    double dt = 0.1;
    int steps = 20;

    //setting up the system object
    System sys(N, box_size, radius, noise);

    //adding the data file
    std::ofstream dataFile("positions.csv");
    //writing the header
    dataFile << "time, id, x, y\n";

    std::cout << "---Running simulation with " << N << "birds---" << std::endl;

    //making the loop
    for (int t = 1; t<= steps; t++) {
        sys.align(); //calculating facing direction based on neighbours
        sys.evolve(dt); //moving all the particles together

        //getting the data 
        std::vector<double> x_vals = sys.get_x_positions();
        std::vector<double> y_vals = sys.get_y_positions();

        //writing to datafile
        for (int i = 0; i < N; i++){
            dataFile << t<< "," << i << "," << x_vals[i] << "," << y_vals[i] << "\n";
        }

    }
    
    dataFile.close();
    std::cout << "--- Simulation Complete. Data written to positions.csv ---" << std::endl;
    return 0;
    //return 0 is a thing used in c++ to show that no errors have been found
    // its used because in c++ main() must return an integer. 
}