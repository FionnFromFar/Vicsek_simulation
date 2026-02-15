CXX = g++ #the compiler im using

CXXFLAGS = -std=c++11 -Wall

#name of outputted file
TARGET = my_simulation

#adding the phony part so makefile ignores 
.PHONY: clean run

#adding the source files
SRCS = main.cpp particle.cpp system.cpp

# The object files (we replace .cpp with .o automatically)
OBJS = $(SRCS:.cpp=.o)

# --- RULES ---

#1: Building the final output
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

#2: turning .cpp files into .o
.cpp.o:
	$(CXX) $(CXXFLAGS) -c $< -o $@

#3: Getting rid of the stuff im not gonna use
clean:
	rm -f $(OBJS) $(TARGET)

#4: Running the program
run: $(TARGET)
	./$(TARGET)