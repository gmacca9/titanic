"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.1
"""
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score


def split_data (df, test_size=0.3, random_state=9999):
    """Defines the training and testing datasets."""
    
    X = df.drop('Survived',axis=1)
    y = df['Survived']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                        random_state=random_state,
                                                        stratify=y)
    
    return X_train, X_test, y_train, y_test


def fit_model(X_train,X_test,y_train,y_test):
    """Fits a classifier model using a training dataset."""
    
    clf = tree.DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    
    """Predicts test set"""
    y_pred = clf.predict(X_test)
    
    """Reports score"""
    score = accuracy_score(y_test,y_pred)
    print(score)
    
    return clf