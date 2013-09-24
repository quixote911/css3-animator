# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import socket
from django.utils import simplejson
import json

def test(request):
    return render(request,'jqueryuitest.html')

def ajax(request):
    print "AJAX METHOD CALLED"
    return render(request,'learnajax.html')

def ajax_process(request):
    print "AJAX_PROCESS METHOD CALLED"
    if request.POST:
        x = request.POST
        print x
        y="RETURN IS SUCCESSFULL!!!"
        response_dict = {}
        response_dict.update({'server_response': y })
        return HttpResponse(json.dumps(response_dict), mimetype='application/javascript')
    else:
        return render(request,'learnajax.html')