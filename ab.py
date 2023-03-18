import os

import subprocess

import sys

import marshal

try:

    import cython

    from Cython.Build.BuildExecutable import build

except ImportError:

    print('Cython is not installed. Installing now...')

    subprocess.run(['pip', 'install', 'cython'], check=True)

    import cython

    from Cython.Build.BuildExecutable import build

def compile_cython():

    file = input('Enter file location: ')

    try:

        with open(file, 'r') as f:

            f.read()

    except FileNotFoundError:

        print('File not found:', file)

        return

    try:

        subprocess.run(['cythonize', '-i', '-2', file], check=True)

    except subprocess.CalledProcessError as e:

        print('Cython compilation failed:', e)

        return

    print('Compilation successful')

def compile_elf():

    file = input('Enter file location: ')

    try:

        with open(file, 'r') as f:

            f.read()

    except FileNotFoundError:

        print('File not found:', file)

        return

    try:

        build(file)

    except cython.CompilerError as e:

        print('ELF compilation failed:', e)

        return

    print('Compilation successful')

def compile_marshal():

    file = input('Enter file location: ')

    try:

        with open(file, 'r') as f:

            source_code = f.read()

    except FileNotFoundError:

        print('File not found:', file)

        return

    code_object = compile(source_code, file, 'exec')

    output_file = input('Enter output file location: ')

    with open(output_file, 'wb') as f:

        marshal.dump(code_object, f)

    print('Compilation successful')

def main():

    while True:

        os.system('clear')

        print('Code By AKING\n----------------')

        print('1 -> Compile Cython')

        print('2 -> Compile ELF (ex: ./run)')

        print('3 -> Compile Marshal')

        print('0 -> Exit')

        opt = input('-> Opt: ')

        if opt == '1':

            compile_cython()

        elif opt == '2':

            compile_elf()

        elif opt == '3':

            compile_marshal()

        elif opt == '0':

            sys.exit('Exiting...')

        else:

            print('Invalid option')

if __name__ == '__main__':

    main()

