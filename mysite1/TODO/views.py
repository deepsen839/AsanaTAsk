from multiprocessing import context
from pickle import FALSE, TRUE
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView,RedirectView


from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import asanaModel
from .forms import asanaForm
from django.core import serializers
import json
from django.template.loader import render_to_string
from django.conf import settings
from asana import *
# Create your views here.
class apiView(TemplateView):
    template_name = 'TODO/addtask.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = asanaModel.objects.all()
        context['form'] = asanaForm()
        context['tasks'] = tasks
        context['template_name']="TODO/addtask.html"
        return context
    def post(self, request, *args, **kwargs):
        form = asanaForm(data=request.POST)
        template_name = "TODO/addtask.html"
        if form.is_valid():
            client = Client.access_token(settings.PERSONAL_ACCESS_TOKEN)
            #jsondata = json.dumps(creatTask); 
            #return HttpResponse(json.dumps(jsondata))
            creatTask = {'name': request.POST.get('taskname'),'notes': request.POST.get('notes'),"projects":[settings.PROJECT_ID]}                
            result = client.tasks.create_task(creatTask,opt_pretty=True)

          #  resultDatafterParsingToJson = json.load(json.dumps(result))

            form.instance.task_id=int(result['gid'])
            form.save()
            return HttpResponseRedirect('/')
        else:
            tasks = asanaModel.objects.all()
            return render(request, template_name, {'form': form,'tasks':tasks})

class detailsView(TemplateView):
    template_name = "TODO/details.html"
    def get(self, request, *args, **kwargs):
        template_name = "TODO/details.html"
        data = asanaModel.objects.get(pk=kwargs['id'])
        taskData = {'taskData':data}
        html = render_to_string(template_name,taskData)
        htmlData = {'html':html}
     #   data = serializers.serialize("json",[taskData])
        return HttpResponse(html,content_type='application/json')

        #return render(request, template_name, {'form': form,'tasks':tasks})
    """ def post(self, request, *args, **kwargs):
        taskData = asanaModel.objects.get(pk=kwargs['id'])
        form = self.form_class(request.POST,instance=taskData)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-view'))
        else:
            return render(request, self.template_name, {'form': form})"""