from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
    
    
    def get(self):
        self.layout['content'] = self.htmldir + 'write.html'
        params = {'layout':self.layout,'form':bbsform()}
        fpath = os.pathjoin(os.path.dirname(_file_),'layouts',self.layout_file)
        html = template.render(fpath.params)
        self.response.out.write(html) 


application = webapp.WSGIApplication([('/', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
