def add(x, y):
    return x + y
def mul(x,y):return x * y
def sub(x,y): return x - y

def test_add():
    assert add(2, 3) == 5  # Assertion
def test_mul():assert mul(2,3)==6
def test_sub():assert sub(2,3)==-1
