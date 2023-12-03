import pytest
import sys
from src.managers.IdManager import generateId
sys.path.append(r'C:\Users\dabro\Desktop\wrk\projekty\projekt-backendapi\backend\src')

@pytest.fixture
def idTestData1():
  return [
    {"id":1, "name":"Esteban","lastname":"Ratke"},
    {"id":2, "name":"Magnolia","lastname":"Yundt"},
    {"id":3, "name":"Mikayla","lastname":"Kub"},
    {"id":4, "name":"Fay","lastname":"Schmeler"},
    {"id":5, "name":"Jensen","lastname":"Adams"},
    {"id":6, "name":"Pauline","lastname":"Aufderhar"},
    {"id":7, "name":"Braxton","lastname":"Bayer"},
    {"id":8, "name":"Sienna","lastname":"Hintz"},
    {"id":9, "name":"Tyra","lastname":"Daugherty"},
    {"id":10, "name":"Sterling","lastname":"Ankunding"},
    {"id":11, "name":"Aletha","lastname":"Kris"},
    {"id":12, "name":"Myrna","lastname":"Goyette"},
    {"id":13, "name":"Izaiah","lastname":"Haag"}
  ]
@pytest.fixture
def idTestData2():
  return [
    {"id":1, "name":"Esteban","lastname":"Ratke"},
    {"id":2, "name":"Magnolia","lastname":"Yundt"},
    {"id":3, "name":"Mikayla","lastname":"Kub"},
    {"id":4, "name":"Fay","lastname":"Schmeler"},
    {"id":5, "name":"Jensen","lastname":"Adams"},
    {"id":6, "name":"Pauline","lastname":"Aufderhar"},
    {"id":7, "name":"Braxton","lastname":"Bayer"},
    {"id":8, "name":"Sienna","lastname":"Hintz"}
  ]

def test_IdGenerator_1(idTestData1):
  assert generateId(idTestData1) == 14
def test_IdGenerator_2(idTestData2):
  assert generateId(idTestData2) == 9