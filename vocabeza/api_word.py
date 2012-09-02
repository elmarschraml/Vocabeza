from google.appengine.ext import db
import json
import webapp2
import logging
import model_word


class  WordResource(webapp2.RequestHandler):


    def get(self,location):
      logging.info("word get is not yet implemented")
      word_id = location.lstrip('/')
      logging.info("looking for word with id: " + word_id)
      q = db.Query(model_word.WordModel)
      q.filter("wordid =",word_id)
      found_word = q.get()
      word_dict = db.to_dict(found_word)
      jsontext = json.dumps(word_dict)
      self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
      self.response.out.write(jsontext)     
      #TODO error handling
      #TODO if no id present, go by url param for de or es

      
    def delete(self,location):
      logging.info("word get is not yet implemented")
      #TODO implement
      #get id from url
      #delete word
      #send confirmation json

    def post(self,location):
	  logging.info("word post is not yet implemented")
	  #TODO implement
	  #get id from url
	  #update word
	  #save
	  #send confirmation json
	
  #TODO implement log and error message when another (unsupported) operation is called	
 
