from google.appengine.ext import db
import json
import webapp2
import logging
import model_word



class QuizResource(webapp2.RequestHandler):

  def get(self,location):
      logging.info("word get is not yet implemented")
      #TODO implement


  def put(self,location):
      logging.info("word get is not yet implemented")
      #TODO implement

  #TODO implement log and error message when another (unsupported) operation is called
  def main():
      run_wsgi_app(application)

  if __name__ == '__main__':
      main()