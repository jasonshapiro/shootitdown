<<<<<<< HEAD
from django.http import HttpResponse

from django.shortcuts import render_to_response
import datetime
from shootitdown.shootitdown_app.models import *

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('base.html')

def submit(request):
    return render_to_response('submit.html')

def latest(request):
    idea_title_form = request.POST['idea_title']
    idea_text_form = request.POST['idea_text']
    idea_created_form = datetime.datetime.now()
    idea_last_activity_form = datetime.datetime.now()
    idea = Idea(idea_title=idea_title_form, idea_text=idea_text_form, idea_created=idea_created_form, 
                idea_last_activity=idea_last_activity_form)
    idea.save()
    return render_to_response('base.html')
=======
def index(request):
    
    ideas = Models.Ideas.sort(recency)[0:4]
    allcomments = []
    for eachidea in ideas:
        comments = Models.comments(eachidea.id)
        allcomments = [allcomments,comments]

    return rendertoresponse('/index.html',RequestContext='{ideas:ideas, allcomments:allcomments}')
>>>>>>> 3eac54981b4d7145eaef8d2790a900b83e70f1dd
