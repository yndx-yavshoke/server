from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Status code wrong, check this'
    WRONG_ELEMENT_COUNTS = "Number of items is not equal to expected"
    WRONG_BODY = "Body response not a correct"
    WRONG_TOKEN = "Wrong token"
