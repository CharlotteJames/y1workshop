WORKSHEETS =\
			complex_algebra.pdf\
			sets_of_solutions.pdf\
			#

all: $(WORKSHEETS)

%.pdf: %
	cd $< && make --makefile=../Makefile.ws
