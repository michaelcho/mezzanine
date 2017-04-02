from mezzanine.pages.models import Page
from mezzanine.pages.page_processors import processor_for
from django.contrib.auth.models import User

# The members of Page will be inherited by the Author model, such
# as title, slug, etc. For authors we can use the title field to
# store the author's name. For our model definition, we just add
# any extra fields that aren't part of the Page model, in this
# case, date of birth.


class Community(Page):
    pass


@processor_for(Community)
def community(request, page):
    users = User.objects.all().order_by('-pk')[:5]
    return {"users": users}