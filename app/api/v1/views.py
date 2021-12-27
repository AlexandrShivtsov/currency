from api.v1.filters import ContactCreateFilter, RateFilter
from api.v1.paginators import ContactCreatePaginations, RatePaginations
from api.v1.serializer import ContactUsSerializer, RateSerializer, SourceBankSerializer
from api.v1.throttles import AnonUserRateThrottle

from currency import model_choces as mch
from currency.models import ContactCreate, Rate, SourceBank

from django.core.mail import send_mail

from django_filters import rest_framework as filters

from rest_framework import filters as rest_framework_filters
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from settings import settings


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().select_related('source')
    serializer_class = RateSerializer
    pagination_class = RatePaginations
    filterset_class = RateFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    ordering_fields = ['id', 'created', 'sale', 'buy']
    throttle_classes = [AnonUserRateThrottle]


class RateChoicesView(generics.GenericAPIView):
    def get(self, request):
        return Response(
            {'rate_types': mch.RATE_TYPES},
        )


class SourceBankView(generics.ListAPIView):
    queryset = SourceBank.objects.all()
    serializer_class = SourceBankSerializer


@api_view(['GET'])
def ContactUsList(request):
    contact_us = ContactCreate.objects.all()
    serializer = ContactUsSerializer(contact_us, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def CreateContactUs(request):
    serializer = ContactUsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        subject = serializer.data['subject']
        message = serializer.data['message']
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [settings.SUPPORT_EMAIL],
            fail_silently=False,
        )

    return Response(serializer.data)


@api_view(['POST'])
def UpdateContactUs(request, pk):
    contact_us = ContactCreate.objects.get(id=pk)
    serializer = ContactUsSerializer(instance=contact_us, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def DeleteContactUs(request, pk):
    contact_us = ContactCreate.objects.get(id=pk)
    contact_us.delete()
    return Response('Successfully')


class ContactUsView(viewsets.ModelViewSet):
    queryset = ContactCreate.objects.all()
    serializer_class = ContactUsSerializer
    pagination_class = ContactCreatePaginations
    filterset_class = ContactCreateFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.SearchFilter,
        rest_framework_filters.OrderingFilter,
    )
    ordering_fields = ['id', 'created', 'subject']
    search_fields = ['email_to']
    throttle_classes = [AnonUserRateThrottle]
