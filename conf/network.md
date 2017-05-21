意外防止：
	sudo mv /etc/network/interfaces /boot/interfaces
	sudo ln -s /boot/interfaces /etc/network/interfaces

无线配置：
安装完成的基本系统默认没有无线的工具，需要安装和配置。   
1. 安装wpasupplicant  
	$ sudo apt-get install wireless-tools wpasupplicant 
2. 树莓派3自带无线网卡，因此不需要插入usb无线网卡，否则需要首先检查USB无线网卡是否已经正确识别 
	$ lsusb 
3. 使用如下命令获得wifi设置： 

	$ wpa_passphrase SSID_name SSID_password 

回显如下：
    network={  
        ssid="SSID_name"  
        #psk="SSID_password" 
        psk=4b7084a26fea96aaf67518820cc1151fb8f47c5fc0674cd6e877a2ecd70b596e  
	}  

借助 cat 等命令，复制这段回显并保存到自己的配置文件中 
	sudo nano /etc/wpa_supplicant/wpa_supplicant.conf 
4. 配置/etc/network/interfaces， 
	sudo nano /etc/network/interfaces 
	如果自动获得IP地址，配置内容如下：
	allow-hotplug wlan0  
	auto wlan0  
	iface wlan0 inet dhcp  
	pre-up wpa_supplicant -B w -D wext -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf  
	post-down killall -q wpa_supplicant

    auto lo eth0
	iface lo inet loopback
	iface eth0 inet dhcp
	iface wlan0 inet dhcp
	wpa-conf /home/ubuntu/conf/wpa.conf

如果设置固定IP地址，配置内容如下：
	allow-hotplug wlan0  
	auto wlan0  
	iface wlan0 inet static  
    address 192.168.1.137  
    netmask 255.255.255.0  
    network 192.168.1.0  
    broadcast 192.168.1.255  
    gateway 192.168.1.1  
    wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf  

连接网络命令。或者重新启动系统可自动连接无线。

	sudo ifup wlan0 