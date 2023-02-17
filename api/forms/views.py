from rest_framework import status
from rest_framework.views import APIView

from api.common.responses import Response
from api.forms.models import FormData
from api.forms.serializers.form import FormDataSerializer
from api.forms.utils import FormUtils


class Form(APIView):
    """Endpoint to get all the form submissions"""

    @staticmethod
    def get(request):
        try:
            form_data = FormData.objects.all()
            form_data = FormDataSerializer(form_data, many=True).data
        except Exception:
            return Response.generate(
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                "Something went wrong",
            )

        return Response.generate(
            status.HTTP_200_OK,
            "Successfully fetched form data",
            {"data": form_data},
        )

    @staticmethod
    def post(request):
        data = request.data
        try:
            data = FormUtils.validate_form_data(data)
        except Exception:
            return Response.generate(
                status.HTTP_400_BAD_REQUEST,
                "Something went wrong",
                {"reasons": ["Missing required parameters"]},
            )

        FormData.objects.create(**data)

        return Response.generate(
            status.HTTP_200_OK,
            "Successfully created form data",
        )
