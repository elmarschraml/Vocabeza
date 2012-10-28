from google.appengine.ext import db
from model_word import WordModel 

class QuizModel(db.Model):
    version = db.IntegerProperty(required=True)
    word = db.ReferenceProperty(WordModel)
    answer = db.StringProperty(required=True)
    date = db.DateTimeProperty(required=False)

    
    def to_dict(self):
      return dict([(p, unicode(getattr(self, p))) for p in self.properties()])

    def __str__(self):
      return str(self.to_dict())