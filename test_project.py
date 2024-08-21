from project import check_commandla, percentage, simulate_round
import pytest

def test_check_commandla():
    with pytest.raises(SystemExit):
        check_commandla()

def test_generate_integer():
    assert percentage(40) == "FAIL"
    assert percentage(50) == "PASS"

def test_simulate_round():
    with pytest.raises(TypeError):
        simulate_round()
    """ This only work with my desktop VScode
    assert simulate_round(1,2) == None
    assert simulate_round(1,1) == None
    assert simulate_round(10,2) == None
    assert simulate_round(1,10) == None"""
