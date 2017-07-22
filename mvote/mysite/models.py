# -*- encoding:utf-8 -*-
from django.db import models
class Mood(models.Model):
	status = models.CharField(max_length = 10,null = False)
	def __str__(self):
		return self.status


class Post(models.Model):
	mood = models.ForeignKey(Mood,on_delete = models.CASCADE)
	nickname = models.CharField(max_length = 10,verbose_name = '用户名')
	message = models.TextField(null = False,verbose_name = '张贴信息')
	pub_time = models.DateTimeField(auto_now = True,verbose_name = '张贴时间')
	enabled = models.BooleanField(default = False,verbose_name = '按键选项')
	def __str__(self):
		return self.message
	#class Meta:
	#	verbose_name = u"全部帖文"