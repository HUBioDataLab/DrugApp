# DrugApp: A Method for Machine Learning-based Prediction of Drug Approval
In this repository, we presented a programmatic tool called “DrugApp”, that utilize available clinical trial and patent related data together with physicochemical and molecular properties of drugs candidate compounds within a random forest classifier to predict their potential of getting regulatory approval as drugs for certain indications. The major contributions of this work are summarized below:

* Presenting the method "DrugApp" which can predict drug approvals prospectively with reasonably high performance.
* Preparing drug development-related property datasets (including features from patents, clinical trials, and physicochemical + molecular properties) by gathering and organizing data from multiple resources, which will be useful for further studies in terms of training and testing development-centric prediction models.
* Identifying features that are important for drug approvals, which can be evaluated by experts to increase the efficiency of drug development procedures.

The methodology followed while developing DrugApp is shown below.

<img width="1201" alt="DrugApp_Figure1" src="https://user-images.githubusercontent.com/13165170/178265643-25759b13-cb62-414d-89b9-9a619eb2e5a2.png">


## Programming Environment, Folders/Files and Dependencies

**Descriptions of folders and files:**

*	**datasets** folder includes benchmark datasets constructed by applying extensive filtering operations. 
    * **prospective_analysis_datasets** contains both raw feature files and ready to use feature vectors for drugs in ongoing clinical trials (as of May 2022).
    * **training_datasets** contains training datasets of DrugApp (both raw feature files and ready to use feature vectors) for regulatorily approved and unapproved drugs. The column named "Label" indicates the approval status of the drug (i.e., 1:approved, 0:unapproved).
*	**scripts** contains Python scripts required for the construction of DrugApp prediction models, as well as their performance evaluation via validation experiments, and feature importance identification.
*	**results** contains the output of each DrugApp model considering both the model performance scores and approval prediction results for drugs in ongoing clinical trials (as of May 2022). 

**Dependencies:**

* Python 3.7.4
* Scikit-learn 1.0.2
* Pandas 1.0.3
* Numpy 1.19.5
* Matplotlib 3.2.2

**Step-by-step operation:**
1. We recommend to use conda platform for installing dependencies properly. After installation of appropriate [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) version for your operating system, install dependencies as below:
```
conda install -c anaconda scikit-learn=1.0.2
conda install -c anaconda pandas=1.0.3
pip install numpy==1.19.5
pip install matplotlib==3.2.2
```
2. Clone this repository.
3. Set the location of the "scripts" folder (presented in the DrugApp main folder) as the current working directory, and run the corresponding script to predict drug approval for disease class of your interest. 


## How to Run DrugApp

**Example commands to run the scripts for predicting drug approvals for disease group of your interest:**
   
For predicting drug approval for a specific disease group, run the "rf_model_for_predicting_drug_approval.py" script by defining the name of the drug_indication dataset (i.e., "Alimentary", "Infective", "Blood", "Dermatological", "Heart", "Hormonal", "Immunological", "Musculoskeletal", "Neoplasms", "Nervous", "Rare", "Respiratory", "Sensory", and "Urinary") as an argument, e.g.:
   
```
python rf_model_for_predicting_drug_approval.py Rare
```

The output will be a csv file, name starting with "predictions" (e.g. predictions_Rare).

**Example commands to run the scripts for evaluation metrics and feature importances:**
   
For calculating the performance of models and determining feature importances on a specific disease group dataset, run the "evaluation_metrics_and_feature_importance.py" script by giving the name of the dataset (i.e., "Alimentary", "Infective", "Blood", "Dermatological", "Heart", "Hormonal", "Immunological", "Musculoskeletal", "Neoplasms", "Nervous", "Rare", "Respiratory", "Sensory", and "Urinary") as an argument, e.g.:
   
```
python evaluation_metrics_and_feature_importance.py Rare
```
   
## License

Copyright (C) 2022 HUBioDataLab

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.


