LATEX = xelatex
NAME = $(shell basename $(CURDIR))

EXPECTED_FILES = questions.tex preamble.tex title.tex

all: $(NAME)_exercises.pdf $(NAME)_solutions.pdf

%_exercises.pdf: ../utils/exercises.tex $(EXPECTED_FILES)
	$(LATEX) -jobname=$(NAME)_exercises ../utils/exercises.tex
	$(LATEX) -jobname=$(NAME)_exercises ../utils/exercises.tex
	rm *.aux *.log

%_solutions.pdf: ../utils/solutions.tex $(EXPECTED_FILES)
	$(LATEX) -jobname=$(NAME)_solutions ../utils/solutions.tex
	$(LATEX) -jobname=$(NAME)_solutions ../utils/solutions.tex
	rm *.aux *.log
