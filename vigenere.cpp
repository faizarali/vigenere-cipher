#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <cctype>
#include <algorithm>
using std::cout;
using std::endl;
using std::string;
using std::vector;
using std::stringstream;

#define LIMIT 80

// Helper function for obtaining the alphabetic letters from file.
bool isNotAlpha(char c) {
    return isalpha(c) == 0;
}

// Print a max of 80 letters per row of the given string.
void printToConsole(string sFile, int limit) {
    for (int i = 0; i < sFile.length(); i++) {
        cout << sFile.at(i);

        if ((i + 1) % limit == 0)
            cout << '\n';
    }
    cout << '\n';
}

// Convert the contents of the file into a string (with some modifications).
string fileToString(const string &givenFileName) {
    std::ifstream givenFileNameStream;

    givenFileNameStream.open(givenFileName.c_str());

    stringstream strStreamForFile;
    strStreamForFile << givenFileNameStream.rdbuf();
    string file_string = strStreamForFile.str();

    // We only need to deal with the alphabetic letters.
    file_string.erase(remove_if(file_string.begin(),
                                file_string.end(), isNotAlpha),
                                file_string.end());

    // Make our string all lowercase.
    std::transform(file_string.begin(), file_string.end(),
                   file_string.begin(), ::tolower);

    givenFileNameStream.close();

    return file_string;
}

string makingPlaintext(const string &plaintext_arg) {
    string plaintext_string = fileToString(plaintext_arg);

    if (plaintext_string.length() < 512) {
        plaintext_string.resize(512, 'x');
    } else if (plaintext_string.length() > 512) {
        plaintext_string.resize(512);
    }
    return plaintext_string;
}

string modifyKeyString(string key_string) {
    int initialKeyLen = key_string.length();
    int keyTracker = 0;

    while (key_string.length() != 512) {
        key_string.push_back(key_string.at(keyTracker));
        keyTracker++;

        if (keyTracker >= initialKeyLen)
            keyTracker = 0;
    }
    return key_string;
}

string buildingCiphertext(string key_string, string plaintext_string) {
    string cipher_string;

    for (int i = 0; i < plaintext_string.length(); i++) {
        int plainTextDec = plaintext_string.at(i) - 'a';
        int keyDec = key_string.at(i) - 'a';

        int addDec = (plainTextDec + keyDec) % 26;

        char cipher = static_cast<char>(addDec + 'a');

        cipher_string.push_back(cipher);
    }
    return cipher_string;
}

int main(int argc, char **argv) {
    if (argc != 3) {
        std::cerr << "Usage: ./a.out keyFile plaintextFile" << '\n';
        return 1;
    }

    string key_arg = argv[1];
    string plaintext_arg = argv[2];

    string key_string = fileToString(key_arg);

    cout << '\n';
    cout << '\n';

    cout << "Vigenere Key:" << '\n';
    cout << '\n';

    printToConsole(key_string, LIMIT);

    cout << '\n';
    cout << '\n';

    string plaintext_string = makingPlaintext(plaintext_arg);

    cout << "Plaintext:" << '\n';
    cout << '\n';

    printToConsole(plaintext_string, LIMIT);

    cout << '\n';
    cout << '\n';

    key_string = modifyKeyString(key_string);

    string cipher_string = buildingCiphertext(key_string, plaintext_string);

    cout << "Ciphertext:" << '\n';
    cout << '\n';

    printToConsole(cipher_string, LIMIT);

    return 0;
}
