import pytest
from src.managers.IdManager import IdManager

@pytest.mark.parametrize("start_count,expected", [
  (0, 1),
  (1, 2),
  (10, 11),
  (100, 101),
  (1000, 1001),
  (10000, 10001),
  (100000, 100001),
  (1000000, 1000001),
  (10000000, 10000001),
  (100000000, 100000001)
])
def test_IdGenerator_different_start_counts(start_count, expected):
  manager = IdManager(start_count)
  assert manager.genId([]) == expected

@pytest.mark.parametrize("start_count,expected", [
  (0, 1),
  (1, 2),
  (10, 11),
  (100, 101),
  (1000, 1001),
  (10000, 10001),
  (100000, 100001),
  (1000000, 1000001),
  (10000000, 10000001),
  (100000000, 100000001)
])
def test_IdGenerator_single_value(start_count, expected):
  manager = IdManager(start_count)
  assert manager.genId([{"id":1, "name":"Esteban","lastname":"Ratke"}]) == expected

@pytest.mark.parametrize("start_count,expected", [
  (0, 1),
  (1, 2),
  (10, 11),
  (100, 101),
  (1000, 1001),
  (10000, 10001),
  (100000, 100001),
  (1000000, 1000001),
  (10000000, 10000001),
  (100000000, 100000001)
])
def test_IdGenerator_data_mismatch(start_count, expected):
  manager = IdManager(start_count)
  assert manager.genId([{"id":1, "name":"Esteban","lastname":"Ratke"}, {"id":2, "name":"Magnolia","lastname":"Yundt"}]) == expected
