from behave import given, when, then
from ncclient import manager

SWITCH_IP = "192.168.1.1"
USER = "admin"
PASSWORD = "admin"

@given('el switch está conectado')
def step_impl(context):
    context.connection = manager.connect(
        host=SWITCH_IP, port=830, username=USER, password=PASSWORD, hostkey_verify=False
    )
    assert context.connection.connected

@when('configuro las VLANs')
def step_impl(context):
    netconf_config = """
    <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
            <bd-items>
                <bd-items>
                    <BD-list>
                        <fabEncap>vlan-10</fabEncap>
                        <name>VLAN10</name>
                    </BD-list>
                    <BD-list>
                        <fabEncap>vlan-20</fabEncap>
                        <name>VLAN20</name>
                    </BD-list>
                </bd-items>
            </bd-items>
        </System>
    </config>
    """
    context.connection.edit_config(target='running', config=netconf_config)

@then('las VLANs deben estar presentes')
def step_impl(context):
    netconf_filter = """
    <filter>
        <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
            <bd-items>
                <bd-items>
                    <BD-list>
                    </BD-list>
                </bd-items>
            </bd-items>
        </System>
    </filter>
    """
    response = context.connection.get(netconf_filter)
    print(response)
    assert "vlan-10" in response.xml
    assert "vlan-20" in response.xml
