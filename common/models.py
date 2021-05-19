# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2021/05/12 15:10

from django.db import models

class User(models.Model):

    id = models.AutoField(primary_key=True,verbose_name='主键')

    username = models.CharField(max_length=32,verbose_name='用户名')

    password = models.CharField(verbose_name='密码',max_length=64)

    def __str__(self):
        return '%s' %self.username
