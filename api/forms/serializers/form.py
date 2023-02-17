from rest_framework import serializers

from api.forms.models import FormData


class FormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormData
        fields = "__all__"
