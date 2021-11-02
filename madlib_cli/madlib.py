
import re
def read_template(path):
    print("""
    ***************************************************************************************************
    *** this is game for fun will ask you to enter some words and will give back to you a paragraph ***
    ***************************************************************************************************
    """)
    file = open(path)
    content = "Error : Sorry file not found"
    content = file.read() 
    file.close()
    return content




def merge(path,forma):
    return path.format(*forma)
    
def parse_template(content):
    # result=[]
    # path=content.split()
    # for i in path:
    #     if i.startswith('{'):
    #         result.append(i[1:-1])
    # arr = tuple(result)
    # res = dict.fromkeys(arr, '{}')
    # last = (content.format(**res))


    # return(last,tuple(arr))

    data = re.findall(r"\{(.*?)\}", content)
    text = re.sub(r"\{(.*?)\}", '{}', content)
    return (text,tuple(data))

    # print(*arr)

def madlib(content,replaceData):
    replaceData=list(set(replaceData))
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
    