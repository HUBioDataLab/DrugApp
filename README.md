# DrugApp: A Comprehensive Benchmark for Machine Learning-based Prediction of Drug Approval
In this study/repository, we presented a programmatic tool called “DrugApp”, that utilize available clinical trial- and patent-related data together with physicochemical and molecular features of drugs candidate compounds within a random forest classifier to predict their potential of getting approval as drugs for certain indications. The major contributions of our study are summarized below:
* We showed the high potential of our method for predicting drug approval. 
* We proposed comprehensive datasets, which can be useful for further computational studies as benchmarks.
* We presented important features for drug approval prediction, which can be used by both commercial and non-commercial entities to increase the efficiency of drug development procedures.
The modeling methodology of this study is summarized below.

![Modeling Methodology](https://user-images.githubusercontent.com/108183756/177561886-7b15e9b2-74bf-4ee6-9092-146d9cb3c836.PNG)

## Programming Environment and Files
**Descriptions of folders and files:**

*	**datasets** folder includes benchmark datasets constructed by applying extensive filtering operations. 
    * **raw_datasets** folder contains FDA-approved and FDA-unapproved drug indication pairs together with all features. One-hot encoded version of categorical features are also provided. FDA-approved and FDA-unapproved drugs are represented in the column called "Label" in binary classification format (i.e., 1:approved, 0:unapproved).
    * **prospective_analysis_datasets** folder contains drug indication pairs together with all features for ongoing clinical trials.
    * **training_datasets** folder contains unique FDA-approved and FDA-unapproved drugs together with randomly selected indications and all other features used for the determination of evaluation metrics and feature importances. 
*	**scripts** folder includes script files required for the construction of model for predicting drug approval as well as for the determination of evaluation metrics and feature importances.
*	**results** folder contains prediction results of each disease group for ongoing clinical trials. 

**Dependencies:**

* Python 3.7.4
* Scikit-learn 1.0.2
* Pandas 1.0.3
* Numpy 1.19.5
* Matplotlib 3.2.2

**Step-by-step operation:**
1. We highly recommend you to use conda platform for installing dependencies properly. After installation of appropriate [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) version for your operating system, install dependencies as below:
```
conda install -c anaconda scikit-learn=1.0.2
conda install -c anaconda pandas=1.0.3
pip install numpy==1.19.5
pip install matplotlib==3.2.2
```
2. Clone this repository.
3. Set the location of the "scripts" folder present in "DrugApp" folder as the current working directory, and run the corresponding script to predict drug approval for disease class of your interest. 

**Example commands to run the scripts for predicting drug approval for disease class of your interest:**
   
For predicting drug approval for a specific disease group, run the "rf_model_for_predicting_drug_approval.py" script for RF algorithm by defining the name of the drug_indication dataset (i.e., "Alimentary", "Anti-infective", "Blood", "Dermatological", "Heart", "Hormonal", "Immunological", "Musculoskeletal", "Neoplasms", "Nervous", "Rare", "Respiratory", "Sensory", and "Urinary") as parameter, e.g.:
   
```
python rf_model_for_predicting_drug_approval.py Rare
```

The output will be a csv (comma-separated values) file, named as "Predictions" (e.g. Predictions_Rare).

**Example commands to run the scripts for evaluation metrics and feature importances:**
   
For determining evaluation metrics and feature importances for a specific disease group, run the "evaluation_metrics_and_feature_importance.py" script by defining the name of the unique_drug dataset (i.e., "Alimentary", "Anti-infective", "Blood", "Dermatological", "Heart", "Hormonal", "Immunological", "Musculoskeletal", "Neoplasms", "Nervous", "Rare", "Respiratory", "Sensory", and "Urinary") as parameter, e.g.:
   
```
python evaluation_metrics_and_feature_importance.py Rare
```
   
## License

Copyright (C) 2022 HUBioDataLab

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.


