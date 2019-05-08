if type yum > /dev/null 2> /dev/null
then
  echo "FEDORA"
  sudo yum install gcc openssl-devel bzip2-devel
  sudo dnf install python3
  sudo dnf install python3-pip
  sudo yum install python3-devel
  sudo yum install libxslt-devel libxml2-devel
elif type apt-get > /dev/null 2> /dev/null
then
  echo "UBUNTU"
  sudo apt install build-essential
  sudo apt-get install python3
  sudo apt-get install python3-pip
  sudo apt-get install python3-venv
  sudo apt-get install python3-lxml
fi
python3 -m venv venv
source venv/bin/activate
pip3 install wheel
pip3 install -r requirements.txt
sudo ./sentinelbackend/chkrootkit2
deactivate
