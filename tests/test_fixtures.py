import pytest

@pytest.fixture
def sample_data():
    """Sample fixture providing test data.
    
    This fixture can be used across multiple tests by passing it as a parameter.
    """
    return {
        "name": "Test Item",
        "value": 42,
        "items": [1, 2, 3, 4, 5]
    }
