'''
Created on 2012/07/14
##Pushリクエストのテスト
@author: dmitryshostakovich
'''
from google.appengine.ext.db import import djangoforms

class bbsform(djangoforms.ModelForm):
    '''
    bbsのform
    '''
    model = bbsdata

class bbsdata(db.Model):
    name = db.StringProperty(required=True,multiline=False,verbose_name='名前')
    mail = db.StringProperty(multiline=False,verbose_name='メール')
    title = db.StringProperty(multiline=False,verbose_name='タイトル')
    memo = db.StringProperty(multiline=True,required=True,verbose_name='投稿欄')


    def __init__(selfparams):
        '''
        Constructor
        '''
        