from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request, post_title_url):
    def index(request):
        # Obtain the context from the HTTP request.
        context = RequestContext(request)

        # Query the database for a list of ALL categories currently stored.
        # Order the categories by no. likes in descending order.
        # Retrieve the top 5 only - or all if less than 5.
        # Place the list in our context_dict dictionary which will be passed to the template engine.
        post_list = Post.objects.order_by('updated')[:5]
        context_dict = {'posts': post_list}

        # Render the response and send it back!
        return render_to_response('index.html', context_dict, context)
def posts(request):
    return render(request, "post.html", {})
def about(request):
    return render(request, "about.html", {})
def contact(request):
    return render(request, "contact.html", {})