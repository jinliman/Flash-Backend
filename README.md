# Python EWS Backend API

**Installation**

	# install required packages
    sudo apt-get install python3 python3-dev python3-pip python3-pylibmc memcached
    
	# clone the repository 
    sudo git clone https://gituser@github.com/devmaster23/Flask-Backend-Api.git
	
    # copy the config file to the required destination
    sudo mkdir -p /etc/ews/
	sudo cp etc/ews/cfg /etc/ews/cfg
	
	# install python3 requirements 
	pip3 install -r requirements.txt
    
    # download Maxmind's GeoIP database and copy it to the right destination
    cd var/lib/GeoIP/
	./download.sh
	sudo cp *.dat /var/lib/GeoIP/
