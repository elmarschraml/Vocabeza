

from google.appengine.ext import db
import json
import webapp2
from webapp2_extras import jinja2


class WordModel(db.Model):
    id = db.StringProperty(required=True)
    version = db.IntegerProperty(required=True)
    de = db.StringProperty(required=True)
    es = db.StringProperty(required=True)
    comment = db.StringProperty
    quiz_nr = db.IntegerProperty
    quiz_ok = db.IntegerProperty
    quiz_last = db.DateProperty


class WordResource(webapp2.RequestHandler):

  @webapp2.cached_property
  def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

  def render_template(self, filename, **template_args):
    self.response.write(self.jinja2.render_template(filename, **template_args))


  def post(self, location):
    # Do something for location
    my_response = {'id':'abcd1234', 'version':1, 'de':'antrag', 'es':'pedido'}
    json = json.dumps(my_response)
    self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
    self.response.out.write(json)

  def get(self,location):
        self.render_template('wordlist.html', url_linktext="supi supi linki")

  def put(self,location):
        self.response.out.write('doin da put')

  def delete(self,location):
        self.response.out.write('doin da delete')
	
	

app = webapp2.WSGIApplication([
    ('/(.*)', WordResource),
])

