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

def equal_details(detail_a: Detail, detail_b: Detail) -> bool:
    """returns true if two Detail objects have the same page and value."""
    if (detail_a.value == detail_b.value) & (detail_a.page == detail_b.page):
        return True
    return False

def sort_details(details: list[Detail]) -> list[Detail]:
    """sorts details in page order and then in alphabetical order. Also removes duplicates."""
    if len(details) == 0:
        return []
    
    details.sort(key=lambda obj: obj.value)
    details.sort(key=lambda obj: obj.page)
    
    result = [details[0]]
    i = 0
    j = 1
    while j < len(details):
        if equal_details(details[i], details[j]):
            j += 1
        else:
            result.append(details[j])
            i = j
            j += 1

    return result
