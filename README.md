# Django 制作简易博客
这个项目源于实验楼里的一个课程（[Django 搭建简易博客](https://www.shiyanlou.com/courses/487)）。

在此基础上稍作修改，并作出相关笔记，运行项目时需要先

### 1. 安装三个插件（建议在虚拟环境中运行安装，~~虽然我现在还不是很懂这个的必要性~~，就是还没遇到过相关问题）

__使用虚拟环境的原因：服务器一般会存在多个项目，若使用的相同框架的不同版本就会产生矛盾。__

virtual_my_ez_blog文件夹是我创建的一个虚拟Python环境，可以忽视。

#### 1.1 bootstrap

~~~Shell
$ pip3 install bootstrap-admin
~~~

用于美化后台管理界面，其配置文件已经写好在文件`settings.py`里的INSTALLED_APPS之中。

#### 1.2安装markdown

~~~Shell
$ pip3 install markdown
~~~

用于作为书写blog的格式。

#### 1.3 Django

~~~Shell
$ pip3 install django	
~~~

这个就不用解释了吧。



### 2.超级管理员账号与密码

**Username: refrainGo**

**Password: ,**

注：密码是英文逗号



### 3.Django项目文件说明

​	**3.1 urls.py**

​	链接入口（路由配置），关联到对应的 `views.py` 中的一个函数（或者乘坐 generic 类），访问的链接就对应一个函数。

​	**3.2 views.py**

​	处理用户发出的请求，从 `urls.py` 中对应而来，通过渲染 *templates* 中的网页可以为用户显示页面内容，比如登录后的用户名，用户请求的数据，通过其输出到页面。

​	**3.3 models.py**

​	与数据库操作相关，存入或读取数据时使用。当不使用数据库的时候，也可以当做一般的类封装文件，存储各种类的定义。

​	**3.4 forms.py**

​	表单，用户在浏览器上输入提交，对数据的验证工作以及输入框的生成等工作，都依托于此。

​	**3.5 admin.py**

​	后台文件，可以用少量的代码就拥有一个强大的后台。

​	**3.6 settings.py**

​	Django 的设置、配置文件，比如 DEBUG 的开关，静态文件的位置等等。

除了这些，还有以上目录中未提及的：

​	**3.7 templates目录**

​	`views.py` 中的函数渲染 templates 中的 html 模板，得到动态内容的网页，可以用缓存来提高渲染速度。



### 4. Djnago终端命令

	#### 	4.1创建项目

~~~Shell
$ django-admin.py startproject <your project name>
~~~



#### 	4.2 新建app

~~~shell
$ python3 manage.py startapp <your app name>
#或者
$ django-admin.py startapp <your app name>
~~~

​	

#### 	4.3 同步数据库	

~~~Shell
$ python3 manage.py makemigrations
$ python3 manage.py migrate
~~~

​	

#### 	4.4 使用开发服务器

~~~shell
$ python3 manage.py runserver <localhost:9000>
# 默认情况在 0.0.0.0:8000启动
~~~

​	

#### 	4.5 清空数据库

~~~Shell
$ python3 manage.py flush	
~~~

​	会留下空表

​	

#### 	4.6 创建超级管理员

~~~shell
$ python3 manage.py createsuperuser
# 修改密码
$ python3 manage.py changepassword username
~~~

​	依照终端提示操作即可。

​	

#### 	4.7 导入/出数据

~~~Shell
$ python3 manage.py dumpdata <your app name> > <your app name>.json
$ python3 manage.py loaddata <your app name>.json
~~~



#### 	4.8 启动Django项目终端环境

~~~Shell
$ python3 manage.py shell	
~~~



#### 	4.9 数据库命令行

~~~Shell
$ python3 manage.py dbshell
~~~



#### 	4.10 获取更多命令

~~~shell
$ python3 manage.py
~~~



### 5.后记

只是懂一点点HTML，有些地方还不理解，界面做得也还有待改善，再说吧，主要是入门Django的，第一阶段先结束了。





