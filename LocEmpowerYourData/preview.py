#!-*- coding:utf-8 -*-"
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import os
import bbsdata

class PreviewPage(webapp.RequestHandler):
    def post(self):
##
## 書き込み処理を書く
##

        fpath = os.path.join(os.path.dirname(__file__),'htmldir', 'preview.html')
        self.response.out.write(template.render(fpath, template_values))

application = webapp.WSGIApplication([('/preview', PreviewPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
