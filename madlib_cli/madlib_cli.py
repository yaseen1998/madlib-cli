

import re
def read_file(path):
    try:
        file = open(path)
    except FileNotFoundError:
        content = "Error : Sorry file not found"
    else:
      

        content = file.readline()
        content = file.readline()
        content = file.readline()
        file.close()
       
    finally:
        return content

def madlib(content,replaceData):
    content=content.split('}')
    for j in range(len(content)):
        for i in replaceData:
            if i in content[j]:
                content[j] = content[j].replace('{'+i,input(f"write {i} : "))
    content =' '.join(content)
    return content

def importKeys(text):
    data = re.findall(r"\{(.*?)\}", text)
    # text = re.sub(r"\{(.*?)\}", '{}', text)
    return list(set(data))



if __name__=="__main__":
    content = read_file('./assets/madlib.txt')
    replaceData= (importKeys(content))
    lastText = madlib(content,replaceData)
    print(lastText)
    
    