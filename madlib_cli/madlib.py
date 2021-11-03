
import re
def read_template(path):
    """
    in this function I open the txt file and return what it conten
    """
    print("""
    ***************************************************************************************************
    *** this is game for fun will ask you to enter some words and will give back to you a paragraph ***
    ***************************************************************************************************
    """)
    file = open(path) # open txt file
    content = file.read() # store the txt in conten
    file.close() # close the txt filr
    return content




def merge(path,forma):
    """
    format txt file to replace every {} to specific word
    """
    return path.format(*forma)
    
def parse_template(content):
    """
    in this function first I find and store key of txt file 
    second I replace this key to {}
    """
    # result=[]
    # path=content.split()
    # for i in path:
    #     if i.startswith('{'):
    #         result.append(i[1:-1])
    # arr = tuple(result)
    # res = dict.fromkeys(arr, '{}')
    # last = (content.format(**res))


    # return(last,tuple(arr))

    data = re.findall(r"\{(.*?)\}", content) # find key of txt
    text = re.sub(r"\{(.*?)\}", '{}', content) # replace key to {}
    return (text,tuple(data))

    # print(*arr)

def madlib(content,replaceData):
    """
    extra function just for practice another ways for format document
    """
    replaceData=list(set(replaceData)) # keys of txt
    content=content.split('}')
    for j in range(len(content)):
        for i in replaceData:
            if i in content[j]:
                content[j] = content[j].replace('{'+i,input(f"write {i} : "))
    content =' '.join(content)
    return content

if __name__=="__main__":
    content = read_template('./assets/madlib.txt')
    data,replaceData= (parse_template(content))
    lastText = madlib(content,replaceData)
    print(lastText)
    