# UFRN-SIC2-SERVER

InfoSystem workshop project for II SIC event at CERES-UFRN, Caicó/RN, Brazil

https://sites.google.com/site/siceres2016/

<b>Software prerequisite</b>

1. Git
2. Python 3.4
3. Visual Studio Code


<b>Setup Python 3.4 enviroment on Ubuntu 12.04:</b>

`sudo apt-get install git`

`sudo add-apt-repository ppa:fkrull/deadsnakes`

`sudo apt-get update`

`sudo apt-get install python3.4`

`cd /opt`

`sudo wget https://bootstrap.pypa.io/get-pip.py`

`sudo python3.4 get-pip.py`


<b>To install Visual Studio Code download it at:</b>

http://code.visualstudio.com/


<b>Get and Run infosystem instructions</b>

Go or create your project dir, example:

`cd`

`mkdir Dev`

`cd Dev`

Download and install infosystem project:

`git clone https://github.com/fdoliveira/ufrn-sic2-server`: Download project

`cd ufrn-sic2-server`: Enter project dir

`sudo pip3 install infosystem`: Download infosystem package

`sudo mkdir /etc/infosystem`: Create infosystem dir

`sudo cp etc/infosystem.conf /etc/infosystem/`: Copy infosystem.conf file to infosystem etc dir

`sudo cp etc/policy.json /etc/infosystem/`: Copy policy.json file to infosystem etc dir

`python3.4 app.py`: Run app
