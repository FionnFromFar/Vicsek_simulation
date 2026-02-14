# The compiler we want to use
CXX = g++

# The flags (options) for the compiler
# -std=c++11 : Use the modern 2011 standard (required for some math)
# -Wall      : "Warning All" - show us all potential errors
CXXFLAGS = -std=c++11 -Wall

# The final executable name
TARGET = my_simulation

# The source files
SRCS = main.cpp particle.cpp

# The object files (we replace .cpp with .o automatically)
OBJS = $(SRCS:.cpp=.o)

# --- RULES ---

# Rule 1: How to build the final target
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

# Rule 2: How to turn .cpp into .o
.cpp.o:
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Rule 3: Clean up (delete all the "cake")
clean:
	rm -f $(OBJS) $(TARGET)