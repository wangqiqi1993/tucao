#-*- encoding:utf-8 -*-
from captcha.fields import CaptchaField
from django import forms
from mysite import models
class ContactForm(forms.Form):
	CITY = [

			    ['安徽','安徽省'],
                ['北京','北京市'],
                ['重庆','重庆市'],
                ['福建','福建省'],
                ['甘肃','甘肃省'],
                ['广东','广东省'],
                ['广西','广西壮族'],
                ['贵州','贵州省'],
                ['海南','海南省'],
                ['河北','河北省'],
                ['河南','河南省'],
                ['黑龙江','黑龙江省'],
                ['湖北','湖北省'],
		        ['湖南','湖南省'],
	        	['吉林','吉林省'],
	        	['江苏','江苏省'],
	          	['江西','江西省'],
	        	['辽宁','辽宁省'],
	        	['内蒙古','内蒙古'],
	        	['宁夏','宁夏回族'],
	        	['青海','青海省'],
	        	['山东','山东省'],
	        	['陕西','陕西省'],
	        	['山西','山西省'],
	        	['上海','上海市'],
	        	['四川','四川省'],
	        	['天津','天津市'],
	        	['西藏','西藏'],
	        	['新疆','新疆维吾尔'],
	        	['云南','云南省'],
	        	['浙江','浙江省'],

		]
	user_name = forms.CharField(label = '您的姓名',max_length = 50)
	user_city = forms.ChoiceField(label = '居住城市',choices = CITY )
	user_email = forms.EmailField(label = '电子邮件')
	user_message = forms.CharField(label = '您的意见',widget = forms.Textarea)
class PostForm(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = models.Post
		fields = ['mood','nickname','message']
	def __init__(self,*args,**kwargs):
		super(PostForm,self).__init__(*args,**kwargs)
		self.fields['mood'].label = '现在的心情'
		self.fields['nickname'].label = '用户名'
		self.fields['message'].label = '心情留言'
		self.fields['captcha'].label = '确定您不是机器人'
class LoginForm(forms.Form):
    username = forms.CharField(label = '姓名',max_length = 10)
    password = forms.CharField(label = '密码',widget = forms.PasswordInput())