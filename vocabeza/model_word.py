from google.appengine.ext import db

class WordModel(db.Model):
    #keine id, stattdessen datastore key
    version = db.IntegerProperty(required=True)
    de = db.StringProperty(required=True)
    es = db.StringProperty(required=True)
    comment = db.StringProperty
    quiz_nr = db.IntegerProperty
    quiz_ok = db.IntegerProperty
    quiz_last = db.DateProperty

    def to_dict(self):
	       return dict([(p, unicode(getattr(self, p))) for p in self.properties()])