'''
Created on 2012/07/14
##Push���N�G�X�g�̃e�X�g
@author: dmitryshostakovich
'''
from google.appengine.ext.db import import djangoforms

class bbsform(djangoforms.ModelForm):
    '''
    bbs��form
    '''
    model = bbsdata

class bbsdata(db.Model):
    name = db.StringProperty(required=True,multiline=False,verbose_name='���O')
    mail = db.StringProperty(multiline=False,verbose_name='���[��')
    title = db.StringProperty(multiline=False,verbose_name='�^�C�g��')
    memo = db.StringProperty(multiline=True,required=True,verbose_name='���e��')


    def __init__(selfparams):
        '''
        Constructor
        '''
        