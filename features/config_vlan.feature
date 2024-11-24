Feature: Configuración de VLANs
  Como administrador de red
  Quiero asegurar que las VLANs se configuren correctamente
  Para que la red funcione sin problemas.

  Scenario: Crear VLAN 10 y VLAN 20
    Given el switch está conectado
    When configuro las VLANs
    Then las VLANs deben estar presentes
