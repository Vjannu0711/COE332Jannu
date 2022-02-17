from analyze_water import calculate_turbidity
from analyze_water import calculate_time
from analyze_water import main
import pytest
import json

testdata = {}
testdata['info'] = []
testdata['info'].append({'calib':1,'detect':2})
testdata['info'].append({'calib':2,'detect':3})

# UNIT TESTS FOR CALCULATE TURBIDITY FUNCTION
def test_calculate_turbidity():
    assert calculate_turbidity(testdata['info'],'calib','detect',0) == 2
    assert calculate_turbidity(testdata['info'],'calib','detect',1) == 6
    assert isinstance(calculate_turbidity(testdata['info'],'calib','detect',0), float) == True
def test_calculate_turbidity_exceptions():
    with pytest.raises(IndexError):
        calculate_turbidity( [ {'calib' : 1, 'detect' : 2} ], 'calib',' detector', 1)
    with pytest.raises(NameError):
        calculate_turbidiy( [ {'calib' : 1, 'detect' : 2} ], 'cali', 'detect', 1)
#def test_calc_turb_exceptions():
#    with pytest.raises(ValueError):
#        calculate_turbidity(testdata['info'], 'calib', 'detect', 2)

# UNIT TESTS FOR CALCULCATE TIME FUNCTION
def test_calc_time():
    assert calculate_time(3) == 54.37945872310939
    assert calculate_time(4) == 68.61923698304129
    assert calculate_time(5) == 79.66446710032875
    assert isinstance(calculate_time(4), float) == True
def test_calculate_time_exceptions():
    with pytest.raises(TypeError):
        calculate_time([ { 'cali' : 1}, 1 ])
    with pytest.raises(NameError):
        calculate_tim([ {'cali' : 1, 'detect' : 2} ], 1)
