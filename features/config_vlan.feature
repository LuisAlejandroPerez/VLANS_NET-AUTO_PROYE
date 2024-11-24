Feature: Configuring VLANs and Ports
  As a network administrator
  I want to ensure that VLANs and ports are configured correctly
  In order for the network to run smoothly

  Scenario: Creating and Configuring VLANs with Port Mapping
    Given the switch is connected
    When I configure the VLANs with specific names
      | vlan_id | name      |
      | 10      | HRR       |
      | 20      | Reception |
    And I configure the ports for the VLANs
      | interface | vlan_id |
      | eth1/2   | 10      |
      | eth1/3   | 10      |
      | eth1/4   | 10      |
      | eth1/5   | 10      |
      | eth1/6   | 20      |
