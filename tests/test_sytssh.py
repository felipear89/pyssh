import os
from argparse import Namespace
from context import main


YAML_TEST_FILE = os.path.join(os.path.dirname(__file__), './sytssh-test.yaml')

def test_load_yaml():
    doc = main.load_yaml(YAML_TEST_FILE)
    assert len(doc.keys()) == 3
    assert doc['project1']['host']['prod'] == 'nix-project1.mycompany'

def test_connect(monkeypatch):
    def mockreturn(path):
        assert path == 'ssh root@nix-project1.qa.mycompany -p 32768'
    monkeypatch.setattr(main.os, 'system', mockreturn)
    doc = main.load_yaml(YAML_TEST_FILE)
    namespace = Namespace(environment='qa', project='project1')
    main.connect(doc, namespace)

