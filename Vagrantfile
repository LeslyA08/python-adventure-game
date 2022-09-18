Vagrant.configure("2") do |config|
    config.vm.box = "generic/ubuntu2010"
    config.vm.network "private_network", ip: "192.168.56.10"
    config.hostsupdater.aliases = ["nology.training"]
    config.vm.provider "virtualbox" do |vb|
      config.vm.synced_folder "app/", "/home/vagrant/app/"
    end
    config.vm.provision "shell", path: "env/script.sh"
  end 
  
# Vmware
# --------------------------------------------------------------

# Vagrant.configure("2") do |config|
  
# Provisioning NodeJS App
#   config.vm.define "nodeapp" do |nodeapp|
#     nodeapp.vm.box = "spox/ubuntu-arm"
#     nodeapp.vm.network "private_network", ip: "192.168.56.10"
#     nodeapp.hostsupdater.aliases = ["nology.training"]
#     nodeapp.vm.provider "vmware_fusion" do |vb|
#       nodeapp.vm.synced_folder "app/", "/home/vagrant/app/"
#       nodeapp.vm.synced_folder "env/", "/home/vagrant/env"
#     end
#     nodeapp.vm.provision "shell", inline: <<-SHELL
#       systemctl disable apt-daily.service
#       systemctl disable apt-daily.timer
#       sudo apt remove unattended-upgrades -y
#     SHELL
#     nodeapp.vm.provision "shell", path: "env/nodeapp/script.sh"
#   end
# end