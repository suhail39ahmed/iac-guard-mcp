resource nsg 'Microsoft.Network/networkSecurityGroups@2023-09-01' = {
  name: 'nsg-demo'
  location: 'eastus'
  properties: {
    securityRules: [
      {
        name: 'ssh-open'
        properties: {
          priority: 100
          direction: 'Inbound'
          access: 'Allow'
          protocol: 'Tcp'
          sourceAddressPrefix: '*'
          destinationPortRange: '22'
          destinationAddressPrefix: '*'
          sourcePortRange: '*'
        }
      }
    ]
  }
}
