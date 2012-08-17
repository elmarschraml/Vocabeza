from google.appengine.ext import db
import json
import webapp2
import logging
import model_word



class AllwordsResource(webapp2.RequestHandler):

  word_wrong_input_message = "To PUT a new word, you need to supply a json body, e.g. {'de':'Beispiel','es':'ejemplo'}"     

  def get(self,location):
    q = model_word.WordModel.all()
    q.order("de")
    wordlist = q.fetch(100)

    jsontext = json.dumps([w.to_dict() for w in wordlist])
    self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
    self.response.out.write(jsontext)

  def put(self,location):
    logging.info("read request" + self.request.body)
    requestbody = self.request.body
    if len(requestbody) == 0:
      logging.info("wordlist PUT: empty request body, cannot continue")
      self.response.status = 415
      self.response.status_message = self.word_wrong_input_message
    elif requestbody == "ping":
      new_word = model_word.WordModel(id='123', version=1, de='bla', es='bla')
      new_word.put()
      self.response.status = 200
    else:   
        try:
          from_request = json.loads(self.request.body)
          logging.info("from_request: " + str(from_request))
          new_word = model_word.WordModel(id='123', version=1, de='bla', es='bla')
          logging.info("new_word raw: " + str(new_word))
          new_word.de = from_request["de"]
          new_word.es = from_request["es"]
          if "comment" in from_request:
            new_word.comment = from_request["comment"]
          logging.info("new_word with data: " + str(new_word))
          new_word.put()
          logging.info("was put in db")
          word_dict = db.to_dict(new_word)
          jsontext = json.dumps(word_dict)
          logging.info("was serialized")
          self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
          self.response.out.write(jsontext)
        except (ValueError, TypeError) as error:
          logging.info(error)
          self.response.status = 415
          self.response.status_message = self.word_wrong_input_message
 

  #TODO implement log and error message when another (unsupported) operation is called
  def main():
    run_wsgi_app(application)

  if __name__ == '__main__':
      main()