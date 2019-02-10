echo "Installing dependencies"
sudo apt-get update
sudo apt-get install python3 python3-pip -y


echo "Installing Python Libraries"
sudo pip3 install -r requirements.txt
