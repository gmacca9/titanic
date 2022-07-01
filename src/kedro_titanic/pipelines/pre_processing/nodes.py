"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.18.1
"""
import pandas as pd
# import sklearn as skl
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier

def preprocess_titanic(df: pd.DataFrame):
    """ This function cleanses the Titanic raw_data, removing unused columns. """
    
    # Remove unused columns 
    df = df.drop(columns=['Name','Ticket','PassengerId','Cabin'])
    
    return df