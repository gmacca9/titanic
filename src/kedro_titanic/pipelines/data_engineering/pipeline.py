"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from kedro_titanic.pipelines.data_engineering.nodes import data_engineering


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = data_engineering,
            inputs = 'pp_titanic_dataset_train',
            outputs = 'de_titanic_dataset_train',
            name = 'dataengineering_titanic'
        ),

        node(
            func = data_engineering,
            inputs = 'pp_titanic_dataset_test',
            outputs = 'de_titanic_dataset_test',
            name = 'dataengineering_titanic_test'
        )
    ])