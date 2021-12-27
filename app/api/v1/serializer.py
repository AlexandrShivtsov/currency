from currency.models import ContactCreate, Rate, SourceBank

from rest_framework import serializers


class SourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = SourceBank
        fields = (
            'id',
            'name',
        )


class RateSerializer(serializers.ModelSerializer):
    source_obj = SourceSerializer(source='source', read_only=True)

    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sale',
            'currency_type',
            'created',
            'source_obj',
            'source',
        )
        extra_kwargs = {
            'source': {'write_only': True},
        }


class SourceBankSerializer(serializers.ModelSerializer):

    class Meta:
        model = SourceBank
        fields = (
            'name',
        )


class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactCreate
        fields = ('id',
                  'email_to',
                  'subject',
                  'message',
                  'created',)
