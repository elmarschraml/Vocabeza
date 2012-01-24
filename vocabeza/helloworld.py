from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class WordHandler(webapp.RequestHandler):
  def get(self, location):
    # Do something for location
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Hello, webapp World!')

application = webapp.WSGIApplication([
    ('/(.*)', WordHandler),
])

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()