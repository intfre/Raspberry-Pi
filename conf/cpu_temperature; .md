先通过shell操作热身一下。登录树莓派之后使用指令查看CPU温度，依次输入以下指令：  
    # 进入目录  
    cd /sys/class/thermal/thermal_zone0 
    # 查看温度   
	cat temp
    # 树莓派返回   
    48692   
    从以上操作可以获得以下几点  
    【1】树莓派的CPU温度信息位于文件 /sys/class/thermal/thermal_zone0/temp中，该文件为一个只读文件。   
    【2】根据网上的资料和实际情况，返回的温度参数应该除以1000，单位为摄氏度。   
 