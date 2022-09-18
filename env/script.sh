echo ---- Updating sources ----
sudo apt-get update -y

echo ---- Installing Python ----
sudo apt-get install software-properties-common -y

echo --- Installing Apache ---
sudo apt install apache2 -y

echo ----- enabling apache proxy -------
sudo a2enmod proxy
sudo a2enmod proxy_http

echo ------- Add nology Apache Proxy File -----------
sudo cp /home/ubuntu/env/nodeapp/nology-proxy.conf /etc/apache2/sites-available
echo ls -la /etc/apache2/sites-available

echo ------- Register nology Apache Proxy File ------
sudo a2ensite nology-proxy.conf

echo -------------- Restart Apache ------------------
sudo systemctl reload apache2


echo ---- Move into app ----
cd ../vagrant/app
pwd

echo ---- install dependencies ----
sudo apt-get install python3-pandas -y
