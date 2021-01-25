Target:	        Fit 3 models (XGB, LGBM, CATBoost) for all datasets (regression/ classification).

Instuctions: 1. Preprocess the data for the models (convert types, splitting etc, but Not
		 normalize etc.).
	     2. Use deafault hyper-parameters for models (if changes aren't necessary).
	     3. You havn't to reach best score with the models.
	     4. Use K-Fold (K=5) for every model. total score is mean of losses
		 (over test and train folds).
	     5. Use mse loss for regression and log-loss for classification.
	     6. You may use data_info for understanding what is the target of every dataset

structure: Read and Preprocess all data files, then run 3 models over every dataset. 
	   Save your results.