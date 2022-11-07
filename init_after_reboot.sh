sed -i s/deb.debian.org/mirrors.huaweicloud.com/g /etc/apt/sources.list
apt update
apt install -y wget curl python3-pip