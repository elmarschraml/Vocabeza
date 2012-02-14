

from google.appengine.ext import db
import json
import webapp2
import logging
from webapp2_extras import jinja2


class WordModel(db.Model):
    #keine id, stattdessen datastore key
    version = db.IntegerProperty(required=True)
    de = db.StringProperty(required=True)
    es = db.StringProperty(required=True)
    comment = db.StringProperty
    quiz_nr = db.IntegerProperty
    quiz_ok = db.IntegerProperty
    quiz_last = db.DateProperty
   



        
        
class AllwordsResource(webapp2.RequestHandler):

  @webapp2.cached_property
  def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

  def render_template(self, filename, **template_args):
    self.response.write(self.jinja2.render_template(filename, **template_args))

  def get(self,location):
    q = WordModel.all()
    q.order("de")
    wordlist = q.fetch(100)
    self.render_template('wordlist.html', url_linktext="supi supi linki", words=wordlist)

  def put(self,location):
    logging.info("read request" + self.request.body)
    from_request = json.loads(self.request.body)
    logging.info("from_request: " + str(from_request))
    new_word = WordModel(id='1', version=1, de='bla', es='bla')
    logging.info("new_word raw: " + str(new_word))
    new_word.de = from_request["de"]
    new_word.es = from_request["es"]
    new_word.comment = from_request["comment"]
    logging.info("new_word with data: " + str(new_word))
    new_word.put()
    logging.info("was put in db")
    word_dict = db.to_dict(new_word)
    jsontext = json.dumps(word_dict)
    logging.info("was serialized")
    self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
    self.response.out.write(jsontext)
		

    
class  WordResource(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def get(self,location):
      logging.info("word get is not yet implemented")
      #TODO implement
      #get id from url
      #get word for id from db
      #render template
      
    def delete(self,location):
      logging.info("word get is not yet implemented")
      #TODO implement
      #get id from url
      #delete word
      #send confirmation json
      
class WelcomeResource(webapp2.RequestHandler):
    def get(self,location):
      self.redirect("/html/welcome.html")    
   
	
	

app = webapp2.WSGIApplication([
    ('/allwords(.*)', AllwordsResource),
    ('/word(.*)', WordResource),
    ('/(.*)', WelcomeResource)
])

