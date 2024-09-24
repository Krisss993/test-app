from django.shortcuts import render
import os
from django.http import HttpResponse

def serve_chart1(request):
    chart_file_path = os.path.join('static', 'notebooks', 'charts', 'KMclustDB.html')

    try:
        with open(chart_file_path, 'r', encoding='utf-8') as f:
            chart_html = f.read()
        return HttpResponse(chart_html)
    except FileNotFoundError:
        return HttpResponse("Chart not found", status=404)
    
    
def serve_chart2(request):
    chart_file_path = os.path.join('static', 'notebooks', 'charts', 'KMclustDB2.html')

    try:
        with open(chart_file_path, 'r', encoding='utf-8') as f:
            chart_html = f.read()
        return HttpResponse(chart_html)
    except FileNotFoundError:
        return HttpResponse("Chart not found", status=404)
    
def serve_chart3(request):
    chart_file_path = os.path.join('static', 'notebooks', 'charts', 'KMclustDB3.html')

    try:
        with open(chart_file_path, 'r', encoding='utf-8') as f:
            chart_html = f.read()
        return HttpResponse(chart_html)
    except FileNotFoundError:
        return HttpResponse("Chart not found", status=404)
    
def serve_chart4(request):
    chart_file_path = os.path.join('static', 'notebooks', 'charts', 'KMclustDB4.html')

    try:
        with open(chart_file_path, 'r', encoding='utf-8') as f:
            chart_html = f.read()
        return HttpResponse(chart_html)
    except FileNotFoundError:
        return HttpResponse("Chart not found", status=404)
    



def serve_chart_tsne1(request):
    chart_file_path = os.path.join('static', 'notebooks', 'charts', 'pcabar.html')

    try:
        with open(chart_file_path, 'r', encoding='utf-8') as f:
            chart_html = f.read()
        return HttpResponse(chart_html)
    except FileNotFoundError:
        return HttpResponse("Chart not found", status=404)
    
def serve_chart_tsne2(request):
    chart_file_path = os.path.join('static', 'notebooks', 'charts', 'pca3d.html')

    try:
        with open(chart_file_path, 'r', encoding='utf-8') as f:
            chart_html = f.read()
        return HttpResponse(chart_html)
    except FileNotFoundError:
        return HttpResponse("Chart not found", status=404)
    
def serve_chart_tsne3(request):
    chart_file_path = os.path.join('static', 'notebooks', 'charts', 'tsne2comp.html')

    try:
        with open(chart_file_path, 'r', encoding='utf-8') as f:
            chart_html = f.read()
        return HttpResponse(chart_html)
    except FileNotFoundError:
        return HttpResponse("Chart not found", status=404)

def serve_chart_tsne4(request):
    chart_file_path = os.path.join('static', 'notebooks', 'charts', 'tsnepca.html')

    try:
        with open(chart_file_path, 'r', encoding='utf-8') as f:
            chart_html = f.read()
        return HttpResponse(chart_html)
    except FileNotFoundError:
        return HttpResponse("Chart not found", status=404)
    
def serve_chart_tsne5(request):
    chart_file_path = os.path.join('static', 'notebooks', 'charts', 'tsneafterpca.html')

    try:
        with open(chart_file_path, 'r', encoding='utf-8') as f:
            chart_html = f.read()
        return HttpResponse(chart_html)
    except FileNotFoundError:
        return HttpResponse("Chart not found", status=404)
    
def serve_chart_tsne6(request):
    chart_file_path = os.path.join('static', 'notebooks', 'charts', 'pcatsnecomp.html')

    try:
        with open(chart_file_path, 'r', encoding='utf-8') as f:
            chart_html = f.read()
        return HttpResponse(chart_html)
    except FileNotFoundError:
        return HttpResponse("Chart not found", status=404)
    
def serve_chart_tsne7(request):
    chart_file_path = os.path.join('static', 'notebooks', 'charts', 'tsne3comp.html')

    try:
        with open(chart_file_path, 'r', encoding='utf-8') as f:
            chart_html = f.read()
        return HttpResponse(chart_html)
    except FileNotFoundError:
        return HttpResponse("Chart not found", status=404)
    
