#!/bin/bash

# 1. Execute the command: chmod +x *.sh
# 2. Compile & test with the command: ./hillcipher-tester.sh hillcipher.xyz
#    (where xyz is either c, cpp, java, cs, go, or py)
#    For example: ./hw1Test.sh vigenere.cpp

case $1 in
vigenere.c)
	rm -f vigenere
	gcc vigenere.c -o vigenere
	compiled=$?
	if [[ $compiled != 0 ]]; then
		echo "does not compile"
		exit 1
	fi
	echo "Compiles"
	EXE="./vigenere"
	;;
vigenere.cpp)
	rm -f vigenere
	g++ vigenere.cpp -o vigenere
	compiled=$?
	if [[ $compiled != 0 ]]; then
		echo "does not compile"
		exit 1
	fi
	echo "Compiles"
	EXE="./vigenere"
	;;
vigenere.java)
	rm -f vigenere.class
	javac vigenere.java
	compiled=$?
	if [[ $compiled != 0 ]]; then
		echo "does not compile"
		exit 1
	fi
	echo "Compiles"
	EXE="java vigenere"
	;;
vigenere.cs)
	rm -f vigenere.exe
	mcs vigenere.cs
	compiled=$?
	if [[ $compiled != 0 ]]; then
		echo "does not compile"
		exit 1
	fi
	echo "Compiles"
	EXE="mono vigenere.exe"
	;;
vigenere.go)
	rm -f vigenere
	go build vigenere.go
	compiled=$?
	if [[ $compiled != 0 ]]; then
		echo "does not compile"
		exit 1
	fi
	EXE="./vigenere"
	;;
vigenere.js)
	echo "Compiles"
	EXE="node vigenere.js"
	;;
vigenere.py)
	echo "Compiles"
	EXE="python3 vigenere.py"
	;;
*)
	echo "Invalid source file name"
	exit 1
esac

test_case_num=4

for (( i = 1; i <= test_case_num; i++ ))
do
    echo -n "Testcase #$i: "
    eval $EXE k$i.txt p$i.txt > stu${i}Output.txt
	executed=$?
	if [[ $executed !=  0 ]]; then
		echo ":'("
		echo "->  Issue related with using command line argments in your code."
		echo "->  Please recheck your source code."
		exit 1
	else
		diff stu${i}Output.txt c${i}Base.txt &> /dev/null
		correct=$?
		if [[ $correct != 0 ]]; then
			echo ":'("
			echo "->  Your output is incorrect."
			echo "->  Here was the command that was run: diff stu${i}Output.txt c${i}Base.txt"
			echo "->  Output of the diff command is provided below:"
			diff stu${i}Output.txt c${i}Base.txt
			exit 1
		else
			echo "───==≡≡ΣΣ((( つºل͜º)つ"
		fi
	fi
done
