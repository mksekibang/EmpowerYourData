#!-*- coding:utf-8 -*-"
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template
from google.appengine.ext import db

class bbsdata2(db.Model):
    no = db.StringProperty(multiline=False)
    name = db.StringProperty(multiline=False)
    mail = db.StringProperty(multiline=False)
    title = db.StringProperty(multiline=False)
    memo = db.StringProperty(multiline=True)

class PreviewPage(webapp.RequestHandler):
    def post(self):
        bd = bbsdata2(key_name = self.request.get('no'))
        bd.no = self.request.get('no')
        bd.name = self.request.get('name')
        bd.mail = self.request.get('mail')
        bd.title = self.request.get('title')
        bd.memo = self.request.get('memo')
        bd.put()

        bbsdatas = db.GqlQuery("SELECT * FROM bbsdata2 ")

        # フォームから送信された内容を取得する
        template_values ={
            'name': self.request.get('name'),
            'mail': self.request.get('mail'),
            'title': self.request.get('title'),
            'memo': self.request.get('memo'),
            'bbsdatas':bbsdatas
        }

        fpath = os.path.join(os.path.dirname(__file__),'htmldir', 'preview.html')
        self.response.out.write(template.render(fpath, template_values))

application = webapp.WSGIApplication([('/preview', PreviewPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
