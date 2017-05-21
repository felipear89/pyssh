import os
from argparse import Namespace
from context import main


YAML_TEST_FILE = os.path.join(os.path.dirname(__file__), './sytssh-test.yaml')

def test_load_yaml():
    doc = main.load_yaml(YAML_TEST_FILE)
    assert len(doc.keys()) == 3
    assert doc['hosts']['project1']['prod'] == 'nix-project1.mycompany'

def test_connect(monkeypatch):
    """ Scenario with default port """
    def mockreturn(path):
        assert path == 'ssh root@nix-project1.qa.mycompany -p 22'
    monkeypatch.setattr(main.os, 'system', mockreturn)
    doc = main.load_yaml(YAML_TEST_FILE)
    namespace = Namespace(environment='qa', project='project1')
    main.connect(doc, namespace)

def test_connect_with_port(monkeypatch):
    """ Scenario with specified port """
    def mockreturn(path):
        assert path == 'ssh root@localhost -p 23'
    monkeypatch.setattr(main.os, 'system', mockreturn)
    doc = main.load_yaml(YAML_TEST_FILE)
    namespace = Namespace(environment='local', project='project2')
    main.connect(doc, namespace)

def test_get_port_with_port():
    port = main.get_port('localhost:123', '22')
    assert port == '123'

def test_get_port_without_port():
    port = main.get_port('localhost', '22')
    assert port == '22'