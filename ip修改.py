from os import system


interface_name=''
ip_address=''
Subnet_mask=''
gateway=''
Gateway_metric=''

system('netsh interface ip show addresses >.\\IP配置文件.txt')
try:
    fh = open("IP配置文件.txt", "r")
except IOError:
    print("打开失败")
else:
    pass
content=fh.readlines(300)
fh.close()

del content[0]
del content[-1]

for i in range(len(content[0])):
    if content[0][i]=='\"':
        i+=1
        while content[0][i]!='\"':
            interface_name+=content[0][i]
            i+=1
        break

for i in range(len(content)):
    content[i]=content[i].split()


del content[0]
del content[0]


ip_address=content[0][-1]
Subnet_mask=content[1][-1]
Subnet_mask=Subnet_mask[:-1]
gateway=content[2][-1]
Gateway_metric=content[3][-1]


print("=============================")

print("当前网络配置：")
print("接口名称："+interface_name)
print("IP地址："+ip_address)
print("子网掩码："+Subnet_mask)
print("网关："+gateway)
print("网关跃点数："+Gateway_metric)

print("=============================")
flag=input('请问是否修改IP(y/n)：')
if flag=='y' or flag =='Y':
    ip_address=input('输入你要修改的IP：')
    
    command = 'netsh interface ip set address name=\"'+interface_name+'\" static '+ip_address+' '+Subnet_mask+' '+gateway+' '+Gateway_metric;

    #print("最终命令是："+command)
    system(command)

print('欢迎使用')
