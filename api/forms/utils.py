from api.common.utils import validate_request


class FormUtils:
    @staticmethod
    def validate_form_data(data):
        (is_valid, errors) = validate_request(
            {
                "name": {"required": True, "verbose_name": "Name"},
                "email": {"required": True, "verbose_name": "Email"},
                "destination": {"required": True, "verbose_name": "Destination"},
                "number_of_travellers": {
                    "required": True,
                    "verbose_name": "Number of Travellers",
                },
                "budget_per_person": {
                    "required": True,
                    "verbose_name": "Budget per person",
                },
            },
            data,
        )
        if not is_valid:
            raise Exception(",".join(errors))
        return data
