LATEX = xelatex
DIR = `pwd`
NAME = $(shell basename $(DIR))

EXERCISES = $(NAME)
SOLUTIONS = $(NAME)_solutions
OUTDIR = ..
CURDIR = .

EXPECTED_FILES = questions.tex preamble.tex title.tex

all: $(OUTDIR)/$(EXERCISES).pdf $(OUTDIR)/$(SOLUTIONS).pdf

$(OUTDIR)/$(EXERCISES).pdf: ../utils/exercises.tex $(EXPECTED_FILES) $(CURDIR)
	echo EXERCISES=$(EXERCISES)
	$(LATEX) -jobname=$(EXERCISES) -output-directory=$(OUTDIR) ../utils/exercises.tex
	$(LATEX) -jobname=$(EXERCISES) -output-directory=$(OUTDIR) ../utils/exercises.tex
	rm $(OUTDIR)/*.aux $(OUTDIR)/*.log

$(OUTDIR)/$(SOLUTIONS).pdf: ../utils/solutions.tex $(EXPECTED_FILES) $(CURDIR)
	$(LATEX) -jobname=$(SOLUTIONS) -output-directory=$(OUTDIR) ../utils/solutions.tex
	$(LATEX) -jobname=$(SOLUTIONS) -output-directory=$(OUTDIR) ../utils/solutions.tex
	rm $(OUTDIR)/*.aux $(OUTDIR)/*.log
