import sys
import subprocess


def delete_exe(arg):
    if arg.lower().endswith(('.c', '.cpp')):
        cmd = 'rm -f a.out'
    elif arg.lower().endswith('.java'):
        cmd = 'rm -f vigenere.class'
    elif arg.lower().endswith('.cs'):
        cmd = 'rm -f vigenere.exe'
    elif arg.lower().endswith('.go'):
        cmd = 'rm -f vigenere'
    else:
        return
    subprocess.run([cmd], capture_output=True, text=True, shell=True)


def check_if_file_compiles(cmd):
    proc = subprocess.run([cmd], capture_output=True, text=True, shell=True)
    if len(str(proc.stderr)) > 0:
        print('Ugh oh... Your program has warning/error messages!')
        sys.exit(1)


def compile_java(java_file):
    cmd = f'javac {java_file}'
    check_if_file_compiles(cmd)
    return 'java vigenere'


def compile_csharp(cs_file):
    cmd = f'mcs {cs_file}'
    check_if_file_compiles(cmd)
    return 'mono vigenere.exe'


def compile_c_cpp(c_cpp_file):
    compiler = 'g++' if c_cpp_file.lower().endswith('.cpp') else 'gcc'
    cmd = f'{compiler} {c_cpp_file}'
    check_if_file_compiles(cmd)
    return './a.out'


def compile_go(go_file):
    cmd = f'go build {go_file}'
    check_if_file_compiles(cmd)
    return './vigenere'


def compile_py(py_file):
    return f'python3 {py_file}'


def compile_file(arg):
    if arg.lower().endswith(('.c', '.cpp')):
        return compile_c_cpp(arg)
    elif arg.lower().endswith('.java'):
        return compile_java(arg)
    elif arg.lower().endswith('.cs'):
        return compile_csharp(arg)
    elif arg.lower().endswith('.go'):
        return compile_go(arg)
    elif arg.lower().endswith('.py'):
        return compile_py(arg)
    else:
        print('Invalid source file name')
        sys.exit(1)


def testcase_checker(exe):
    test_case_num = 4
    for i in range(1, test_case_num+1):
        subprocess.run([f'{exe} k{i}.txt p{i}.txt > stu{i}Output.txt'], capture_output=True, text=True,
                       shell=True)
        proc = subprocess.run([f'diff stu{i}Output.txt c{i}Base.txt'], capture_output=True,
                              text=True, shell=True)

        if proc.returncode != 0:
            print(f'Testcase #{i} - :\'(')
            print('->  Your output is incorrect.')
            print(f'->  Here was the command that was run: diff stu{i}Output.txt c{i}Base.txt')
            print('->  Output of the diff command is provided below:')
            print(proc.stdout)
            sys.exit(1)
        else:
            print(f'Testcase #{i}: ───==≡≡ΣΣ((( つºل͜º)つ')


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 vigenere-tester.py [filename]')
        sys.exit(1)

    arg = sys.argv[1]
    delete_exe(arg)
    exe = compile_file(arg)
    testcase_checker(exe)
    delete_exe(arg)


if __name__ == "__main__":
    main()
