from django.shortcuts import render,HttpResponse
from blog.models import Blog,Contact
import math
# Create your views here.
def home(request):
    return render(request,'index.html')






def blog(request):

    #PAGINATION 
    posts=3
    page=request.GET.get('page')
    if page is None:
        page=1
    else:
        page=int(page)
    
    blogs=Blog.objects.all()
    length=len(blogs)
    print(length)
    blogs=blogs[(page-1)*posts:page*posts]
    if page>1:
        prev=page-1
    else:
        prev=None
    if page<math.ceil(length/posts):
        nxt=page+1
    else:
        nxt=None
    
    
    context={'blogs':blogs,'prev':prev,'nxt':nxt}
    return render(request,'bloghome.html',context)



def blogpost(request,slug):

    blog=Blog.objects.filter(slug=slug).first()
    context={'blog':blog}
    return render(request,'blogpost.html',context)

def search(request):
    return render(request,'search.html')

def contact(request):
    if request.method=='POST':
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        feedback=request.POST["feedback"]
        ins=Contact(name=name,email=email,phone=phone,feedback=feedback)
        ins.save()
    return render(request,'contact.html')
