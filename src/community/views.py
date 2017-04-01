
from django.contrib.auth.models import User
from django.views.generic import TemplateView


class CommunityView(TemplateView):
    template_name = 'community.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CommunityView, self).get_context_data(*args, **kwargs)
        context['users'] = User.objects.all()
        return context

community = CommunityView.as_view()
