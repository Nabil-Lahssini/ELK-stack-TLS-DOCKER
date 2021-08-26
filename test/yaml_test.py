import pytest, yaml, sys, os

def test_yaml_open():
    try:
        with open('instances.yml') as f:        
            d = yaml.safe_load(f)
            assert d != None    
    except IOError:
        assert False

   
def test_yaml_files_format():
    filepaths = ["/instances.yml", "/docker-compose.yml", "/create-certs.yml"]
    for fp in filepaths:
        # Split the extension from the path and normalise it to lowercase.
        ext = os.path.splitext(fp)[-1].lower()
        assert ext == ".yml"

def test_yaml_for_ELK():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filepaths = []  
    for root, dirs, files in os.walk(dir_path):
        for file in files: 
            if file.endswith('.yml'):
                filepaths.append(root+'/'+str(file))

    for fp in filepaths:
        ext = os.path.splitext(fp)[-1].lower()
        assert ext == ".yml"
