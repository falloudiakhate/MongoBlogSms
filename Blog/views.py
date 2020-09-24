from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from Model.models import *
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# Create your views here.
@login_required(login_url='Login')
def Publication(request):
    posts = Post.objects.all().order_by('-id')
    cat = Post.objects.all().values('categorie').distinct()
    r_posts = Post.objects.all().order_by('-id')[:3]
    cat_search = request.GET.get('cat')
    
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    try : 
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
        
    query_ = request.GET.get("q")
    if query_:
        query = Post.objects.filter(title__icontains=query_)
        som_q = query.count()
        
        if som_q !=0:
                messages.success(request,'{0} articles trouvées'.format(som_q))
        if som_q == 0:
                messages.warning(request,'0 articles trouvées')
                
    if cat_search :
        posts_list = Post.objects.filter(categorie=cat_search)
        som = posts_list.count()
        if som !=0:
                    messages.success(request,'{0} articles trouvées'.format(som))
        if som == 0:
                messages.warning(request,'0 articles trouvées')
                
    return render(request, "Blog/blog.html", locals())

@login_required(login_url='Login')
def PublicationDetails(request, id):
    posts = Post.objects.all()
    cat = Post.objects.all().values('categorie').distinct()
    r_posts = Post.objects.all().order_by('-id')[:3]
    post = Post.objects.get(id=id)
    comments = Comments.objects.filter(post=post)
    
    paginator = Paginator(comments,5)
    page = request.GET.get('page')
    try : 
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    
    if request.method == 'POST' and request.user.is_authenticated:
        content = request.POST["content"]
        comment = Comments()
        comment.user = request.user
        comment.post = post
        comment.comment_content = content
        comment.save()
        messages.success(request,'Votre commentaire a été ajouté avec succès !')
        

        
    return render(request, "Blog/blogDetails.html", locals())

@login_required(login_url='Login')
def LikePost(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    
    is_liked = False
    if post.likes.filter(id=request.user.author.id).exists():
        post.likes.remove(request.user.author)
        is_liked = False
    else:
        post.likes.add(request.user.author)
        is_liked = True
        
    return redirect("PublicationDetails", post_id)