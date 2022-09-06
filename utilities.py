# element should have the text property
def toText(element):
    try:
        return element.text.strip()
    except:
        print('failed to convert element to text')