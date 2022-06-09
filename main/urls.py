from django.urls import path

from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('full_list', views.show_full_list_view, name = 'full_list'),
    path("plot_1", views.Plots_View.plot_1, name = "plot_1"),
    path("plot_2", views.Plots_View.plot_2, name = "plot_2"),
    path("plot_3", views.Plots_View.plot_3, name = "plot_3"),
    path("plot_4", views.Plots_View.plot_4, name = "plot_4"),
]