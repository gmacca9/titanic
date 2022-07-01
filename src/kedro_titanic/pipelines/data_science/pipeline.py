"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from kedro_titanic.pipelines.data_science.nodes import split_data, fit_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = split_data,
            inputs = 'de_titanic_dataset_train',
            outputs = ['X_train','X_test','y_train','y_test'],
            name = 'split_data'
        ),
        
        node(
            func = fit_model,
            inputs = ['X_train','X_test','y_train','y_test'],
            outputs = 'classifier',
            name = 'fit_model'
        )

    ])
