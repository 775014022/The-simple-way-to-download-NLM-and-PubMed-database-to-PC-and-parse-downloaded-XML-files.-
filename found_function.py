#Different find and parse mode to suite data structure
def directfind(element,Xpath): #return text
    temp = element.find(Xpath)
    if temp is None:
        return ""
    text = temp.text
    if  text is None:
        return ""
    return text
def allfind(element,Xpath): #return
    temps = element.findall(Xpath)
    if temps is None:
        return ""
    temp_list =  []
    for temp in temps:
        text = temp.text
        if text is None:
            temp_list.append("")
        else:
            temp_list.append(text)

    return "/".join(temp_list)

def sub_allfind(element,Xpath):
    temps = element.findall(Xpath) #author Affliation
    if temps is None:
        return ""
    temp_list = []
    for temp in temps:
        text = temp.text
        if text is None:
            temp_list.append("")
        else:
            temp_list.append(text)

    return ";".join(temp_list)

def element_None_judge(element,Xpath):
    if element.find(Xpath) is None:
        return None

