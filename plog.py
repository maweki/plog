#!/usr/bin/env python3
import os

basedir = os.path.abspath(os.path.dirname(__file__))
datadir = os.path.join(basedir, 'data')

def git_exec(*params):
    wd = os.getcwd()
    os.chdir(datadir)
    import subprocess
    ret = subprocess.call(['git'] + list(params))
    os.chdir(wd)
    return ret

def init():
    res = git_exec('init', '--quiet')
    if res:
        print("Error creating personal log repository")

def add(text):
    t = ' '.join(text)
    git_exec('commit', '--quiet', '--allow-empty', '-m', t)

def show():
    git_exec('log', '--no-notes', '--date=local', '--format=%Cred%ad, %ar: %Cgreen%s')

def main():
    import argparse
    parser = argparse.ArgumentParser('Personal Log')
    subparsers = parser.add_subparsers(dest='cmd')
    p_init = subparsers.add_parser('init', help="Init personal log")
    p_add = subparsers.add_parser('add', help="Clean personal log")
    p_add.add_argument('message', type=str, nargs='+')


    args = parser.parse_args()

    if args.cmd == 'init':
        init()
    elif args.cmd == 'add':
        add(args.message)
    else:
        show()

main()
