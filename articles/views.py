from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy # new
from .models import Article


# Create your views here.
class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView): # new
    model = Article
    template_name = 'article_detail.html'

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleUpdateView(LoginRequiredMixin, UpdateView): # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView): # new
    model = Article
    fields = ('title', 'body')
    template_name = 'article_new.html'

    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)

