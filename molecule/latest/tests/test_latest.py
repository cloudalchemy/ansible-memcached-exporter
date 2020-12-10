import pytest
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("files", [
    "/etc/systemd/system/memcached_exporter.service",
    "/usr/local/bin/memcached_exporter"
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file
