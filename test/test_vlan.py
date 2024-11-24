import pytest
from unittest.mock import Mock, patch
from ncclient import manager

def test_vlan_creation():
    mock_connection = Mock()
    vlans = [
        {"vlan_id": "10", "name": "HRR"},
        {"vlan_id": "20", "name": "Reception"}
    ]

    expected_config = '''
    <config>
        <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
            <bd-items>
                <bd-items>
                    <BD-list>
                        <fabEncap>vlan-10</fabEncap>
                        <name>HRR</name>
                    </BD-list>
                    <BD-list>
                        <fabEncap>vlan-20</fabEncap>
                        <name>Reception</name>
                    </BD-list>
                </bd-items>
            </bd-items>
        </System>
    </config>
    '''
    
    mock_connection.edit_config.return_value = True
    result = mock_connection.edit_config(target='running', config=expected_config)
    
    assert result is True
    mock_connection.edit_config.assert_called_once()
    call_args = mock_connection.edit_config.call_args[1]
    assert call_args['target'] == 'running'
    assert 'vlan-10' in call_args['config']
    assert 'vlan-20' in call_args['config']
    assert 'HRR' in call_args['config']
    assert 'Reception' in call_args['config']
