import re

from eve import Eve
from eve.io.mongo import Validator

class MyValidator(Validator):
    def _validate_isodd(self,isodd, field, value):
        if isodd and not bool(value & 1):
            self._error(field, 'Value must be an odd number')

    def _validate_type_email(self,field, value):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            self._error(field, 'Value is not a valid email')


app = Eve(validator = MyValidator)