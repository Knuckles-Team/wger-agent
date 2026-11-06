"""Measurement and measurement-category ids are UUID strings on current wger servers."""

import inspect

import pytest

from wger_agent.api.api_client_body import Api


@pytest.mark.parametrize(
    ("method", "param"),
    [
        ("get_measurement", "measurement_id"),
        ("update_measurement", "measurement_id"),
        ("delete_measurement", "measurement_id"),
        ("get_measurement_category", "category_id"),
        ("delete_measurement_category", "category_id"),
        ("create_measurement", "category"),
    ],
)
def test_measurement_ids_accept_uuid_strings(method, param):
    annotation = inspect.signature(getattr(Api, method)).parameters[param].annotation
    assert "str" in str(annotation)
