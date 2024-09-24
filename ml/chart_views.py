from django.shortcuts import render
import os
from django.http import HttpResponse

def serve_chart1(request):
    # Assuming the chart is located in 'static/notebooks/charts/'
    chart_file_path = os.path.join('static', 'notebooks', 'charts', 'KMclustDB.html')

    try:
        with open(chart_file_path, 'r', encoding='utf-8') as f:
            chart_html = f.read()
        return HttpResponse(chart_html)
    except FileNotFoundError:
        return HttpResponse("Chart not found", status=404)
    
    
def serve_chart2(request):
    # Assuming the chart is located in 'static/notebooks/charts/'
    chart_file_path = os.path.join('static', 'notebooks', 'charts', 'KMclustDB2.html')

    try:
        with open(chart_file_path, 'r', encoding='utf-8') as f:
            chart_html = f.read()
        return HttpResponse(chart_html)
    except FileNotFoundError:
        return HttpResponse("Chart not found", status=404)
    
def serve_chart3(request):
    # Assuming the chart is located in 'static/notebooks/charts/'
    chart_file_path = os.path.join('static', 'notebooks', 'charts', 'KMclustDB3.html')

    try:
        with open(chart_file_path, 'r', encoding='utf-8') as f:
            chart_html = f.read()
        return HttpResponse(chart_html)
    except FileNotFoundError:
        return HttpResponse("Chart not found", status=404)
    
def serve_chart4(request):
    # Assuming the chart is located in 'static/notebooks/charts/'
    chart_file_path = os.path.join('static', 'notebooks', 'charts', 'KMclustDB4.html')

    try:
        with open(chart_file_path, 'r', encoding='utf-8') as f:
            chart_html = f.read()
        return HttpResponse(chart_html)
    except FileNotFoundError:
        return HttpResponse("Chart not found", status=404)
    