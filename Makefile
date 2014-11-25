run:
	./run.py 20
	#./run.py 15

clean:
	rm console* data_*.txt summary_plot.png data_*.png progress_plot.png fuzzy_result_all_images.png fuzzy_output_result_all_images.png *.pyc

backup:
	mkdir backup
	mv console* data_*.txt summary_plot.png data_*.png progress_plot.png fuzzy_result_all_images.png fuzzy_output_result_all_images.png backup/

progress:
	./plot_progress.py
	./plotFuzzy_progress.py 
	eog fuzzy_result_all_images.png

fuzzyplot:
	./plotFuzzyOutput.py
	eog fuzzy_output_result_all_images.png

test:
	./SimuladorTest ${FILE} 1

testManual:
	./SimuladorTest data_manual_*_fuzzy.txt 1 || echo test
testAll:
	./SimuladorTest data_ga_*_fuzzy.txt 1 || echo test
	./SimuladorTest data_pso_*_fuzzy.txt 1 || echo test
	./SimuladorTest data_sh_*_fuzzy.txt 1 || echo test
	./SimuladorTest data_sa_*_fuzzy.txt 1 || echo test

manual:
	./Simulador data_manual_fuzzy.txt 20 1

primer_sim:
	cp primer_sim/* .

