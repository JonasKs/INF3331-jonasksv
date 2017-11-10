import re

def parse_nwodkram(text):
    """A parser to parse from nwodkram to HTML"""
    text = re.sub(r'(?<!\\)(\*)(.*?)(?<!\\)(\*)',r'<i>\2</i>',text) #Changing *text* to <i>text</i>
    text = re.sub(r'((?<!\\)\%(.*?)(?<!\\)\%)',r'<b>\2</b>',text) #Changing %text% to <b>text</b>
    text = re.sub(r'\[(.*?)\]\((http(s)?:\/\/)?(.*?)\)',r"<a href='\2\4'>\1</a>",text) #Changing [here](www.google.com) to <a href='www.google.com'>here</a> and so on
    if re.findall(r"(href='www*)",text): #If its no http:// or https:// do the following:
        text = re.sub(r"(href='www*)",r"href='http://www",text) #Change from href='www to href='http://www.
    text = re.sub(r"href='([^htp].*\..*)'", r"href='http://\1'", text)
    text = re.sub(r'\\\*','*',text) #Remove escape-characters, changing \* to *
    text = re.sub(r'\\\%','%',text) #Remove escape-characters, changing \% to %
    text = re.sub(r'\>\>(.*)(?=\n)',r'<blockquote>\1</blockquote>',text) #Change >> text to <blockcode>text</blockcode>
    text = re.sub(r'(\<(http://www|www)(.*?)\>)\(w=(\d*),h=(\d*)\)',r'<img src=\1" style="width:\4px;height:\5px;">',text) #Change to html height/width
    text = re.sub(r'\[wp:(.*?)\]', r'https://en.wikipedia.org/w/index.php?title=Special:Search%search=\1',text) #Change from [wp:QUERY] to https://...serach=QUERY
    return(text)

