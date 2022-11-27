import sys
import subprocess


def compile_java(java_file):
    cmd = f'javac {java_file}'
    process = subprocess.Popen(cmd, shell=True)
    process.wait()
    return "java vigenere"


def compile_csharp(cs_file):
    cmd = f'mcs {cs_file}'
    process = subprocess.Popen(cmd, shell=True)
    process.wait()
    return "mono vigenere.exe"


def compile_cpp(cpp_file):
    cmd = f'g++ {cpp_file}'
    process = subprocess.Popen(cmd, shell=True)
    process.wait()
    return "./a.out"


def compile_c(c_file):
    cmd = f'gcc {c_file}'
    process = subprocess.Popen(cmd, shell=True)
    process.wait()
    return "./a.out"


def compile_py(py_file):
    return "python3 vigenere.py"


if len(sys.argv) != 2:
    print('Usage: python3 vigenere-tester.py [filename]')
    sys.exit(1)

arg = sys.argv[1]

if arg == "vigenere.c":
    EXE = compile_c(arg)
elif arg == "vigenere.cpp":
    EXE = compile_cpp(arg)
elif arg == "vigenere.java":
    EXE = compile_java(arg)
elif arg == "vigenere.cs":
    EXE = compile_csharp(arg)
elif arg == "vigenere.py":
    EXE = compile_py(arg)
else:
    print("Invalid source file name")
    sys.exit(1)

for i in range(1, 5):
    print(f"Case #{i}")
    p = subprocess.Popen(EXE + f' k{i}.txt p{i}.txt > stu{i}Output.txt', shell=True)
    p.wait()
    p = subprocess.Popen(f'diff stu{i}Output.txt c{i}Base.txt', shell=True)
    p.wait()
    print(f"Case #{i} - complete")
