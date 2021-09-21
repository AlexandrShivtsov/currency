from currency.views import (ContactusCreateView, CurrencyRateListView, CurrencyResponseLog,
                            SourceCreateView, SourceDeleteView, SourceDetailsView,
                            SourceListView, SourceUpdateView)

import debug_toolbar

from django.urls import include, path


app_name = 'currency'

urlpatterns = [

    path('source-list/', SourceListView.as_view(), name='source-list'),
    path('rate-list/', CurrencyRateListView.as_view(), name='rate-list'),
    path('source-list/create-source/', SourceCreateView.as_view(), name='create-source'),
    path('source-list/details-source/<int:pk>/', SourceDetailsView.as_view(), name='details-source'),
    path('source-list/update-source/<int:pk>/', SourceUpdateView.as_view(), name='update-source'),
    path('source-list/delete-source/<int:pk>/', SourceDeleteView.as_view(), name='delete-source'),
    path('contactus/create/', ContactusCreateView.as_view(), name='contactus-create'),
    path('response-log/', CurrencyResponseLog.as_view(), name='response-log'),

    path('__debug__/', include(debug_toolbar.urls)),

]
