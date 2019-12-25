### PyCharm连接Docker镜像进行开发

1. Dockerfile为python_env.build，用build.sh生成Docker镜像；
2. py文件用于测试Python环境是否导入成功，docker_python_test_file.py是用tornado写的HTTP请求服务，f_write.py用于测试文件写入功能；
3. 该Docker镜像含有jieba和tornado模块；
4. PyCharm连接Docker镜像进行开发：

- 本地（或者服务器端）的Docker是否启动，连接方式为: ip:2375；
- 选择镜像为读者自己打包的镜像（用build.sh生成的镜像）；
- 选择Python路径为: /usr/local/Python-3.7.0/python
- 注意本地项目路径与Docker项目路径的对应关系；