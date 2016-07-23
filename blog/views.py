from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from el_pagination.decorators import page_template

def home(request, template='home.html'):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    post_list = Post.objects.order_by('updated')[:3]
    context_dict = {'post_list': post_list}
    # Render the response and send it back!
    return render_to_response(template, context_dict, context)

@page_template('post_index_page.html')
def posts(request, template='post_index.html', extra_context=None):
    post_list=Post.objects.all()
    context = {
        'post_list':post_list,
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(
        template, context, context_instance=RequestContext(request))

def post(request, slug, id, template='post.html'):
    post=get_object_or_404(pk=id)
    context = RequestContext(request)

def about(request, template='about.html'):
    context = RequestContext(request)
    return render_to_response(template, context)
def contact(request):
    pass