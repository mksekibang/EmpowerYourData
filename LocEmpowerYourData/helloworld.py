#!-*- coding:utf-8 -*-"
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template
import bbsdata

class MainPage(webapp.RequestHandler):
    
    def get(self):
        params = {'form':bbsdata.bbsform()}
        fpath = os.path.join(os.path.dirname(__file__),'htmldir','write.html')
        html = template.render(fpath,params)
        self.response.out.write(html)

class PreviewPage(webapp.RequestHandler):
    def post(self):
        # フォームから送信された内容を取得する
        template_values ={
            'name': self.request.get('name'),
            'mail': self.request.get('mail'),
            'title': self.request.get('title'),
            'memo': self.request.get('memo')
        }

        fpath = os.path.join(os.path.dirname(__file__),'htmldir', 'preview.html')
        self.response.out.write(template.render(fpath, template_values))

def main():
    application = webapp.WSGIApplication([('/', MainPage),('/preview', PreviewPage)], debug=True)
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
