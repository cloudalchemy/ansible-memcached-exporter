import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service(host):
    s = host.service("memcached_exporter")
    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    sockets = [
        "tcp://127.0.0.1:9150"
    ]
    for socket in sockets:
        s = host.socket(socket)
        assert s.is_listening
