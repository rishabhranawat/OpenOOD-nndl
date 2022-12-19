This is a fork from the OpenOOD benchmark repository. The main goal of the modifications made here is to understand the robustness of OODD methods when there exists a variation in terms of optimizers and activation functions. We also provide scripts to perform the analysis and calculate a robustness score metric.

Following are the Jupyter Notebooks to conduct these experiments and run the analysis

#### Running MNIST/Fashion-MNIST Experiments
oodn-mnist-study.ipynb

#### Running CIFAR/CIFAR-100 Experiments
oodn-resnet-cifar-study.ipynb

#### Running OOD Analysis On Trained Models
trained-models-oodn-analysis.ipynb

#### Generating Analysis and Charts
analysis_and_charts.ipynb

#### Calculating Robustness Scores
Calculating Robustness Score.ipynb 

#### Result Files
oodn_odin_mcd_results_v1.csv (used in the paper)

#### All Metrics From Individual Runs
cifar10-study
mnist-study

Project Contributors:
Lihan Zhou
Jerry Yang
Rishabh Ranawat
