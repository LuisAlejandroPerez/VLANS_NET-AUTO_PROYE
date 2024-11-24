from ncclient import manager

SWITCH_IP = "192.168.1.1"
USER = "admin"
PASSWORD = "admin"

def test_vlan_created():
    with manager.connect(host=SWITCH_IP, port=830, username=USER, password=PASSWORD, hostkey_verify=False) as m:
        netconf_filter = """
        <filter>
            <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
                <vlan-items/>
            </System>
        </filter>
        """
        response = m.get(netconf_filter)
        assert "<id>10</id>" in response.xml
        assert "<id>20</id>" in response.xml
