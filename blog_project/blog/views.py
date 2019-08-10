from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import CreateView,DeleteView,UpdateView,TemplateView,ListView,DetailView
from .models import Post,Comment
from django.urls import reverse_lazy
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect

from .forms import PostForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse


# Create your views here.
class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    redirect_field_name = 'post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/user_login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


#################
#################
#################

@login_required
def post_publish(request,pk):
    post= get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment =get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',post_pk)

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('post_list'))

def user_login(request):
	if request.method =='POST':
		username = request.POST.get('username')
		password= request.POST.get('password')

		user = authenticate(username= username, password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('post_list'))
			else:
				return HttpResponse("Account not Active")
		else:
			print("Login is failed")
			return HttpResponse("Invalid login detail supplied")
	else:
		return render(request,'blog/login.html',{})


