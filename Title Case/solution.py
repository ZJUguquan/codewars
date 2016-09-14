'''
Best practice:

def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])
'''


def title_case(title, minor_words=''):
    if not title:
        return ''
    normalizedMinorWords = [word.lower() for word in minor_words.split(" ")]
    titleIt = iter(title.split(" "))
    result = [next(titleIt).capitalize()]
    for titleElem in titleIt:
        if( titleElem.lower() in normalizedMinorWords ):
            result.append(titleElem.lower())
        else:
            result.append(titleElem.capitalize())
    return " ".join(result)