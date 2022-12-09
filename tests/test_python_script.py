# test_db_handler.py
import pytest
from rc_management_gui.db_handler import db_handler
from datetime import datetime

#from hypothesis import given
#from hypothesis import strategies as some

testdata = [
    (1, 1, 5, datetime(2001, 12, 11)),
    (0, 1, 3, datetime(2002, 12, 11)),
]

@pytest.mark.parametrize("a,b,c,t", testdata)
def test_add_and_get_log(a,b,c,t):
    db = db_handler(":memory:")
    db.add_log(a,b,c,t)
    result = db.get_recent_sensor_data()
    assert result[0][0] == a and result[0][1] == b  and result[0][2] == c
