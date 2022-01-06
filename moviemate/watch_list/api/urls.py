
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from watch_list.api.views import (StreamPlaformDetailAV, StreamPlatformListAV, WatchListAV,WatchDetailsAV,
ReviewCreate,ReviewListAV,ReviewDetailsAV)
router = DefaultRouter()
urlpatterns = [
    path('list/',WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>/',WatchDetailsAV.as_view(),name='movie-details'),

    path('',include(router.urls)),

    # path('stream/',StreamPlatformListAV.as_view(),name='stream-list'),
    # path('stream/<int:pk>/',StreamPlaformDetailAV.as_view(),name='stream-details'),

    # path('review/',ReviewListAV.as_view(),name='review-list'),
    # path('review/<int:pk>',ReviewDetailsAV.as_view(),name='review-details'),

    path('<int:pk>/review-create/', ReviewCreate.as_view(),name='review-create'),
    path('<int:pk>/reviews/', ReviewListAV.as_view(),name='review-list'),
    path('review/<int:pk>/', ReviewDetailsAV.as_view(),name='review-details'),





]
 