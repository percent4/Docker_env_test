TIMENOW=`date +%y.%m.%d.%H%M`

# 进行docker镜像打包
# -f 指定文件 ， -t 指定生成镜像名称 , 冒号后为版本号 ，例子 ： docker_package:17.08.01.1311
docker build -f python_env.build -t python_env:${TIMENOW} .