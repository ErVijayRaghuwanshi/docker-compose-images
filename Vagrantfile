# Kubernetes 1 Master + 1 Worker on VirtualBox
# Compatible with Ubuntu 22.04 LTS (Jammy)

Vagrant.configure("2") do |config|
  # Use a lightweight Ubuntu box
  config.vm.box = "ubuntu/jammy64"

  # Disable automatic box updates
  config.vm.box_check_update = false

  # Common setup for both master and worker
  config.vm.provider "virtualbox" do |vb|
    vb.memory = 2048
    vb.cpus = 2
  end

  # Master Node Configuration
  config.vm.define "k8s-master" do |master|
    master.vm.hostname = "k8s-master"
    master.vm.network "private_network", ip: "192.168.56.10"

    master.vm.provision "shell", inline: <<-SHELL
      # Disable swap (required by kubeadm)
      sudo swapoff -a
      sudo sed -i '/ swap / s/^/#/' /etc/fstab

      # Update system and install dependencies
      sudo apt-get update -y
      sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release

      # Add Kubernetes APT repository
      sudo curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-archive-keyring.gpg
      echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list

      # Install Kubernetes and containerd
      sudo apt-get update -y
      sudo apt-get install -y kubelet kubeadm kubectl containerd
      sudo apt-mark hold kubelet kubeadm kubectl

      # Configure containerd
      sudo mkdir -p /etc/containerd
      containerd config default | sudo tee /etc/containerd/config.toml
      sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml
      sudo systemctl restart containerd
      sudo systemctl enable containerd

      # Initialize the control plane (Master)
      sudo kubeadm init --apiserver-advertise-address=192.168.56.10 --pod-network-cidr=10.244.0.0/16

      # Configure kubectl for vagrant user
      mkdir -p /home/vagrant/.kube
      sudo cp -i /etc/kubernetes/admin.conf /home/vagrant/.kube/config
      sudo chown vagrant:vagrant /home/vagrant/.kube/config

      # Install Flannel network plugin
      sudo -u vagrant kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml

      # Output join command for worker
      echo "Run this command on the worker node to join the cluster:"
      kubeadm token create --print-join-command
    SHELL
  end

  # Worker Node Configuration
  config.vm.define "k8s-worker" do |worker|
    worker.vm.hostname = "k8s-worker"
    worker.vm.network "private_network", ip: "192.168.56.11"

    worker.vm.provision "shell", inline: <<-SHELL
      sudo swapoff -a
      sudo sed -i '/ swap / s/^/#/' /etc/fstab

      sudo apt-get update -y
      sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release

      sudo curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-archive-keyring.gpg
      echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list

      sudo apt-get update -y
      sudo apt-get install -y kubelet kubeadm kubectl containerd
      sudo apt-mark hold kubelet kubeadm kubectl

      sudo mkdir -p /etc/containerd
      containerd config default | sudo tee /etc/containerd/config.toml
      sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml
      sudo systemctl restart containerd
      sudo systemctl enable containerd

      echo "Worker ready to join cluster. Use the join command from master node."
    SHELL
  end
end
