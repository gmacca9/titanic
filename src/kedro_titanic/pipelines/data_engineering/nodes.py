"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.1
"""

import pandas as pd


def data_engineering(df: pd.DataFrame):
    
    """ Converts the sex of the person to a integer 
    in two separated columns. """
    
    df = pd.get_dummies(df, columns=['Sex'])
    df = df.rename(columns = {'Sex_0':'Male', 'Sex_1':'Female'})

    """ Converts the null embark data to the most 
    commom port of embarkation. """
    
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    
    """ Converts the embarked data to a integer 
        in three separated columns. """
    
    df = pd.get_dummies(df, columns=['Embarked'])
    df = df.rename(columns = {'Embarked_C':'Emb_C', 'Embarked_Q':'Emb_Q', 
                              'Embarked_S':'Emb_S'})
    
    """ Converts the null age data to the age's mean. """

    df['Age'] = df['Age'].fillna(df['Age'].mean())
    
    return df