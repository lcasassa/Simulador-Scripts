run:
	./run.py 20
	#./run.py 15

clean:
	rm data_*.txt summary_plot.png data_*.png progress_plot.png fuzzy_result_all_images.png fuzzy_output_result_all_images.png *.pyc

backup:
	mkdir backup
	mv data_*.txt summary_plot.png data_*.png progress_plot.png fuzzy_result_all_images.png fuzzy_output_result_all_images.png backup/

progress:
	./plot_progress.py
	./plotFuzzy_progress.py 
	eog fuzzy_result_all_images.png

fuzzyplot:
	./plotFuzzyOutput.py
	eog fuzzy_output_result_all_images.png

test:
	./SimuladorTest ${FILE} 1

testAll:
	./SimuladorTest data_ga_*_fuzzy.txt 1 || echo next
	./SimuladorTest data_pso_*_fuzzy.txt 1 || echo test
	./SimuladorTest data_sh_*_fuzzy.txt 1 || echo test
	./SimuladorTest data_sa_*_fuzzy.txt 1 || echo test

primer_sim:
	cp primer_sim/* .

