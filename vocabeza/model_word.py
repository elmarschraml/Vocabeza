from google.appengine.ext import db

class WordModel(db.Model):
    version = db.IntegerProperty(required=True)
    de = db.StringProperty(required=True)
    es = db.StringProperty(required=True)
    comment = db.StringProperty(required=False)
    difficulty = db.IntegerProperty    # lowest: 1, highest: 100
    lastquiz = db.DateProperty

    def to_dict(self):
	       return dict([(p, unicode(getattr(self, p))) for p in self.properties()])

    def __str__(self):
           return str(self.to_dict())           