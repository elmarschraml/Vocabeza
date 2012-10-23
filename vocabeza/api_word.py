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
          all_word_propnames = model_word.WordModel(version=1,de="bla",es="bla").to_dict().keys()
          logging.info("word props: " + str(all_word_propnames))
          q = model_word.WordModel.all()
          filter_count = 0
          for curprop in all_word_propnames:
            if curprop in all_param_names:
              filter_count += 1
              filter_crit = curprop + " ="
              filter_val = self.request.params.get(curprop)
              logging.info("crit:" + filter_crit + " , value: " + filter_val)
              q.filter(filter_crit,filter_val)
          if filter_count == 0:
            retval = dict(code="badinput", message="None of the request parameters match a word property to search for. Supported search parameters are: " + str(all_word_propnames))
          else:
            wordlist = q.fetch(1000)
            logging.info("search results: " + str(wordlist))
            retval = [w.to_dict() for w in wordlist]

      
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
      self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
      word_id = location.lstrip('/')
      if len(word_id) == 0:
        logging.info("DELETE /word: no id given, nothing to be done")
        retval = dict(code="badinput", message="Please add an id to the url to which word to delete")
      else:
        found_word = model_word.WordModel.get_by_id(int(word_id))
        if (found_word):
          db.delete(found_word)
          retval = dict(code="ok", message="word with id " + word_id + " was deleted")
        else:
          retval = dict(code="notfound", message="no word found with id " + word_id + ", so could not delete anything")
      jsontext = json.dumps(retval)
      self.response.out.write(jsontext)
    
    def post(self,location):
      self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
      logging.info("doing word post")
      word_id = location.lstrip('/')
      if len(word_id) == 0:
        logging.error("no word id given, dont know which word to update")
        retval = dict(code="badinput", message="word id missing, cant update anything - Please add the id of the word to update to the url, like POST /word/17")
      elif not(word_id.isdigit()): #id is not numeric
        retval = dict(code="badinput", message="word id has to be numeric")
      else:
        logging.info("looking for word with id: " + word_id)
        found_word = model_word.WordModel.get_by_id(int(word_id))
        if (found_word):
          try:
            rawrequest = self.request.body
            payload = json.loads(rawrequest)
            logging.info("from_request: " + str(payload))
            #BETA avoid hardcoding word attributes - is there a way to get all declared attributes from a class?
            word_attributes = ["version","de","es","comment"] #difficulty and lastquiy can not be set by client
            for cur_attribute in word_attributes:
              if cur_attribute in payload:
                setattr(found_word,cur_attribute, payload[cur_attribute])
                logging.debug("word was changed to: " + json.dumps(db.to_dict(found_word)) )
                #found_word[cur_attribute] = payload[cur_attribute]
            found_word.put()
            retval = dict(code="ok", message="word with id " + word_id + " was updated")
          except (ValueError, TypeError) as payloaderror:
            logging.info(payloaderror)
            retval = dict(code="badinput", message="could not read input as json representation of a word, input was: " + rawrequest)
        else:
          retval = dict(code="notfound", message="No word found for id " + word_id)
      
      jsontext = json.dumps(retval)
      self.response.out.write(jsontext)

  
  #TODO implement log and error message when another (unsupported) operation is called
 
