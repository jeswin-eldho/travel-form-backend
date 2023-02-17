from django.urls import path

from api.forms.views import Form

app_name = "api.forms"

urlpatterns = [
    path(
        "",
        Form.as_view(),
        name="form_data",
    ),
]
