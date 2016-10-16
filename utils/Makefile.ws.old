.PHONY: clean

# These should be set before calling:
#
# NAME = particle_statics
# QFIGS =
# AFIGS =

TEX = xelatex
QUESTIONS = questions.tex
UTILS = ../utils/utils.tex ../utils/shortlst.sty
QDEPS = $(QFIGS) $(QUESTIONS) $(UTILS)
ADEPS = $(QDEPS) $(AFIGS)

all: $(NAME)_exercises.pdf $(NAME)_solutions.pdf

clean:
	rm -f *.aux *.log *.out *.pdf
	rm -f images/*.pdf

$(NAME)_exercises.pdf: exercises.tex $(QDEPS)
	$(TEX) $<
	$(TEX) $<
	cp exercises.pdf $@
	rm exercises.pdf *.aux *.log

$(NAME)_solutions.pdf: solutions.tex $(QDEPS) $(ADEPS)
	$(TEX) $<
	$(TEX) $<
	cp solutions.pdf $@
	rm solutions.pdf *.aux *.log

images/%.pdf: images/%.svg
	inkscape -f "$(PWD)/$<" -A "$(PWD)/$@"

images/%.pdf: images/%.py
	./$< $@
