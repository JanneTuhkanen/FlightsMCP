import pytest
from test_fixtures import sample_data

def test_example():
    assert 1 + 1 == 2

def test_with_fixture(sample_data):
    """Example test using the sample_data fixture."""
    assert sample_data["name"] == "Test Item"
    assert sample_data["value"] == 42
    assert len(sample_data["items"]) == 5