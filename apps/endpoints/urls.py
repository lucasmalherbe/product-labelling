from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.endpoints.views import home, labellingbyhand_label, labellingbyhand_prediction
from apps.endpoints.views import labelling_tableChoice, labelling_groupChoice, labelling_prediction
from apps.endpoints.views import labelling_summary, labelling_final

urlpatterns = [
    path('home', home, name='home'),
    path('labellingbyhand/label/', labellingbyhand_label, name='labellingbyhand_label'),
    path('labellingbyhand/prediction/', labellingbyhand_prediction, name='labellingbyhand_prediction'),
    path('labelling/tablechoice', labelling_tableChoice, name='labelling_tableChoice'),
    path('labelling/groupchoice', labelling_groupChoice, name='labelling_groupChoice'),
    path('labelling/prediction', labelling_prediction, name='labelling_prediction'),
    path('labelling/summary', labelling_summary, name='labelling_summary'),
    path('labelling/final', labelling_final, name='labelling_final')
]
