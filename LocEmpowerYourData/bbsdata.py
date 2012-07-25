#!-*- coding:utf-8 -*-"
from google.appengine.ext import db
from google.appengine.ext.db import djangoforms

class bbsdata(db.Model):
    name = db.StringProperty(required=True,multiline=False,verbose_name='名前')
    mail = db.StringProperty(multiline=False,verbose_name='メールアドレス')
    title = db.StringProperty(multiline=False,verbose_name='タイトル')
    memo = db.StringProperty(multiline=True,required=True,verbose_name='内容')

class bbsdata2(db.Model):
    name = db.StringProperty(multiline=False)
    mail = db.StringProperty(multiline=False)
    title = db.StringProperty(multiline=False)
    memo = db.StringProperty(multiline=True)

class bbsform(djangoforms.ModelForm):
    class Meta:
        model = bbsdata