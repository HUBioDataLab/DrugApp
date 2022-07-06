# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import sys
import pandas as pd
from datetime import datetime
import sklearn
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, matthews_corrcoef
from sklearn.model_selection import cross_validate
from sklearn.metrics import make_scorer
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier


print(datetime.now())

#Data:
df=pd.read_csv("{0}_app_unapp_drug_indication.csv".format(sys.argv[1]),sep=',')

X = df.iloc[:,15:199]
y = df["Label"]


#Cross-validation:
def RF_cv(model_name, X, y, classifier):

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    
    clf = classifier 
    
    scoring = {"accuracy":"accuracy","balanced_accuracy":"balanced_accuracy","precision":"precision","precision_weighted":"precision_weighted","recall":"recall","recall_weighted":"recall_weighted","f1":"f1","f1_weighted":"f1_weighted","mcc":make_scorer(matthews_corrcoef)}  

    result = sklearn.model_selection.cross_validate(clf, X, y, cv=skf, scoring=scoring)
   
    return print (result) 
   
     
clf_optimized_parameters = RandomForestClassifier(n_estimators = 200, max_depth =16, min_samples_split = 2, max_features ='sqrt', min_samples_leaf = 2, class_weight= "balanced", random_state=42)                  


#Evaluation metrics (For this part, unique drug data was utilized and provided in a separate script-not to repeat patent, molecular, physicochemical features for different trials of the same drug):
#model_optimized = RF_cv("optimized_model",X,y,clf_optimized_parameters)


#Model:
clf = RandomForestClassifier(n_estimators = 200, max_depth = 16, min_samples_split = 2, max_features = 'sqrt', min_samples_leaf = 2, class_weight= "balanced", random_state=42) 


clf.fit(X, y) 


#The prediction for a disease group:
df_test=pd.read_csv("{0}_to_be_predicted.csv".format(sys.argv[1]),sep=',')
X_test=df_test.iloc[:,5:189]


#To align features of X and X_test:
cols=X.columns.to_list()
X_test=X_test[cols]


#Prediction scores (column 1:the probability of approval of a drug, column 0:the probability of unapproval of a drug):
clf_predict=clf.predict_proba(X_test)
df_clf_predict = pd.DataFrame(clf_predict)


df_test_part_1=df_test[['Name', 'Conditions', 'NCT_Number', 'Phases']]


df_test_part_1.reset_index(drop=True, inplace=True)
df_clf_predict.reset_index(drop=True, inplace=True)
df_concat = pd.concat([df_test_part_1, df_clf_predict], axis=1)


df_concat.columns=['Name',    'Conditions',    'NCT_Number',        'Phases', 'Prob_unapproval', 'Prob_approval']


#Save:
df_concat.to_csv("Predictions_{0}.csv".format(sys.argv[1]),index=None)


print(datetime.now())




