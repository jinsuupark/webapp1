from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.mixins import AccessMixin
from django.views.defaults import permission_denied

from blog.models import Post

from django.views.generic import TodayArchiveView
# TemplateView

class Homeview(TodayArchiveView):
    template_name = 'home.html'
    model = Post
    date_field = 'modify_dt'
    # month_format = '%m'
    paginate_by = 2
    allow_empty = True




# User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = 'Owner only can update/delete the object'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()  # 모델 인스턴스 얻기
        if self.request.user != self.object.owner:
            self.handle_no_permission()
        return super().get(request, *args, **kwargs)
