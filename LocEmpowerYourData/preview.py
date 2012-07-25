#!-*- coding:utf-8 -*-"
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import os
import bbsdata

class PreviewPage(webapp.RequestHandler):
    def post(self):
        bd = bbsdata.bbsdata2()
        bd.name = self.request.get('name')
        bd.mail = self.request.get('mail')
        bd.title = self.request.get('title')
        bd.memo = self.request.get('memo')
        bd.put()

        # フォームから送信された内容を取得する
        template_values ={
            'name': self.request.get('name'),
            'mail': self.request.get('mail'),
            'title': self.request.get('title'),
            'memo': self.request.get('memo')
        }

        fpath = os.path.join(os.path.dirname(__file__),'htmldir', 'preview.html')
        self.response.out.write(template.render(fpath, template_values))

application = webapp.WSGIApplication([('/preview', PreviewPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
