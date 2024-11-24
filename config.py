from ncclient import manager

SWITCH_IP = "192.168.1.1"
USER = "admin"
PASSWORD = "admin"

def test_capabilities():
    with manager.connect(host=SWITCH_IP, port=830, username=USER, password=PASSWORD, hostkey_verify=False) as m:
        print("\n--- Capabilities ---")
        for capability in m.server_capabilities:
            print(capability)
