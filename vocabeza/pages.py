from google.appengine.ext import db
import json
import webapp2
import logging
import model_word
from webapp2_extras import jinja2


class PageController(webapp2.RequestHandler):

  @webapp2.cached_property
  def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

  def render_template(self, filename, **template_args):
    self.response.write(self.jinja2.render_template(filename, **template_args))

  def get(self,location):
	#TODO: check for url ending in /allwords
	#TODO: redirect to start page if unknown page requested
    q = model_word.WordModel.all()
    q.order("de")
    wordlist = q.fetch(100)
    self.render_template('wordlist.html', url_linktext="supi supi linki", words=wordlist)

   #only supports get to return rendered jinja templates
   #updates/changes are done by ajax request to the api

  def main():
    run_wsgi_app(application)

  if __name__ == '__main__':
    main()   