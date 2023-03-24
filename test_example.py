import example

def test_add():
    assert example.add(2, 3) == 5
    assert example.add(0, 0) == 0
    assert example.add(-1, 1) == 0
