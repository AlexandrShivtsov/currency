from currency.views import SourceCreateView, SourceListView
from currency.views import SourceDeleteView
from currency.views import SourceDetailsView
from currency.views import SourceLoginView
from currency.views import SourceUpdateView

import debug_toolbar

from django.urls import include
from django.urls import path

app_name = 'currency'

urlpatterns = [
    path('login/', SourceLoginView.as_view(), name='login'),
    path('source-list/', SourceListView.as_view(), name='source-list'),
    path('source-list/create-source/', SourceCreateView.as_view(), name='create-source'),
    path('source-list/details-source/<int:pk>/', SourceDetailsView.as_view(), name='details-source'),
    path('source-list/update-source/<int:pk>/', SourceUpdateView.as_view(), name='update-source'),
    path('source-list/delete-source/<int:pk>/', SourceDeleteView.as_view(), name='delete-source'),

    path('__debug__/', include(debug_toolbar.urls)),
]
