WORKSHEETS =\
			complex_algebra.pdf\
			sets_of_solutions.pdf\
			linear_systems.pdf\
			worksheet_4.pdf\
			eigenvalues_and_eigenvectors.pdf\
			proof_by_induction.pdf\
			trusses.pdf\
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
		 trusses/fixed.pdf\
		 trusses/pin.pdf\
		 trusses/roller.pdf\
		 trusses/mj_1.pdf\
		 trusses/mj_2.pdf\
		 trusses/mj_3.pdf\
		 trusses/mj_4.pdf\
		 trusses/mj_5.pdf\
		 trusses/ms_1.pdf\
		 trusses/ms_2.pdf\
		 trusses/ms_3.pdf\
		 trusses/ms_4.pdf\
		 trusses/roof.pdf\
		 trusses/howe.pdf\
		 trusses/pratt.pdf\
		 trusses/bridge.pdf\
		 #

all: $(WORKSHEETS)

%.pdf: % $(FIGURES)
	cd $< && make --makefile=../Makefile.ws

%.pdf: %.svg
	inkscape -f $< -A $@
