import sys
import subprocess
import functools
import os


def delete_exe(arg, base):
    if arg.lower().endswith(('.c', '.cpp')):
        cmd = 'rm -f a.out'
    elif arg.lower().endswith('.java'):
        cmd = f'rm -f {base}.class'
    elif arg.lower().endswith('.cs'):
        cmd = f'rm -f {base}.exe'
    elif arg.lower().endswith('.go'):
        cmd = f'rm -f {base}'
    else:
        return
    subprocess.run([cmd], capture_output=True, text=True, shell=True)


def check_if_file_compiles(cmd):
    proc = subprocess.run([cmd], capture_output=True, text=True, shell=True)
    if len(str(proc.stderr)) > 0:
        print('Ugh oh... Your program has warning/error messages!')
        sys.exit(1)
    else:
        print('Compiles')


def compile_java(java_file, base):
    cmd = f'javac {java_file}'
    check_if_file_compiles(cmd)
    return f'java {base}'


def compile_csharp(cs_file, base):
    cmd = f'mcs {cs_file}'
    check_if_file_compiles(cmd)
    return f'mono {base}.exe'


def compile_c_cpp(c_cpp_file):
    compiler = 'g++' if c_cpp_file.lower().endswith('.cpp') else 'gcc'
    cmd = f'{compiler} {c_cpp_file}'
    check_if_file_compiles(cmd)
    return './a.out'


def compile_go(go_file, base):
    cmd = f'go build {go_file}'
    check_if_file_compiles(cmd)
    return f'./{base}'


def compile_js(js_file):
    print('Compiles')
    return f'node {js_file}'


def compile_py(py_file):
    print('Compiles')
    return f'python3 {py_file}'


def compile_file(arg, base):
    if arg.lower().endswith(('.c', '.cpp')):
        return compile_c_cpp(arg)
    elif arg.lower().endswith('.java'):
        return compile_java(arg, base)
    elif arg.lower().endswith('.cs'):
        return compile_csharp(arg, base)
    elif arg.lower().endswith('.go'):
        return compile_go(arg, base)
    elif arg.lower().endswith('.js'):
        return compile_js(arg)
    elif arg.lower().endswith('.py'):
        return compile_py(arg)
    else:
        print('Invalid source file name', file=sys.stderr)
        sys.exit(1)


def testcase_checker(exe):
    test_case_num = 4

    error_checker_1 = subprocess.run([f'{exe}'], capture_output=True, text=True, shell=True)
    error_checker_2 = subprocess.run([f'{exe} k1.txt'], capture_output=True, text=True, shell=True)

    if len(str(error_checker_1.stderr)) <= 0 or len(str(error_checker_2.stderr)) <= 0:
        print('Ugh oh... You seem to be having issues with the command line arguments. Make sure you output your '
              'error checking to stderr.')
        return
    elif len(str(error_checker_1.stdout)) != 0 or len(str(error_checker_2.stdout)) != 0:
        print('Issue: Your program might be either hard coding filenames in the source code and/or not handling error '
              'checking correctly. Please fix this issue.')
        return

    for i in range(1, test_case_num + 1):
        subprocess.run([f'{exe} k{i}.txt p{i}.txt > stu{i}Output.txt'], capture_output=True, text=True,
                       shell=True)

        # read output from each text file
        with open(f'stu{i}Output.txt', "r") as f1:
            l1 = f1.readlines()

        with open(f'c{i}Base.txt', "r") as f2:
            l2 = f2.readlines()

        # compare the content read
        if len(l1) == len(l2) and functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, l1, l2), True):
            print(f'Testcase #{i}: ───==≡≡ΣΣ((( つºل͜º)つ')
        else:
            print(f'Testcase #{i} - :\'(')
            print('->  Your output is incorrect.')
            print(f'->  Please use this command: diff stu{i}Output.txt c{i}Base.txt')
            print('->  Output of the diff command is provided below:')
            proc = subprocess.run([f'diff stu{i}Output.txt c{i}Base.txt'], capture_output=True,
                                  text=True, shell=True)
            print(proc.stdout)
            return


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 vigenere-tester.py [filename]', file=sys.stderr)
        sys.exit(1)

    arg = sys.argv[1]
    base, ext = os.path.splitext(arg)
    delete_exe(arg, base)
    exe = compile_file(arg, base)
    testcase_checker(exe)
    delete_exe(arg, base)


if __name__ == "__main__":
    main()
