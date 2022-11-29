import sys
import subprocess
import shlex


def delete_exe():
    cmd = None
    if arg == 'vigenere.c':
        cmd = 'rm -f a.out'
    elif arg == 'vigenere.cpp':
        cmd = 'rm -f a.out'
    elif arg == 'vigenere.java':
        cmd = 'rm -f vigenere.class'
    elif arg == 'vigenere.cs':
        cmd = 'rm -f vigenere.exe'
    elif arg == 'vigenere.go':
        cmd = 'rm -f vigenere'
    else:
        return
    process = subprocess.Popen(shlex.split(cmd))
    process.wait()


def compile_java(java_file):
    cmd = f'javac {java_file}'
    process = subprocess.Popen(shlex.split(cmd))
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
    process = subprocess.Popen(shlex.split(cmd))
    if process.wait() != 0:
        print('does not compile')
        sys.exit(1)
    return './a.out'


def compile_c(c_file):
    cmd = f'gcc {c_file}'
    process = subprocess.Popen(shlex.split(cmd))
    if process.wait() != 0:
        print('does not compile')
        sys.exit(1)
    return './a.out'
    

def compile_go(go_file):
    cmd = f'go build {go_file}'
    process = subprocess.Popen(shlex.split(cmd))
    if process.wait() != 0:
        print('does not compile')
        sys.exit(1)
    return './vigenere'


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
elif arg == 'vigenere.go':
    EXE = compile_go(arg)
elif arg == 'vigenere.py':
    EXE = compile_py(arg)
else:
    print('Invalid source file name')
    sys.exit(1)

test_case_num = 4

for i in range(1, test_case_num + 1):
    file_input = f'{EXE} k{i}.txt p{i}.txt'
    command = shlex.split(file_input)
    with open(f'stu{i}Output.txt', 'w') as outfile:
        p = subprocess.Popen(command, stdout=outfile)
        p.wait()
    file_input = f'diff stu{i}Output.txt c{i}Base.txt'
    p = subprocess.Popen(shlex.split(file_input), stdout=subprocess.DEVNULL)
    if p.wait() != 0:
        print(f'Testcase #{i} - :\'(')
        print('->  Your output is incorrect.')
        print(f'->  Here was the command that was run: diff stu{i}Output.txt c{i}Base.txt')
        print('->  Output of the diff command is provided below:')
        file_input = f'diff stu{i}Output.txt c{i}Base.txt'
        p = subprocess.Popen(shlex.split(file_input))
        p.wait()
        sys.exit(1)
    else:
        print(f'Testcase #{i}: ───==≡≡ΣΣ((( つºل͜º)つ')

delete_exe()
