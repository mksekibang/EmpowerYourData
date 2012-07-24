#!-*- coding:utf-8 -*-"
from google.appengine.ext import db
from google.appengine.ext.db import djangoforms

class bbsdata(db.Model):
    no = db.StringProperty(required=True,multiline=False,verbose_name='番号')
    name = db.StringProperty(required=True,multiline=False,verbose_name='名前')
    mail = db.StringProperty(multiline=False,verbose_name='メールアドレス')
    title = db.StringProperty(multiline=False,verbose_name='タイトル')
    memo = db.StringProperty(multiline=True,required=True,verbose_name='内容')

class bbsform(djangoforms.ModelForm):
    class Meta:
        model = bbsdata