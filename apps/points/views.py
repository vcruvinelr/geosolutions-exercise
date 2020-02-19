import json
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import TemplateView
from django.contrib.gis.measure import D
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.core.cache import cache
from django.core import serializers

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

def search(request):
    try:

        query_x = request.GET.get('query_x')
        query_y = request.GET.get('query_y')
        points_returned = request.GET.get('points_returned')
        distance_condition = request.GET.get('distance_condition')

        if distance_condition == 'Nearest':

            object_list = Points.objects.filter(
                geom_point__distance_lte=('POINT({0} {1})'.format(query_x, query_y), D(km=100000000000))
                ).order_by('geom_point')[:int(points_returned)]

        else:
            object_list = Points.objects.filter(
                geom_point__distance_lte=('POINT({0} {1})'.format(query_x, query_y), D(km=100000000000))
                ).order_by('-geom_point')[:int(points_returned)]

        if not 'query_x' in request.session or not request.session['query_x']:
            request.session['query_x'] = [query_x]
        else:
            saved_list = request.session['query_x']
            saved_list.append(query_x)
            request.session['query_x'] = saved_list

        if not 'query_y' in request.session or not request.session['query_y']:
            request.session['query_y'] = [query_y]
        else:
            saved_list = request.session['query_y']
            saved_list.append(query_y)
            request.session['query_y'] = saved_list

        as_json = serializers.serialize('json', object_list)

        return JsonResponse(as_json, safe=False)

    except KeyError:
        return render_to_response('home.html', {'points_list': points_list})
