"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from kedro_titanic.pipelines.pre_processing.nodes import preprocess_titanic


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = preprocess_titanic,
            inputs = 'raw_titanic_dataset_train',
            outputs = 'pp_titanic_dataset_train',
            name = 'preprocess_titanic'
        ),
        
        node(
            func = preprocess_titanic,
            inputs = 'titanic_dataset_test',
            outputs = 'pp_titanic_dataset_test',
            name = 'preprocess_titanic_test'
        )
    ])
