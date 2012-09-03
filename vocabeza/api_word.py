from google.appengine.ext import db
import json
import webapp2
import logging
import model_word


class  WordResource(webapp2.RequestHandler):


    def get(self,location):
      self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
      word_id = location.lstrip('/')
      if len(word_id) == 0:
        logging.info("GET /word: no id given, so going by request parameters for attribute search")
        all_param_names = self.request.arguments()
        if all_param_names == None or len(all_param_names) == 0:
          retval = dict(code="badinput", message="Please either add an id to the url to retrieve a word, e.g. GET /word/17, or supply parameters to search, e.g. GET /word?de=beispiel")
        else:
          #add matching url params to query filter
          retval = dict(message="cant handle param search yet")


      elif not(word_id.isdigit()): #id is not numeric
        retval = dict(code="badinput", message="word id has to be numeric")
      else:
        logging.info("looking for word with id: " + word_id)
        found_word = model_word.WordModel.get_by_id(int(word_id))
        if (found_word):
          retval = db.to_dict(found_word)
        else:
          retval = dict(code="notfound", message="No word found for id " + word_id)
      jsontext = json.dumps(retval)
      self.response.out.write(jsontext)     
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
 
