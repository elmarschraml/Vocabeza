from google.appengine.ext import db
import json
import webapp2
import logging
import model_word



class AllwordsResource(webapp2.RequestHandler):

  def get(self,location):
    q = model_word.WordModel.all()
    q.order("de")
    wordlist = q.fetch(100)
    jsontext = json.dumps(wordlist)
    self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
    self.response.out.write(jsontext)

  def put(self,location):
    logging.info("read request" + self.request.body)
    from_request = json.loads(self.request.body)
    logging.info("from_request: " + str(from_request))
    new_word = model_word.WordModel(id='1', version=1, de='bla', es='bla')
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

  #TODO implement log and error message when another (unsupported) operation is called