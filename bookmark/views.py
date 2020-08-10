from django.shortcuts import render

from django.views.generic import ListView,DetailView
from bookmark.models import Bookmark

from django.views.generic import CreateView,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

class BookmarkLV(ListView):
    model = Bookmark
    context_object_name = 'bookmark_list'

class BookmarkDV(DetailView):
    model = Bookmark
    context_object_name = 'bookmark'
#파이썬은 다중상속가능
class BookmarkCV(LoginRequiredMixin,CreateView):
    model=Bookmark
    fields=['title','url'] #폼 모델에 사용할 필드 -> 폼 모델 자동 생성
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BookmarkChangeLV(LoginRequiredMixin,ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return BookmarkCV.objects.filter(owner=self.request.user)


class BookmarkUV(OwnerOnlyMixin,UpdateView):
    model = Bookmark
    fields=['title','url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self,form):
        form.instance.owner = self.request.user
        success_url=reverse_lazy('bookmark/index')

# def index(request):
#     object_list = Bookmark.objects.all()
#     print(object_list)
#     context = {'bookmark_list':object_list}
#     return render(request,'bookmark/bookmark_list.html',context)
#
#
# def detail(request,pk):
#     object= Bookmark.objects.get(pk=pk)  # .get(id=pk) 같음
#     context={'bookmark':object}
#     return render(request,'bookmark/bookmark_detail.html',context)