# ansible-laradock-kubernetes
Ansible playbook to setup docker containers for laravel application using laradock. Platform is debian/ubuntu. 

To setup docker containers for laravel app, check command - 

	ansible-playbook -i devserver get_laradock.yml -b   (-b equivalents to sudo)

To setup kubernetes cluster (single node),  check command - 

	ansible-playbook -i devserver install_kubernetes.yml 

Change the sample IP in the inventory file :)

install ansible ?

	sudo apt-add-repository -y ppa:ansible/ansible
	sudo apt-get update
	sudo apt-get install -y ansible
