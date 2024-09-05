import os
import sys
import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score, recall_score, f1_score, precision_score,roc_auc_score
from sklearn.model_selection import GridSearchCV
from src.exception import customException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as fileobj:
            pickle.dump(obj, fileobj)
    except Exception as e:
        raise customException(e, sys)

def evaluate_model(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(model.values())[i]
            para = param[list(models.key())[i]]
            
            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)
            y_pred_train = model.predict(X_train)
            y_pred_test = model.predict(X_test)
            train_model_score = accuracy_score(y_train, y_pred_train)
            test_model_score = accuracy_score(y_test, y_pred_test)
            train_model_f1_score = f1_score(y_train, y_pred_train)
            test_model_f1_score = f1_score(y_test, y_pred_test)
            train_model_roc_auc_score = roc_auc_score(y_train, y_pred_train)
            test_model_roc_auc_score = roc_auc_score(y_test, y_pred_test)
            score = [test_model_f1_score, test_model_roc_auc_score]
            report[list(models.keys())[i]] = score
            return report
            
    except Exception as e:
        raise customException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise customException(e, sys)