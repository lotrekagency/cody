from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route


from core.models import Project, Action

from .tasks import task_execute_action


class ProjectsViewSet(viewsets.ViewSet):

    def get_object(self, pk):
        try:
            return Project.objects.get(slug=pk)
        except Project.DoesNotExist:
            raise Http404

    def _check_header(self, request, project):
        if 'Auth ' + project.token != request.META.get('HTTP_PROJECTTOKEN', None):
            raise Http404

    @detail_route(methods=["post"])
    def execute(self, request, pk):
        project = self.get_object(pk)
        action = request.data.get('action', None)
        self._check_header(request, project)
        if action:
            actions = [Action.objects.get(project=project, endpoint=action)]
            response = {'result' : f'Executing action {action} on project {pk}'}
        else:
            actions = Action.objects.filter(project=project)
            response = {'result' : f'Executing all actions on project {pk}'}
        task_execute_action(project, actions)
        return Response(response)
