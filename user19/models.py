from django.db import models

# Create your models here.

# class UserInfo(models.Model):
#     user = models.CharField(max_length=32)
#     pwd = models.CharField(max_length=32)

class User(models.Model):


    #用户表

    gender = (
        ('male','男'),
        ('female','女'),
    )

######################
#注意，这里的用户名是网络上的用户名
#并非真实名字，所以没有设置为unique
#
######################




    #姓名
    name = models.CharField('姓名',max_length=128, unique=True)
    #年龄
    age = models.PositiveIntegerField(verbose_name='年龄', default=1)
    #密码
    password = models.CharField('密码',max_length=256)
    #邮箱
    email = models.EmailField('邮箱',unique=True)
    #性别
    sex = models.CharField('性别',max_length=32, choices=gender,default='男')
    #用户创建时间
    c_time = models.DateTimeField('用户创建时间',auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'






