LATEX = xelatex
NAME = complex_algebra

all: $(NAME)_exercises.pdf $(NAME)_solutions.pdf

%_exercises.pdf: exercises.tex questions.tex
	$(LATEX) -jobname=$(NAME)_exercises exercises.tex

%_solutions.pdf: solutions.tex questions.tex
	$(LATEX) -jobname=$(NAME)_solutions solutions.tex

clean:
	rm *.aux *.log *.pdf
