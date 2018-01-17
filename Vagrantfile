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

        config.vm.network :forwarded_port, guest: 22, host: 2122, id: 'ssh', auto_correct: true
        config.vm.network :forwarded_port, guest: 830, host: 2123, id: 'netconf', auto_correct: true
        config.vm.network :forwarded_port, guest: 80, host: 2124, id: 'restconf', auto_correct: true
        config.vm.network :forwarded_port, guest: 443, host: 2125, id: 'restconf-ssl', auto_correct: true
        config.vm.network :forwarded_port, guest: 8443, host: 2126, id: 'iox', auto_correct: true

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

          config.vm.network :forwarded_port, guest: 22, host: 2222, id: 'ssh', auto_correct: true
          config.vm.network :forwarded_port, guest: 830, host: 2223, id: 'netconf', auto_correct: true
          config.vm.network :forwarded_port, guest: 80, host: 2224, id: 'restconf', auto_correct: true
          config.vm.network :forwarded_port, guest: 443, host: 2225, id: 'restconf-ssl', auto_correct: true
          config.vm.network :forwarded_port, guest: 8443, host: 2226, id: 'iox', auto_correct: true

          # Gig2 connected to nsox1 Eth1/3
          # Gig3 connected to nsxo2 Eth1/3
          # Gig4 connected to iosxe1 Gig4
          # auto-config not supported.
          node.vm.network :private_network, virtualbox__intnet: "wire4", auto_config: false
          node.vm.network :private_network, virtualbox__intnet: "wire5", auto_config: false
          node.vm.network :private_network, virtualbox__intnet: "wire3", auto_config: false
      end

      # Node 3: IOS-XE Device
      config.vm.define "iosxe3" do |node|
           node.vm.box =  "iosxe/16.06.02"

           config.vm.network :forwarded_port, guest: 22, host: 2322, id: 'ssh', auto_correct: true
           config.vm.network :forwarded_port, guest: 830, host: 2323, id: 'netconf', auto_correct: true
           config.vm.network :forwarded_port, guest: 80, host: 2324, id: 'restconf', auto_correct: true
           config.vm.network :forwarded_port, guest: 443, host: 2325, id: 'restconf-ssl', auto_correct: true
           config.vm.network :forwarded_port, guest: 8443, host: 2326, id: 'iox', auto_correct: true

           # Eth1/2 connected to iosxe1 Gig2
           # Eth1/3 connected to iosxe2 Gig2
           # Eth1/4 connected to nxos Eth1/4
           # auto-config not supported.
             node.vm.network :private_network, virtualbox__intnet: "wire1", auto_config: false
             node.vm.network :private_network, virtualbox__intnet: "wire4", auto_config: false
             node.vm.network :private_network, virtualbox__intnet: "wire6", auto_config: false
      end

      # Node 4: IOS-XE Device
      config.vm.define "iosxe4" do |node|
           node.vm.box =  "iosxe/16.06.02"

           config.vm.network :forwarded_port, guest: 22, host: 2422, id: 'ssh', auto_correct: true
           config.vm.network :forwarded_port, guest: 830, host: 2423, id: 'netconf', auto_correct: true
           config.vm.network :forwarded_port, guest: 80, host: 2424, id: 'restconf', auto_correct: true
           config.vm.network :forwarded_port, guest: 443, host: 2425, id: 'restconf-ssl', auto_correct: true
           config.vm.network :forwarded_port, guest: 8443, host: 2426, id: 'iox', auto_correct: true

           # Eth1/2 connected to iosxe1 Gig3
           # Eth1/3 connected to iosxe2 Gig3
           # Eth1/4 connected to nxos Eth1/4
           # auto-config not supported.
             node.vm.network :private_network, virtualbox__intnet: "wire2", auto_config: false
             node.vm.network :private_network, virtualbox__intnet: "wire5", auto_config: false
             node.vm.network :private_network, virtualbox__intnet: "wire6", auto_config: false
      end

      # Node 5: IOS-XE Device
      config.vm.define "iosxe5" do |node|
           node.vm.box =  "iosxe/16.06.02"

           config.vm.network :forwarded_port, guest: 22, host: 2522, id: 'ssh', auto_correct: true
           config.vm.network :forwarded_port, guest: 830, host: 2523, id: 'netconf', auto_correct: true
           config.vm.network :forwarded_port, guest: 80, host: 2524, id: 'restconf', auto_correct: true
           config.vm.network :forwarded_port, guest: 443, host: 2525, id: 'restconf-ssl', auto_correct: true
           config.vm.network :forwarded_port, guest: 8443, host: 2526, id: 'iox', auto_correct: true

           # Eth1/2 connected to iosxe1 Gig3
           # Eth1/3 connected to iosxe2 Gig3
           # Eth1/4 connected to nxos Eth1/4
           # auto-config not supported.
           #  node.vm.network :private_network, virtualbox__intnet: "wire2", auto_config: false
           #  node.vm.network :private_network, virtualbox__intnet: "wire5", auto_config: false
           #  node.vm.network :private_network, virtualbox__intnet: "wire6", auto_config: false
      end

      config.vm.provision "ansible" do |ansible|
        ansible.playbook = "ansible/playbooks/ansible_provision.yaml"
        ansible.inventory_path = "./hosts"
      end

end
