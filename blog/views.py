from django.shortcuts import render , HttpResponse
from blog.models import Post,Contact
from random import shuffle


# Create your views here.
def home(request):
    allPosts = Post.objects.all()
    my_list = list(allPosts)
    shuffle(my_list)
    
    
    context = {'allPosts': my_list}
    return render(request,'home.html',context)
def bloghome(request):
    allPosts1 = Post.objects.all().order_by('-timeStamp')
    
    context = {'allPosts1':allPosts1}
    
    return render(request,'Bloghome.html',context)
def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    
   
    
    
    context = {'post': post}
   
    return render(request,'blogPost.html',context)
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        phone = request.POST['phone']
        contact = Contact(name=name , email=email, phone=phone,content=content)
        contact.save()

    return render(request,'contact.html')
def search(request):
    query = request.GET['query']
    if len(query)>140:
        allPosts = Post.objects.none()
    else:
        allPoststitle = Post.objects.filter(title__icontains=query)
        allPostscontent = Post.objects.filter(content__icontains=query)
        allPosts = allPoststitle.union(allPostscontent)
        
    params = {'allPosts':allPosts, 'query': query}
    return render(request,'search.html',params)
    #return HttpResponse('this is search')

