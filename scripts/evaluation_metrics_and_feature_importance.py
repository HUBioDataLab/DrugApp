# -*- coding: utf-8 -*-
import sys
import pandas as pd
from datetime import datetime
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, matthews_corrcoef
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import make_scorer
import matplotlib.pyplot as plt
from sklearn.inspection import permutation_importance


print(datetime.now())


#Data:
df=pd.read_csv(r"..\datasets\training_datasets\{0}_training_feature_vectors.csv".format(sys.argv[1]),sep=',') 

X = df.iloc[:,2:186]
y = df["Label"]


#Cross-validation:
def RF_cv(model_name, X, y, classifier):

    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    
    clf = classifier 
    
    scoring = {"accuracy":"accuracy","balanced_accuracy":"balanced_accuracy","precision":"precision","precision_weighted":"precision_weighted","recall":"recall","recall_weighted":"recall_weighted","f1":"f1","f1_weighted":"f1_weighted","mcc":make_scorer(matthews_corrcoef)}  

    result = sklearn.model_selection.cross_validate(clf, X, y, cv=skf, scoring=scoring)
   
    return print (result) 
   
     
clf_optimized_parameters = RandomForestClassifier(n_estimators = 200, max_depth =16, min_samples_split = 2, max_features ='sqrt', min_samples_leaf = 2, class_weight= "balanced", random_state=42)                  


#Evaluation metrics:
model_optimized = RF_cv("optimized_model",X,y,clf_optimized_parameters)


# Model:
clf = RandomForestClassifier(n_estimators = 200, max_depth = 16, min_samples_split = 2, max_features = 'sqrt', min_samples_leaf = 2, class_weight= "balanced", random_state=42) 


clf.fit(X, y) 


# RF feature importance (MDI):
feature_importances = pd.DataFrame(clf.feature_importances_, index = X.columns,
                                    columns=['importance']).sort_values('importance', ascending=False)


feature_importances .reset_index(inplace=True)
feature_importances  = feature_importances .rename(columns = {'index':'Features'})


#Save:
feature_importances.to_csv("results_feature_importances_MDI_{0}.csv".format(sys.argv[1]),index=None)


# Permutation feature importance:
result = permutation_importance(clf, X, y, n_repeats=10, random_state=42, n_jobs=2)

sorted_idx = result.importances_mean.argsort()[-10:]

fig, ax = plt.subplots(figsize=(6, 3))

ax.boxplot(result.importances[sorted_idx].T, vert=False, labels=X.columns[sorted_idx])

fig.tight_layout()

plt.show()


print(datetime.now())

