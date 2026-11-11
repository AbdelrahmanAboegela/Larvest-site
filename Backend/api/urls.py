from django.urls import path
from . import views

urlpatterns = [
    path('generate-tiles/', views.TileGenerationView.as_view(), name='generate-tiles'),
    path('tile-map/', views.TileMapView.as_view(), name='tile-map'),
    path('time_series/', views.TimeSeriesView.as_view(), name='time_series'),
    path('windy-access/', views.WindyAccessView.as_view(), name='windy-access'),
    # Farm areas CRUD
    path('farm-areas/', views.FarmAreaView.as_view(), name='farm-areas-list'),
    path('farm-areas/<int:pk>/', views.FarmAreaDetailView.as_view(), name='farm-areas-detail'),
]