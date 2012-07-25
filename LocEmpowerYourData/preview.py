#!-*- coding:utf-8 -*-"
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import os
import bbsdata

class BBSWrite(webapp.RequestHandler):
    def post(self):
##
## 書き込み処理
        bd = bbsdata.bbsdata(
            name = self.request.get('name'),
            mail = self.request.get('mail'),
            title = self.request.get('title'),
            memo = self.request.get('memo'))
        bd.put()
        self.redirect("/")

application = webapp.WSGIApplication([('/write', BBSWrite)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
