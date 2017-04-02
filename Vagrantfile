# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "bento/ubuntu-14.04"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # When using django run python manage.py runserver 10.0.0.100:8000
  config.vm.network :forwarded_port, guest: 8000, host: 8000

  # When using django over stunnel to test https
  config.vm.network :forwarded_port, guest: 8443, host: 8443

  # This is for Postgresql database ssh connection
  config.vm.network :forwarded_port, guest: 5432, host: 65432

  # This is for MongoDB database connection
  config.vm.network :forwarded_port, guest: 28017, host: 28018

  # config.vm.provision :shell, :path => "bootstrap.sh"

  # This will make sure either chef-solo or chef-client is
  # installed on the VM and is required for chef provisioning.
  # In order to use omnibus plugin, make sure you install the
  # plugin first: vagrant plugin install vagrant-omnibus
  config.omnibus.chef_version = "11.10.0"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network :private_network, ip: "10.0.0.100"

  config.vm.define "blookvm" do |cfg|

    cfg.vm.provision :chef_solo do |chef|
      chef.custom_config_path = "Vagrantfile.chef"
      chef.cookbooks_path = ['cookbooks', 'cookbooks/vagrant-hadoop/cookbooks']

      chef.add_recipe "apt"
      chef.add_recipe "build-essential"
      chef.add_recipe "curl"
      chef.add_recipe "git"
      chef.add_recipe "openssl"
      chef.add_recipe "python"
      chef.add_recipe "vim"
      chef.add_recipe "mysql"


      chef.json = {
      rbenv: {
        user_installs: [{
          user: 'vagrant',
          rubies: ["2.1.2"],
          global: "2.1.2",
          gems: {
            "2.1.2" => [
              { name: "bundler" }
            ]
          }
        }]
      },
      mysql: {
        server_root_password: ''
      }
    }



    end

    # This will install all the things
    cfg.vm.provision "shell",
      path: "bootstrap.sh", privileged: false
    
  end

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # If true, then any SSH connections made will enable agent forwarding.
  # Default value: false
  # config.ssh.forward_agent = true

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"
  # config.vm.synced_folder "/home/psychok7/code/private/", "/src", :owner => "vagrant"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Don't boot with headless mode
  #   vb.gui = true
  #
  #   # Use VBoxManage to customize the VM. For example to change memory:
  #   vb.customize ["modifyvm", :id, "--memory", "1024"]
  # end
  #
  # View the documentation for the provider you're using for more
  # information on available options.
  
  config.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  end

  # Enable provisioning with CFEngine. CFEngine Community packages are
  # automatically installed. For example, configure the host as a
  # policy server and optionally a policy file to run:
  #
  # config.vm.provision "cfengine" do |cf|
  #   cf.am_policy_hub = true
  #   # cf.run_file = "motd.cf"
  # end
  #
  # You can also configure and bootstrap a client to an existing
  # policy server:
  #
  # config.vm.provision "cfengine" do |cf|
  #   cf.policy_server_address = "10.0.2.15"
  # end

  # This will fix the issue with mounting folders
  # in Linux guest OS
  # config.vm.provision "shell",
  #   inline: "sudo ln -s /opt/VBoxGuestAdditions-*/lib/VBoxGuestAdditions /usr/lib/VBoxGuestAdditions"


  # Enable provisioning with Puppet stand alone.  Puppet manifests
  # are contained in a directory path relative to this Vagrantfile.
  # You will need to create the manifests directory and a manifest in
  # the file default.pp in the manifests_path directory.
  #
  # config.vm.provision "puppet" do |puppet|
  #   puppet.manifests_path = "manifests"
  #   puppet.manifest_file  = "site.pp"
  # end

  # Enable provisioning with chef solo, specifying a cookbooks path, roles
  # path, and data_bags path (all relative to this Vagrantfile), and adding
  # some recipes and/or roles.
  #
  # config.vm.provision "chef_solo" do |chef|
  #   chef.cookbooks_path = "../my-recipes/cookbooks"
  #   chef.roles_path = "../my-recipes/roles"
  #   chef.data_bags_path = "../my-recipes/data_bags"
  #   chef.add_recipe "mysql"
  #   chef.add_role "web"
  #
  #   # You may also specify custom JSON attributes:
  #   chef.json = { :mysql_password => "foo" }
  # end

  # Enable provisioning with chef server, specifying the chef server URL,
  # and the path to the validation key (relative to this Vagrantfile).
  #
  # The Opscode Platform uses HTTPS. Substitute your organization for
  # ORGNAME in the URL and validation key.
  #
  # If you have your own Chef Server, use the appropriate URL, which may be
  # HTTP instead of HTTPS depending on your configuration. Also change the
  # validation key to validation.pem.
  #
  # config.vm.provision "chef_client" do |chef|
  #   chef.chef_server_url = "https://api.opscode.com/organizations/ORGNAME"
  #   chef.validation_key_path = "ORGNAME-validator.pem"
  # end
  #
  # If you're using the Opscode platform, your validator client is
  # ORGNAME-validator, replacing ORGNAME with your organization name.
  #
  # If you have your own Chef Server, the default validation client name is
  # chef-validator, unless you changed the configuration.
  #
  #   chef.validation_client_name = "ORGNAME-validator"
end
