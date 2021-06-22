# the compiler to use
CC = gcc

# compiler flags:
#  -g    adds debugging information to the executable file
#  -Wall turns on most, but not all, compiler warnings
CFLAGS  = -g -Wall
  
# the name to use for both the target source file, and the output file:
TARGET = untitled1
 
all: untitled1 untitled2
  
$(TARGET): $(TARGET).c
	$(CC) -o $(TARGET) $(TARGET).c $(LFLAGS)

clean:
	rm -f untitled1 untitled2
