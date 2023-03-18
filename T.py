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

            source = f.read()

    except FileNotFoundError:

        print('File not found:', file)

        return

    code = compile(source, file, 'exec')

    outfile = os.path.splitext(file)[0] + '.pyc'

    try:

        with open(outfile, 'wb') as f:

            marshal.dump(code, f)

    except IOError as e:

        print('Failed to write compiled file:', e)

        return

    print('Compilation successful')

def load_marshal():

    file = input('Enter file location: ')

    try:

        with open(file, 'rb') as f:

            code = marshal.load(f)

    except FileNotFoundError:

        print('File not found:', file)

        return

    except (EOFError, ValueError) as e:

        print('Failed to load compiled file:', e)

        return

    exec(code)

    print('Code executed successfully')

def main():

    while True:

        os.system('clear')

        print('Code By AKING\n----------------')

        print('1 -> Compile Cython')

        print('2 -> Compile ELF (ex: ./run)')

        print('3 -> Compile Marshal')

        print('4 -> Load Marshal')

        print('0 -> Exit')

        opt = input('-> Opt: ')

        if opt == '1':

            compile_cython()

        elif opt == '2':

            compile_elf()

        elif opt == '3':

            compile_marshal()

        elif opt == '4':

            load_marshal()

        elif opt == '0':

            sys.exit('Exiting...')

        else:

            print('Invalid option')

if __name__ == '__main__':

    main()

