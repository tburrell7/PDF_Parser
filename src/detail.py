class DetailType(enumerate):
    PROCEDURE = 1
    MEDICATION = 2
    ALLERGY = 3

class Detail(object):
    def __init__(self, type: DetailType, value: str, date: str, page: int):
        self.type = type
        self.value = value
        self.date = date
        self.page = page

