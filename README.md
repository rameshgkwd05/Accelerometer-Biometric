# Accelerometer-Biometric
Recognize users of mobile devices from accelerometer data ( Accelerometer Biometric Competition on kaggle)

A course Project for 'CS 725: Foundations of Machine Learning'

#Description:
You can find the description of problem statement at
https://www.kaggle.com/c/accelerometer-biometric-competition

#How To Run the Code:

Assumption: You have train.csv and test.csv in the same folder as other project files

1) Run device_count.py

2) Run extractMeanVar.py

3) Run trimmingdata.py

4) Now you can execute any classifier code. Just look for the required files are there in the same folder.

#Our Approaches
We devised following approaches for solving the problem:

1. Naive Bayes

2. Nearest Neighbors

3. Quadratic Discriminative Analysis ( Similar to LDA)

4. Support Vector Machines

#File related to each approach:

1] Naive Bayes

	1. extractMeanVar.py
	2. naive_bayes.py
	3. naive_bayes_Random.py


2] Nearest Neighbors

	1. trimmingdata.py
	2. device_count.py
	3. KNearestNeighbour.py

3] Quadratic Discriminative Analysis ( Similar to LDA)

	1. qda.py

4] Support Vector Machines

	1. svm_mean.py
	2. svm_modified.py

