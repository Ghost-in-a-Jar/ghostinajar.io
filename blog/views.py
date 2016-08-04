from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from el_pagination.decorators import page_template
from blog.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.shortcuts import redirect

def home(request, template='home.html'):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    post_list = Post.objects.order_by('-updated')[:3]
    context_dict = {'post_list': post_list}
    # Render the response and send it back!
    return render_to_response(template, context_dict, context)

@page_template('post_index_page.html')
def posts(request, template='post_index.html', extra_context=None):
    post_list=Post.objects.order_by('-updated')
    context = {
        'post_list':post_list,
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(
        template, context, context_instance=RequestContext(request))

def post(request, slug, template='post.html'):
    post=get_object_or_404(Post, slug=slug)
    return render(request, template, {
        'post': post,
    })

def about(request, template='about.html'):
    context = RequestContext(request)
    return render_to_response(template, context)

def contact(request, template='contact.html'):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            get_template('contact_template.txt')
        context = Context({
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
        })
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            "ghostinajar.io" + '',
            ['tristan@ghostinajar.io'],
            headers={'Reply-To': contact_email}
        )
        email.send()
        return redirect('contact')

    return render(request, template, {
        'form': form_class,
    })