# Vigenère Cipher

- This README is in works. Some details may **not** be fully described at this time.

Developed multiple programs in various different programming languages (Java, Python, C++) that encrypts the alphabetic letters in a file using the Vigenère cipher method.

This program will take two command line parameters containing the names of the file storing the encryption key and the file to be encrypted. The first command line parameter will be the key file and the second command line parameter will be the plaintext file.

The program will output the following to the console (terminal) screen:
```txt
1. Print out the input key file
2. Print out the input plaintext file
3. Ciphertext output produced from running the cipher against the input plaintext file
```

Here is a sample run command of this program through the command line:
```bash
# Java program:
prompt> javac vigenere.java
prompt> java vigenere.java k1.txt p1.txt
```

Also included is a Bash shell script (and Python testing script), which will test the source code with a number of key files and plaintext file to a corresponding sample output of those files (aka testcases).
