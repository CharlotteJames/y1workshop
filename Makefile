WORKSHEETS =\
			complex_algebra.pdf\
			sets_of_solutions.pdf\
			linear_systems.pdf\
			worksheet_4.pdf\
			#

FIGURES =\
		 sets_of_solutions/mass_horizontal.pdf\
		 sets_of_solutions/mass_slope.pdf\
		 sets_of_solutions/mass_wall.pdf\
		 sets_of_solutions/supports.pdf\
		 sets_of_solutions/supports2.pdf\
		 linear_systems/supports2.pdf\
		 linear_systems/supports3.pdf\
		 linear_systems/moments.pdf\
		 worksheet_4/fig_1.pdf\
		 worksheet_4/fig_2.pdf\
		 worksheet_4/fig_3.pdf\
		 worksheet_4/fig_4.pdf\
		 worksheet_4/fig_5.pdf\
		 #

all: $(WORKSHEETS)

%.pdf: % $(FIGURES)
	cd $< && make --makefile=../Makefile.ws

%.pdf: %.svg
	inkscape -f $< -A $@
