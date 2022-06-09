from django.shortcuts import render
from django.http import HttpResponse
from . import plots
# Create your views here.

class Plots_View:
    plot = [
        plots.plot_1(),
        plots.plot_2(),
        plots.plot_3(),
        plots.plot_4()
    ]
    def plot_1(request):
        # Plot 1
        info = {'data' : Plots_View.plot[0], 'Title' : "Evolution of New Cases", "height" : "700", "width" : "1400"}
        return render(request, "main/_plot_1.html", info)
    def plot_2(request):
        # Plot 2
        info = {'data' : Plots_View.plot[1], 'Title' : "Cumulative Number of Cases", 'height' : "500", "width" : "1200"}
        return render(request, "main/_plot_1.html", info)
    def plot_3(request):
        info = {'data' : Plots_View.plot[2], 'Title' : "Cumulative Number of Cases and Deceased", 'height' : "500", "width" : "1200"}
        return render(request, "main/_plot_1.html", info)
    def plot_4(request):
        info = {'data' : Plots_View.plot[3], 'Title' : "Number of Cases", 'height' : "2500", "width" : "1600"}
        return render(request, "main/_plot_1.html", info)
    

def show_full_list_view(request):
    html_table = plots.data.to_html()
    html_code = """<!DOCTYPE HTML>
<html>
<head>
    <meta charset = "UTF-8">
    <meta name = "viewport" content = "width=device-width, initial-scale = 1.0">
    {% load static %}
    <link rel = "stylesheet" href = "{% static 'main.css' %}">
</head>
<body><h1>全表</h1><a href = "/main">Home</a>""" + html_table + """</body></html>"""
    with open("main/templates/main/full_list.html", 'w') as html_temp:
        html_temp.write(html_code)
    return render(request, 'main/full_list.html')

def home(request):
    data = dict(zip(['plot_1', 'plot_2', 'plot_3', 'plot_4'], 
                [Plots_View.plot[0], Plots_View.plot[1], Plots_View.plot[2], Plots_View.plot[3] ]
    ))
    return render(request, 'main/home.html', data)