import pytest
from .connection import Connection

@pytest.mark.skip(reason="Database dependent testing")
def test_create_database_engine():
    conection = Connection()
    engine = conection.get_engine()

    assert engine is not None
