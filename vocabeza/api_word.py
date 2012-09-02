from google.appengine.ext import db
import json
import webapp2
import logging
import model_word


class  WordResource(webapp2.RequestHandler):


    def get(self,location):
      logging.info("word get is not yet implemented")
      new_word = model_word.WordModel(id='123', version=1, de='mock', es='el mockito')
      word_dict = db.to_dict(new_word)
      jsontext = json.dumps(word_dict)
      self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
      self.response.out.write(jsontext)
      #TODO implement
      #get id from url
      #get word for id from db
      #return json
      
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
 
