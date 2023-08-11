echo "Welcome to the Gen OS Installer. Please wait while Gen OS gets ready for you. You may continue to use your computer until Gen OS is ready."
sleep 8
sudo apt update
sudo apt install simplescreenrecorder pitivi nala audacity kdeconnect python3-pip -y
wget -O onlyoffice.deb "https://download.onlyoffice.com/install/desktop/editors/linux/onlyoffice-desktopeditors_amd64.deb"
sudo apt install ./onlyoffice.deb -y
sudo apt install wget gpg -y
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
sudo rm -f packages.microsoft.gpg
sudo apt install apt-transport-https -y
sudo apt update
sudo apt install code -y
sudo apt purge 'libreoffice*' -y
sudo apt install git -y
git clone https://github.com/crazycheetah42/GenOS-Tools.git
sudo mv GenOS-Tools/adwaita-d.jpg /usr/share/backgrounds/
gsettings set org.gnome.desktop.background picture-uri /usr/share/backgrounds/adwaita-d.jpg
gsettings set org.gnome.desktop.interface gtk-theme Yaru-dark
gsettings set org.gnome.desktop.wm.preferences theme Yaru-dark
mv GenOS-tools ~/Desktop/
