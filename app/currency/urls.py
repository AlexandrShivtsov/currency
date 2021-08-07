from currency.views import (ContactusCreateView, SourceCreateView, SourceDeleteView,
                            SourceDetailsView, SourceListView, SourceLoginView,
                            SourceUpdateView,)

import debug_toolbar

from django.urls import include, path


app_name = 'currency'

urlpatterns = [
    path('login/', SourceLoginView.as_view(), name='login'),
    path('source-list/', SourceListView.as_view(), name='source-list'),
    path('source-list/create-source/', SourceCreateView.as_view(), name='create-source'),
    path('source-list/details-source/<int:pk>/', SourceDetailsView.as_view(), name='details-source'),
    path('source-list/update-source/<int:pk>/', SourceUpdateView.as_view(), name='update-source'),
    path('source-list/delete-source/<int:pk>/', SourceDeleteView.as_view(), name='delete-source'),
    path('contactus/create/', ContactusCreateView.as_view(), name='contactus-create'),

    path('__debug__/', include(debug_toolbar.urls)),
]
