import json
import allure
from allure_commons.types import AttachmentType
from pydantic.error_wrappers import ValidationError
from config.headers import Headers


class BaseService:

    def __init__(self):
        self.headers = Headers()

    def validate(self, code, model):
        if self.response.status_code == code:
            try:
                return model(**self.response.json())
            except ValidationError as e:
                raise AssertionError(e)

    @allure.step("Check status code")
    def check_status_code(self, code=200):
        assert self.response.status_code == code, \
            f"\n \
Expected status code: {code}\n \
Actual status code: {self.response.status_code}\n \
Response: {self.response.text}"
        try:
            allure.attach(
                body=json.dumps(self.response.json(), indent=4),
                name="Response",
                attachment_type=AttachmentType.JSON
            )
        except:
            pass
