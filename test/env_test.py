import sys ,os, pytest
  
def test_env_readable():
    x=0
    try:
        with open('.env') as f:        
            assert f is not None        
    except IOError:
        assert False  

def test_env_isExists():
    x= os.stat('.env').st_size
    assert x == 1157