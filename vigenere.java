import java.util.Scanner;
import java.io.File;
import java.io.IOException;

public class vigenere {
    private static String readFile(String pathname) throws IOException {
        File file = new File(pathname);
        StringBuilder fileContents = new StringBuilder((int)file.length());

        try (Scanner scanner = new Scanner(file)) {
            while (scanner.hasNextLine()) {
                fileContents.append(scanner.nextLine());
            }

            return fileContents.toString().replaceAll("[^A-Za-z]+", "").toLowerCase();
        }
    }

    public static void printToConsole(String sFile, int limit) {
        for (int i = 0; i < sFile.length(); i++) {
            System.out.print(sFile.charAt(i));

            if ((i + 1) % limit == 0)
                System.out.println();
        }
        System.out.println();
    }

    public static String makingPlaintext(String plaintextArg) throws IOException {
        StringBuilder plaintextStr = new StringBuilder(readFile(plaintextArg));

        while (plaintextStr.length() < 512)
            plaintextStr.append('x');

        if (plaintextStr.length() > 512)
            plaintextStr.setLength(512);

        return plaintextStr.toString();
    }

    public static String modifyKeyString(String keyString) {
        StringBuilder keyStringSB = new StringBuilder(keyString);

        int initialKeyLen = keyStringSB.length();
        int keyTracker = 0;

        while (keyStringSB.length() < 512) {
            // Notice the keyTracker post-increment
            keyStringSB.append(keyStringSB.charAt(keyTracker++));

            if (keyTracker >= initialKeyLen)
                keyTracker = 0;
        }

        return keyStringSB.toString();
    }

    public static String buildingCiphertext(String keyString, String plaintextStr) {
        StringBuilder cipherStringSB = new StringBuilder();

        for (int i = 0; i < plaintextStr.length(); i++) {
            int plainTextDec = plaintextStr.charAt(i) - 'a';
            int keyDec = keyString.charAt(i) - 'a';

            int addDec = (plainTextDec + keyDec) % 26;

            char cipherChar = (char)(addDec + 'a');

            cipherStringSB.append(cipherChar);
        }

        return cipherStringSB.toString();
    }

    public static void main(String[] args) throws IOException {
        if (args.length != 2) {
            System.err.println("Usage: java vigenere keyFile plaintextFile");
            System.exit(1);
        }

        String keyArg = args[0];
        String plaintextArg = args[1];

        String keyString = readFile(keyArg);

        System.out.println();
        System.out.println();

        System.out.println("Vigenere Key:");
        System.out.println();

        printToConsole(keyString, 80);

        System.out.println();
        System.out.println();

        String plaintextStr = makingPlaintext(plaintextArg);

        System.out.println("Plaintext:");
        System.out.println();

        printToConsole(plaintextStr, 80);

        System.out.println();
        System.out.println();

        keyString = modifyKeyString(keyString);

        String cipherStr = buildingCiphertext(keyString, plaintextStr);

        System.out.println("Ciphertext:");
        System.out.println();

        printToConsole(cipherStr, 80);
    }
}
