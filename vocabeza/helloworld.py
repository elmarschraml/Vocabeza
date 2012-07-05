from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import simplejson as jsonlib

class WordHandler(webapp.RequestHandler):
  def get(self, location):
    some_param = self.request.get("username")
    postdata = self.request.body
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Hello, webapp World!')
	
class HelloJson(webapp.RequestHandler):
  def get(self, location):
    # Do something for location
    my_response = {'id':'abcd1234', 'version':1, 'de':'antrag', 'es':'pedido'}
    json = jsonlib.dumps(my_response)
    self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
    self.response.out.write(json)
	
    def post(self,location):
        self.response.out.write('doin da post')

    def put(self,location):
        self.response.out.write('doin da post')
		
    def delete(self,location):
        self.response.out.write('doin da post')
	
	

application = webapp.WSGIApplication([
    ('/(.*)', HelloJson),
])

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()