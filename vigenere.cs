using System;
using System.IO;
using System.Text;
using System.Linq;

public class vigenere {

    private static string fileToString(string pathname) {
        string contents = File.ReadAllText(pathname);
        var sb = new StringBuilder();

        foreach (char i in contents)
            if (i != '\n' && i != '\r' && i != '\t')
                sb.Append(i);

        return new string(sb.ToString().Where(Char.IsLetter).ToArray()).ToLower();
    }

    public static void printToConsole(string sFile, int limit) {
        for (int i = 0; i < sFile.Length; i++) {
            Console.Write(sFile[i]);

            if ((i + 1) % limit == 0)
                Console.WriteLine();
        }
        Console.WriteLine();
    }

    public static string makingPlaintext(string plaintextArg) {
        var plaintextStr = new StringBuilder(fileToString(plaintextArg));

        while (plaintextStr.Length < 512)
            plaintextStr.Append('x');

        if (plaintextStr.Length > 512)
            return plaintextStr.ToString().Substring(0, 512);

        return plaintextStr.ToString();
    }

    public static string modifyKeyString(string keyString) {
        var keyStringSB = new StringBuilder(keyString);

        int initialKeyLen = keyStringSB.Length;
        int keyTracker = 0;

        while (keyStringSB.Length < 512) {
            // Notice the keyTracker post-increment
            keyStringSB.Append(keyStringSB[keyTracker++]);

            if (keyTracker >= initialKeyLen)
                keyTracker = 0;
        }
        return keyStringSB.ToString();
    }

    public static string buildingCiphertext(string keyString, string plaintextStr) {
        var cipherStringSB = new StringBuilder();

        for (int i = 0; i < plaintextStr.Length; i++) {
            int plainTextDec = plaintextStr[i] - 'a';
            int keyDec = keyString[i] - 'a';

            int addDec = (plainTextDec + keyDec) % 26;

            char cipherChar = (char)(addDec + 'a');

            cipherStringSB.Append(cipherChar);
        }
        return cipherStringSB.ToString();
    }

    public static void Main(string[] args) {
        if (args.Length != 2) {
            Console.Error.WriteLine("Usage: mono vigenere.exe keyFile plaintextFile");
            Environment.Exit(1);
        }

        string keyArg = args[0];
        string plaintextArg = args[1];

        string keyString = fileToString(keyArg);

        Console.WriteLine();
        Console.WriteLine();

        Console.WriteLine("Vigenere Key:");
        Console.WriteLine();

        printToConsole(keyString, 80);

        Console.WriteLine();
        Console.WriteLine();

        string plaintextStr = makingPlaintext(plaintextArg);

        Console.WriteLine("Plaintext:");
        Console.WriteLine();

        printToConsole(plaintextStr, 80);

        Console.WriteLine();
        Console.WriteLine();

        keyString = modifyKeyString(keyString);

        string cipherStr = buildingCiphertext(keyString, plaintextStr);

        Console.WriteLine("Ciphertext:");
        Console.WriteLine();

        printToConsole(cipherStr, 80);
    }
}
