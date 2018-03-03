# PEBA - Python EWS Backend API

**Installation**

	# install required packages
    sudo apt-get install python3 python3-dev python3-pip python3-pylibmc memcached
    
	# clone the repository 
    sudo git clone git@github.com:dtag-dev-sec/PEBA.git 
	cd PEBA
	
    # copy the config file to the required destination
    sudo mkdir -p /etc/ews/
	sudo cp etc/ews/peba.cfg /etc/ews/peba.cfg
	
	# install python3 requirements 
	pip3 install -r requirements.txt
    
    # download Maxmind's GeoIP database and copy it to the right destination
    cd var/lib/GeoIP/
	./download.sh
	sudo cp *.dat /var/lib/GeoIP/
