#!/usr/bin/env python3

from __future__ import print_function

import os
import os.path
import subprocess
import argparse

worksheets = [
    'complex_algebra', 
    'dynamics', 
    'eigenvalues_and_eigenvectors', 
    'groups', 
    'linear_systems', 
    'odes', 
    'odes_linear_operators',
    'probability', 
    'proof_techniques', 
    'proof_by_induction', 
    'random_variables', 
    'sets_of_solutions', 
    'statics',
    'statics_new',
    'trusses',
    'entropy', 
]

class NotInstalledError(Exception):
    pass

def run_command(cmdline, options,**kwargs):
    if options.dryrun:
        print('Would run:', cmdline)
        return
    print("---------------")
    print("     Running %s" % cmdline)
    print("---------------")
    try:
        subprocess.check_call(cmdline, **kwargs)
    except FileNotFoundError:
        message = "Subcommand failed: is '%s' installed and on PATH?"
        raise NotInstalledError(message % (cmdline[0],))

def make_worksheet(name, options):
    pdfname = name + '.pdf'
    # Skip rebuilding?
    if not options.force:
        if os.path.exists(pdfname) and is_newer_dir(pdfname, name):
            print('Up to date:', pdfname)
            return
    print('Making', name, '...')
    make_figures(name, options)
    run_latex(name, options)

def make_figures(name, options):
    filenames = [os.path.join(name, f) for f in os.listdir(name)]
    svgfiles = [f for f in filenames if f.endswith('.svg')]
    for svgname in svgfiles:
        pdfname = os.path.splitext(svgname)[0] + '.pdf'
        if not options.force:
            if os.path.exists(pdfname) and is_newer(pdfname, svgname):
                print('Uo to date:', pdfname, '...')
                continue
        run_inkscape(svgname, pdfname, options)

def all_subfiles(dirname):
    '''Yields all filepaths under directory dirname'''
    for root, dirs, files in os.walk(dirname):
        for fname in files:
            yield os.path.join(root, fname)

def is_newer(path1, path2):
    '''True if path1 is a newer file than path2'''
    return os.path.getmtime(path1) > os.path.getmtime(path2)

def is_newer_dir(filepath, dirpath):
    '''True if filepath is newer than all files in dirpath'''
    ftime = os.path.getmtime(filepath)
    return all(ftime > os.path.getmtime(p) for p in all_subfiles(dirpath))

def run_inkscape(svgname, pdfname, options):
    cmdline = ['inkscape', '-f', svgname, '-A', pdfname]
    run_command(cmdline, options)
    if not os.path.exists(pdfname):
        raise ValueError('Unable to handle svg file "%s"' % svgname)

def run_latex(name, options):
    cmdline = ['xelatex', '-jobname=' + name, '-output-directory=..', '../utils/exercises.tex']
    run_command(cmdline, options, cwd=name)
    run_command(cmdline, options, cwd=name)
    cmdline = ['xelatex', '-jobname=' + name + '_solutions', '-output-directory=..', '../utils/solutions.tex']
    run_command(cmdline, options, cwd=name)
    run_command(cmdline, options, cwd=name)
    clean(options)

def clean(options):
    print('Removing latex rubbish')
    extensions = '.aux', '.log'
    filenames = os.listdir('.')
    todelete = [f for f in filenames for e in extensions if f.endswith(e)]
    for filename in todelete:
        if options.dryrun:
            print('Would remove:', todelete)
            continue
        os.remove(filename)

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--dryrun', action='store_true',
                        help='do nothing; print the commands that would run')
    parser.add_argument('-f', '--force', action='store_true',
                        help='ignore timestamps and rebuild everything')
    parser.add_argument('targets', metavar='TARGET', type=str, nargs='*',
                        help='worksheets to build (as directory names)')

    options = parser.parse_args(args)

    targets = options.targets
    if targets == [] or targets == ['all']:
        targets = worksheets

    for name in targets:
        make_worksheet(name, options)


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
