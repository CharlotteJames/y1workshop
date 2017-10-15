#!/usr/bin/env python3

from __future__ import print_function

import os.path
import subprocess

worksheets = [
    'complex_algebra', 
    'dynamics', 
    'eigenvalues_and_eigenvectors', 
    'groups', 
    'linear_systems', 
    'odes', 
    'odes_linear_operators',
    'probability', 
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

def run_command(cmdline, **kwargs):
    print("---------------")
    print("     Running %s" % cmdline)
    print("---------------")
    try:
        subprocess.check_call(cmdline, **kwargs)
    except FileNotFoundError:
        message = "Subcommand failed: is '%s' installed and on PATH?"
        raise NotInstalledError(message % (cmdline[0],))

def make_worksheet(name):
    pdfname = name + '.pdf'
    if os.path.exists(pdfname):
        print(pdfname, 'already exists')
    else:
        make_figures(name)
        run_latex(name)

def make_figures(name):
    filenames = [os.path.join(name, f) for f in os.listdir(name)]
    svgfiles = [f for f in filenames if f.endswith('.svg')]
    for svgname in svgfiles:
        pdfname = os.path.splitext(svgname)[0] + '.pdf'
        if os.path.exists(pdfname):
            print(pdfname, 'already exists, skipping...')
        else:
            run_inkscape(svgname, pdfname)

def run_inkscape(svgname, pdfname):
    cmdline = ['inkscape', '-f', svgname, '-A', pdfname]
    run_command(cmdline)
    if not os.path.exists(pdfname):
        raise ValueError('Unable to handle svg file "%s"' % svgname)

def run_latex(name):
    cmdline = ['xelatex', '-jobname=' + name, '-output-directory=..', '../utils/exercises.tex']
    run_command(cmdline, cwd=name)
    run_command(cmdline, cwd=name)
    cmdline = ['xelatex', '-jobname=' + name + '_solutions', '-output-directory=..', '../utils/solutions.tex']
    run_command(cmdline, cwd=name)
    run_command(cmdline, cwd=name)
    clean()

def clean():
    print('Removing latex rubbish')
    extensions = '.aux', '.log'
    filenames = os.listdir('.')
    todelete = [f for f in filenames for e in extensions if f.endswith(e)]
    for filename in todelete:
        os.remove(filename)

def main(worksheet=None):
    if worksheet is None or worksheet == 'all':
        if worksheet == 'all':
            for filename in os.listdir('.'):
                if filename.endswith('.pdf'):
                    os.remove(filename)
        for name in worksheets:
            make_worksheet(name)
    else:
        os.remove(worksheet + '.pdf')
        make_worksheet(worksheet)


if __name__ == "__main__":
    import sys
    main(*sys.argv[1:])
