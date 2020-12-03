import sqlite3 as sql3
# Part A
db = sql3.connect('regression.sqlite')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS model_params")
cursor.execute("DROP TABLE IF EXISTS model_coefs")
cursor.execute("DROP TABLE IF EXISTS model_results")

cursor.execute('''CREATE TABLE model_params
            (id INTEGER, desc TEXT, param_name TEXT, value REAL)''')
cursor.execute('''CREATE TABLE model_coefs
            (id INTEGER, desc TEXT, feature_name TEXT, value REAL)''')
cursor.execute('''CREATE TABLE model_results
            (id INTEGER, desc TEXT, train_score REAL, test_score REAL)''')

db.commit()

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer

# Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)

##2. Write a function to save data to the database
def save_to_database(model_id, model_desc, db, model, X_train, X_test, y_train, y_test):
    cursor=db.cursor()
    #mfit = model.fit(X_train, y_train)
    mfit=model
    ##model params
    m_params = mfit.get_params()
    for key in m_params:
        params = (int(model_id), model_desc, key, m_params[key])
        cursor.execute('''INSERT INTO model_params 
                  (id, desc, param_name, value)
                  VALUES (?, ?, ?, ?)''', params)    
    
    
    #model_coefs
    m_coef_coef, m_coef_intercept = mfit.coef_, mfit.intercept_
    for feature_idx in np.arange(len(X_train.columns)):
        feature_name = X_train.columns[feature_idx]
        coefs = (int(model_id), model_desc, feature_name, m_coef_coef[0][feature_idx]) 
        cursor.execute('''INSERT INTO model_coefs 
                      (id, desc, feature_name, value)
                      VALUES (?, ?, ?, ?)''', coefs) 
    
    intercepts = (int(model_id), model_desc, 'intercept', m_coef_intercept[0])
    cursor.execute('''INSERT INTO model_coefs 
              (id, desc, feature_name, value)
              VALUES (?, ?, ?, ?)''', intercepts) 
    
     
    # model_results
    m_train_score = mfit.score(X_train, y_train)
    m_test_score = mfit.score(X_test, y_test)
    
    scores = (int(model_id), model_desc, m_train_score, m_test_score)
    
    cursor.execute('''INSERT INTO model_results 
          (id, desc, train_score, test_score)
          VALUES (?, ?, ?, ?)''', scores) 
    
# Fit model
baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)
save_to_database(1, 'Baseline model', db, baseline_model, X_train, X_test, y_train, y_test)

feature_cols = ['mean radius', 
                'texture error', 
                'worst radius', 
                'worst compactness', 
                'worst concavity']

X_train_reduced = X_train[feature_cols]
X_test_reduced = X_test[feature_cols]
reduced_model = LogisticRegression(solver='liblinear')
reduced_model.fit(X_train_reduced, y_train)
save_to_database(2, 'Reduced model', db, reduced_model, X_train_reduced, X_test_reduced, y_train, y_test)



penalized_model = LogisticRegression(solver='liblinear', penalty='l1', random_state=87, max_iter=150)
penalized_model.fit(X_train, y_train)
save_to_database(3, 'L1 penalty model', db, penalized_model, X_train, X_test, y_train, y_test)


# Part C

query = '''SELECT id, MAX(test_score) FROM model_results'''
q = cursor.execute(query).fetchall()
print(f"Best model id: {q[0][0]}")
print(f"Best validation score: {q[0][1]}")


query = '''SELECT feature_name, value FROM model_coefs WHERE id = 3 AND feature_name != "intercept"'''
q = cursor.execute(query).fetchall()
for feature_idx in np.arange(len(q)):
    print(f"{q[feature_idx][0]}: {q[feature_idx][1]}")
coef_str = np.array(q)
coef_float = coef_str[:, 1].astype(np.float)

query = '''SELECT feature_name, value FROM model_coefs WHERE id = 3 AND feature_name = "intercept"'''
q = cursor.execute(query).fetchall()
intercept_float = q[0][1]



test_model = LogisticRegression(solver='liblinear')
test_model.fit(X_train, y_train)

# Manually change fit parameters

test_model.coef_ =  np.array([coef_float])

test_model.intercept_ =  np.array([intercept_float]) 

test_score = test_model.score(X_test, y_test) 
print(f'Reproduced best validation score: {test_score}')

db.commit()
#close the connection
db.close()
