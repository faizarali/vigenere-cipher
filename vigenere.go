package main

import (
    "fmt"
    "log"
    "os"
    "regexp"
    "strings"
)

func printToStdout(sFile string, limit int) {
    for i := 0; i < len(sFile); i++ {
        fmt.Print(string(sFile[i]))

        if (i + 1) % limit == 0 {
            fmt.Println()
        }
    }
    fmt.Println()
}

func readFile(pathname string) string {
    b, err := os.ReadFile(pathname)

    if err != nil {
        fmt.Print(err)
    }

    str := string(b)

    reg, err := regexp.Compile("[^A-Za-z]+")
    if err != nil {
        fmt.Print(err)
    }
    newStr := reg.ReplaceAllString(str, "")
    newStr = strings.ToLower(newStr)
    return newStr
}

func createPlainText(plaintextArg string) string {
    var sb strings.Builder
    sb.WriteString(plaintextArg)

    for sb.Len() < 512 {
        sb.WriteRune('x')
    }

    if sb.Len() > 512 {
        return sb.String()[:512]
    } else {
        return sb.String()
    }
}

func createKeyStr(keyStr string) string {
    var sb strings.Builder
    sb.WriteString(keyStr)
    initialKeyLen := sb.Len()
    keyTracker := 0

    for sb.Len() < 512 {
        strTemp := keyStr[keyTracker]
        sb.WriteString(string(strTemp))
        keyTracker += 1

        if keyTracker >= initialKeyLen {
            keyTracker = 0
        }
    }
    return sb.String()
}

func createCiphertext(keyStr string, plaintextStr string) string {
    var sb strings.Builder
    for i := 0; i < len(plaintextStr); i++ {
        plainTextDec := plaintextStr[i] - 'a'
        keyDec := keyStr[i] - 'a'
        addDec := (plainTextDec + keyDec) % 26
        cipherChar := string(addDec + 'a')
        sb.WriteString(cipherChar)
    }
    return sb.String()
}

func main() {
    if len(os.Args) != 3 {
        log.Fatal("Usage: ./vigenere keyFile plaintextFile")
        os.Exit(1)
    }

    keyArg := os.Args[1]
    plaintextArg := os.Args[2]

    fmt.Println()
    fmt.Println()

    keyStr := readFile(keyArg)

    fmt.Println("Vigenere Key:")
    fmt.Println()

    printToStdout(keyStr, 80)

    fmt.Println()
    fmt.Println()

    plaintextStr := readFile(plaintextArg)

    plaintextStr = createPlainText(plaintextStr)

    fmt.Println("Plaintext:")
    fmt.Println()

    printToStdout(plaintextStr, 80)

    fmt.Println()
    fmt.Println()

    keyStr = createKeyStr(keyStr)

    cipherStr := createCiphertext(keyStr, plaintextStr)

    fmt.Println("Ciphertext:")
    fmt.Println()

    printToStdout(cipherStr, 80)
}
