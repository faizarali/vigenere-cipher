CC = g++

SRC = vigenere.cpp

PRG = vigenere

all: $(SRC)
	$(CC) $(SRC) -o $(PRG)

clean:
	rm -f $(PRG)
