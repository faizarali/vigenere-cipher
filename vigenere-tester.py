import sys
import subprocess


def delete_exe():
    process = None
    if arg == 'vigenere.c':
        process = subprocess.Popen('rm -f a.out', shell=True)
    elif arg == 'vigenere.cpp':
        process = subprocess.Popen('rm -f a.out', shell=True)
    elif arg == 'vigenere.java':
        process = subprocess.Popen('rm -f vigenere.class', shell=True)
    elif arg == 'vigenere.cs':
        process = subprocess.Popen('rm -f vigenere.exe', shell=True)
    elif arg == 'vigenere.go':
        process = subprocess.Popen('rm -f vigenere', shell=True)
    else:
        return
    process.wait()


def compile_java(java_file):
    cmd = f'javac {java_file}'
    process = subprocess.Popen(cmd, shell=True)
    if process.wait() != 0:
        print('does not compile')
        sys.exit(1)
    return 'java vigenere'


def compile_csharp(cs_file):
    cmd = f'mcs {cs_file}'
    process = subprocess.Popen(cmd, shell=True)
    if process.wait() != 0:
        print('does not compile')
        sys.exit(1)
    return 'mono vigenere.exe'


def compile_cpp(cpp_file):
    cmd = f'g++ {cpp_file}'
    process = subprocess.Popen(cmd, shell=True)
    if process.wait() != 0:
        print('does not compile')
        sys.exit(1)
    return './a.out'


def compile_c(c_file):
    cmd = f'gcc {c_file}'
    process = subprocess.Popen(cmd, shell=True)
    if process.wait() != 0:
        print('does not compile')
        sys.exit(1)
    return './a.out'


def compile_go(go_file):
    cmd = f'go build {go_file}'
    process = subprocess.Popen(cmd, shell=True)
    if process.wait() != 0:
        print('does not compile')
        sys.exit(1)
    return './vigenere'


def compile_js(js_file):
    return f'node {js_file}'


def compile_py(py_file):
    return f'python3 {py_file}'


if len(sys.argv) != 2:
    print('Usage: python3 vigenere-tester.py [filename]')
    sys.exit(1)

arg = sys.argv[1]

delete_exe()

if arg == 'vigenere.c':
    EXE = compile_c(arg)
elif arg == 'vigenere.cpp':
    EXE = compile_cpp(arg)
elif arg == 'vigenere.java':
    EXE = compile_java(arg)
elif arg == 'vigenere.cs':
    EXE = compile_csharp(arg)
elif arg == 'vigenere.js':
    EXE = compile_js(arg)
elif arg == 'vigenere.go':
    EXE = compile_go(arg)
elif arg == 'vigenere.py':
    EXE = compile_py(arg)
else:
    print('Invalid source file name')
    sys.exit(1)

test_case_num = 4

for i in range(1, test_case_num + 1):
    p = subprocess.Popen(f'{EXE} k{i}.txt p{i}.txt > stu{i}Output.txt', shell=True)
    p.wait()
    p = subprocess.Popen(f'diff stu{i}Output.txt c{i}Base.txt &> /dev/null', shell=True)
    if p.wait() != 0:
        print(f'Testcase #{i} - :\'(')
        print('->  Your output is incorrect.')
        print(f'->  Here was the command that was run: diff stu{i}Output.txt c{i}Base.txt')
        print('->  Output of the diff command is provided below:')
        p = subprocess.Popen(f'diff stu{i}Output.txt c{i}Base.txt', shell=True)
        p.wait()
        sys.exit(1)
    else:
        print(f'Testcase #{i}: ───==≡≡ΣΣ((( つºل͜º)つ')

delete_exe()
