resource "azurerm_network_security_rule" "allow_ssh_world" {
  name                        = "ssh-open"
  priority                    = 100
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "*"
  destination_port_range      = "22"
  source_address_prefix       = "*"
  destination_address_prefix  = "*"
  resource_group_name         = azurerm_resource_group.demo.name
  network_security_group_name = azurerm_network_security_group.demo.name
}

resource "azurerm_storage_account" "sa" {
  name                     = "demostorageopen"
  resource_group_name      = azurerm_resource_group.demo.name
  location                 = "eastus"
  account_tier             = "Standard"
  account_replication_type = "LRS"
  allow_blob_public_access = true
}
