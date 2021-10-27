from django.views import generic
from .models import Project

class ProjectListView(generic.ListView):
    model = Project

    pageTitle = 'Projects'

    context_object_name = 'project'

    ordering = ['-date_posted']

    paginate_by = 3

    template_name = 'project/home.html'


class ProjectDetailView(generic.DetailView):
    model = Project

    pageTitle = Project.name

    context_object_name = 'project'

    template_name = 'project/detail.html'
