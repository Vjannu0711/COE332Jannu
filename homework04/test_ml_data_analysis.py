import json
from ml_data_analysis import *
import pytest

data = {}
data['info'] = []
data['info'].append( {'mass': 1} )
data['info'].append( {'mass': 2} )
def test_compute_average_mass():
    assert isinstance(compute_average_mass(data['info'], 'mass'), float) == True
    assert compute_average_mass(data['info'], 'mass') == 1.5
    assert isinstance(compute_average_mass(data['info'],'mass'), str) == False
def test_compute_average_mass_exceptions():
    with pytest.raises(KeyError):
        compute_average_mass([{'mass':1}],'mss')
    with pytest.raises(NameError):
        compute_average_mas([{'mass':1}],'mass')
def test_check_hemisphere():
    assert check_hemisphere(1.5,2)== 'Northern & Eastern'
    assert check_hemisphere(-0.5,2)== 'Southern & Eastern'
    assert check_hemisphere(2,-0.5)== 'Northern & Western'
    assert check_hemisphere(1,1)== 'Northern & Eastern'
def test_check_hemisphere_exceptions():
    with pytest.raises(NameError):
        check_hemispher([{2, 0.5}])
def test_count_classes():
    assert isinstance(count_classes(data['info'], 'mass'),dict)==True
    assert isinstance(count_classes(data['info'], 'mass'),str)==False
    assert isinstance(count_classes(data['info'], 'mass'),float)==False
def test_count_classes_exceptions():
    with pytest.raises(KeyError):
        count_classes([{'mass':1}],'mas')
    with pytest.raises(NameError):
        count_clases([{'mass':1}],'mass')
    
