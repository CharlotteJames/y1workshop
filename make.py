#!/usr/bin/env python

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
    'trusses',
    'entropy', 
]

def run_command(cmdline, **kwargs):
    print("---------------")
    print("     Running %s" % cmdline)
    print("---------------")
    subprocess.check_call(cmdline, **kwargs)

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
