from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from spot import views

urlpatterns = [
    path('sightings/', views.SightingList.as_view()),
    path('listings/', views.ListingList.as_view())
    # path('sightings/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
