import sys
import subprocess
import shlex

def compile_java(java_file):
    cmd = 'javac ' + java_file
    process = subprocess.Popen(shlex.split(cmd))
    process.wait()
    return "java vigenere"

def compile_cpp(cpp_file):
    cmd = 'g++ ' + cpp_file
    process = subprocess.Popen(shlex.split(cmd))
    process.wait()
    return "./a.out"

def compile_c(c_file):
    cmd = 'gcc ' + c_file
    process = subprocess.Popen(shlex.split(cmd))
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
elif arg == "vigenere.py":
    EXE = compile_py(arg)
else:
    print("Invalid source file name")
    sys.exit(1)

# Accounts for four test cases
for i in range(1, 5):
    print(f"Case #{i}")
    input = EXE + f' k{i}.txt p{i}.txt'
    command = shlex.split(input)
    with open(f'stu{i}Output.txt', "w") as outfile:
        p = subprocess.Popen(command, stdout=outfile)
        p.wait()
    input = f'diff stu{i}Output.txt c{i}Base.txt'
    p = subprocess.Popen(shlex.split(input))
    p.wait()
    print(f"Case #{i} - complete")
