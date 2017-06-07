import os
from argparse import Namespace
from context import sytssh


YAML_TEST_FILE = os.path.join(os.path.dirname(__file__), './sytssh-test.yaml')

def test_load_yaml():
    doc = sytssh.load_yaml(YAML_TEST_FILE)
    assert len(doc.keys()) == 3
    assert doc['hosts']['checkout']['prod'] == 'checkout.mycompany'
    assert doc['hosts']['checkout']['qa'] == 'checkout.qa.mycompany:23'

def test_connect_specified_port(monkeypatch):
    def mockreturn(path):
        assert path == 'ssh root@checkout.qa.mycompany -p 23'
    
    monkeypatch.setattr(sytssh.os, 'system', mockreturn)
    
    doc = sytssh.load_yaml(YAML_TEST_FILE)
    namespace = Namespace(environment='qa', project='checkout', n=0)
    sytssh.connect(doc, namespace)

def test_connect_default_port(monkeypatch):
    def mockreturn(path):
        assert path == 'ssh root@payments.mycompany -p 22'
    
    monkeypatch.setattr(sytssh.os, 'system', mockreturn)
    
    doc = sytssh.load_yaml(YAML_TEST_FILE)
    namespace = Namespace(environment='prod', project='payments', n=0)
    sytssh.connect(doc, namespace)

def test_connect_(monkeypatch):
    def mockreturn(path):
        assert path == 'ssh root@payments.mycompany -p 22'
    
    monkeypatch.setattr(sytssh.os, 'system', mockreturn)
    
    doc = sytssh.load_yaml(YAML_TEST_FILE)
    namespace = Namespace(environment='prod', project='payments', n=0)
    sytssh.connect(doc, namespace)