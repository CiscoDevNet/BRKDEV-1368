# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|


    # Deploy Multiple Nodes in a single Vagrantfile

    # Node 1: IOS XE Device
    config.vm.define "iosxe1" do |node|
        node.vm.box =  "iosxe/16.06.02"

        # Gig2 connected to nsox1 Eth1/2
        # Gig3 connected to nsxo2 Eth1/2
        # Gig4 connected to iosxe2 Gig4
        # auto-config not supported.
        node.vm.network :private_network, virtualbox__intnet: "wire1", auto_config: false
        node.vm.network :private_network, virtualbox__intnet: "wire2", auto_config: false
        node.vm.network :private_network, virtualbox__intnet: "wire3", auto_config: false
      end

      # Node 2: IOS XE Device
      config.vm.define "iosxe2" do |node|
          node.vm.box =  "iosxe/16.06.02"

          # Gig2 connected to nsox1 Eth1/3
          # Gig3 connected to nsxo2 Eth1/3
          # Gig4 connected to iosxe1 Gig4
          # auto-config not supported.
          node.vm.network :private_network, virtualbox__intnet: "wire4", auto_config: false
          node.vm.network :private_network, virtualbox__intnet: "wire5", auto_config: false
          node.vm.network :private_network, virtualbox__intnet: "wire3", auto_config: false
      end

      # Node 3: NX-OS Device
      config.vm.define "nxos1" do |node|
           node.vm.box =  "nxos/7.0.3.I7.2"

          # Setting Timeout
          # config.vm.boot_timeout = 600

           # n9000v defaults to 8G RAM, but only needs 4G
           config.vm.provider "virtualbox" do |vb|
             # Customize the amount of memory on the VM:
             vb.memory = "4096"
           end

           # Eth1/2 connected to iosxe1 Gig2
           # Eth1/3 connected to iosxe2 Gig2
           # Eth1/4 connected to nxos Eth1/4
           # auto-config not supported.
             node.vm.network :private_network, virtualbox__intnet: "wire1", auto_config: false
             node.vm.network :private_network, virtualbox__intnet: "wire4", auto_config: false
             node.vm.network :private_network, virtualbox__intnet: "wire6", auto_config: false
      end

      # Node 4: NX-OS Device
      config.vm.define "nxos2" do |node|
           node.vm.box =  "nxos/7.0.3.I7.2"
	   
	   # Setting Timeout
	   # config.vm.boot_timeout = 600
	   

           # n9000v defaults to 8G RAM, but only needs 4G
           config.vm.provider "virtualbox" do |vb|
             # Customize the amount of memory on the VM:
             vb.memory = "4096"
           end

           # Eth1/2 connected to iosxe1 Gig3
           # Eth1/3 connected to iosxe2 Gig3
           # Eth1/4 connected to nxos Eth1/4
           # auto-config not supported.
             node.vm.network :private_network, virtualbox__intnet: "wire2", auto_config: false
             node.vm.network :private_network, virtualbox__intnet: "wire5", auto_config: false
             node.vm.network :private_network, virtualbox__intnet: "wire6", auto_config: false
      end


end
