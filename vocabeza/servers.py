
#google stuff
from google.appengine.ext import db
import webapp2

#libs
import json
import logging

#vocabeza 
import api_allwords
import api_quiz
import api_word
import model_word
import pages


     
class WelcomeResource(webapp2.RequestHandler):
    def get(self,location):
      self.redirect("/html/welcome.html")    
    
    def main():
      run_wsgi_app(application)

    if __name__ == '__main__':
      main()
   
	
	

app = webapp2.WSGIApplication([
    ('/allwords(.*)', api_allwords.AllwordsResource),
    ('/word(.*)', api_word.WordResource),
    ('/quiz(.*)',api_quiz.QuizResource),
    ('/page(.*)', pages.PageController),
    ('/(.*)', WelcomeResource)
])


