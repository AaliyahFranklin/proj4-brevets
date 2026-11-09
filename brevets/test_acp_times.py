

from nose.tools import assert_equal, raises
from acp_times import open_time, close_time
 
START = "2024-01-01T00:00:00"
 
 
def test_open_spans_two_ranges():
    """250km control on 400km brevet: 200/34 + 50/32 = 7:27"""
    assert_equal(open_time(250, 400, START), "2024-01-01T07:27:00+00:00")
 
 
def test_close_200km_special_rule():
    """200km finish closes at 13:30, not 13:20"""
    assert_equal(close_time(200, 200, START), "2024-01-01T13:30:00+00:00")
 
 
def test_open_control_beyond_brevet():
    """205km control on a 200km brevet is treated as 200km"""
    assert_equal(open_time(205, 200, START), open_time(200, 200, START))
 
 
def test_close_under_60km():
    """50km control: 50/20 + 1 = 3:30"""
    assert_equal(close_time(50, 200, START), "2024-01-01T03:30:00+00:00")
 
 
def test_close_350km_on_600():
    """350km control on 600km brevet: 350/15 = 23:20"""
    assert_equal(close_time(350, 600, START), "2024-01-01T23:20:00+00:00")
 
 
@raises(ValueError)
def test_invalid_brevet_distance():
    """250 is not a valid brevet distance"""
    open_time(100, 250, START)
 

