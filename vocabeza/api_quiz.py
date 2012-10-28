from google.appengine.ext import db
from datetime import datetime
from random import choice
import json
import webapp2
import logging
import model_quiz
import model_word



class QuizResource(webapp2.RequestHandler):

  quiz_wrong_input_message = "To PUT a new quiz, you need to supply a json body, e.g. {'version': 1, 'date': '2012-10-01 10:00:00', 'answer': 'bla', 'word': 17}"     

  def get(self,location):
    nr_of_quizzes = 1
    if "count" in self.request.params:
      try:
        nr_of_quizzes = int(self.request.params["count"])
      except ValueError:
        nr_of_quizzes = 1
    q = model_word.WordModel.all()
    wordlist = q.fetch(1000)
    quizlist = list()
    for _ in range(nr_of_quizzes):
      chosen_word = choice(wordlist)
      quizlist.append(chosen_word)
    jsontext = json.dumps([w.to_dict() for w in quizlist])
    self.response.out.write(jsontext)


  def put(self,location):
    logging.info("read request" + self.request.body)
    requestbody = self.request.body
    if len(requestbody) == 0:
      logging.info("wordlist PUT: empty request body, cannot continue")
      retval = dict(code="badinput", message=self.quiz_wrong_input_message)
    else:   
        try:
          from_request = json.loads(self.request.body)
          logging.info("from_request: " + str(from_request))
          new_quiz = model_quiz.QuizModel(version=1, answer='bla')
          if "version" in from_request:
            new_quiz.version = from_request["version"]
          new_quiz.answer = from_request["answer"]
          if "date" in from_request:
            new_date = datetime.strptime(from_request["date"], "%Y-%m-%d %H:%M:%S")
            new_quiz.date = new_date
          logging.info("new_quiz with data: " + str(new_quiz))
          new_quiz.put()
          logging.info("was put in db")
          retval = dict(code="ok", mesage="quiz for answer " + new_quiz.answer + " was saved") #TODO include whole json quiz object - needs to deal with datetime json serialization
        except (ValueError, TypeError) as error:
          logging.info(error)
          retval = dict(code="badinput", message=self.quiz_wrong_input_message)
    jsontext = json.dumps(retval)
    self.response.out.write(jsontext)
    

  #TODO implement log and error message when another (unsupported) operation is called
  def main():
      run_wsgi_app(application)

  if __name__ == '__main__':
      main()