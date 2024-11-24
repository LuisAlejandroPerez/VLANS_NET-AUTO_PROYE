from behave import given, when, then
from ncclient import manager

@given('the switch is connected')
def step_impl(context):
    print("✓ El switch está conectado correctamente")
    context.connection = manager.connect(
        host="192.168.1.1",
        port=830,
        username="admin",
        password="admin",
        hostkey_verify=False
    )

@when('I configure the VLANs with specific names')
def step_impl(context):
    print("\nConfigurando VLANs con los siguientes parámetros:")
    for row in context.table:
        print(f"- VLAN {row['vlan_id']}: {row['name']}")

    netconf_config = '''
    <config>
        <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
            <bd-items>
                <bd-items>
    '''
    
    for row in context.table:
        vlan_id = row['vlan_id']
        name = row['name']
        netconf_config += f'''
                    <BD-list>
                        <fabEncap>vlan-{vlan_id}</fabEncap>
                        <name>{name}</name>
                    </BD-list>
        '''
    
    netconf_config += '''
                </bd-items>
            </bd-items>
        </System>
    </config>
    '''
    
    context.connection.edit_config(target='running', config=netconf_config)
    print("✓ VLANs configuradas exitosamente")

@when('I configure the ports for the VLANs')
def step_impl(context):
    print("\nAsignando puertos a las VLANs:")
    for row in context.table:
        print(f"- Puerto {row['interface']} -> VLAN {row['vlan_id']}")

    netconf_config = '''
    <config>
        <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
            <intf-items>
                <phys-items>
    '''
    
    for row in context.table:
        interface = row['interface']
        vlan_id = row['vlan_id']
        netconf_config += f'''
                    <PhysIf-list>
                        <id>{interface}</id>
                        <adminSt>up</adminSt>
                        <accessVlan>vlan-{vlan_id}</accessVlan>
                    </PhysIf-list>
        '''
    
    netconf_config += '''
                </phys-items>
            </intf-items>
        </System>
    </config>
    '''
    
    context.connection.edit_config(target='running', config=netconf_config)
    print("✓ Puertos asignados correctamente")
