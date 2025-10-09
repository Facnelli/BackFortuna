import pytest
from .connection import DBconnectionHandler

@pytest.mark.skip(reason="Sensive test")
def test_create_database_engine():
    db_connection_handle = DBconnectionHandler()
    engine = db_connection_handle.get_engine()
    
    assert engine is not None