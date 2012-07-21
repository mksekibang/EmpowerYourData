from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
    
    
    def get(self):
        fpath = os.path.join(os.path.dirname(__file__),'htmldir','write.html')
        html = template.render(fpath,None)
        self.response.out.write(html)


application = webapp.WSGIApplication([('/', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
