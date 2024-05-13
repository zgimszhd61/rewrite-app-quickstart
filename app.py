#coding:utf-8
from openai import OpenAI
import os,re
os.environ["OPENAI_API_KEY"] = "sk-proj-"

def askGPT3(mprompt):
    sprompt = "下面内容是粗译的结果，请整理原文并意译，使之更符合中国人阅读理解习惯，注意说人话。"
    client = OpenAI()
    try:
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": sprompt},
            {"role": "user", "content": mprompt}
        ]
        )
        result = completion.choices[0].message.content.strip()
        print(result)
        writecontent(result + "\n\n")
        return(result)
    except:
        print("ERROR")


def writecontent(content):
    with open('/Users/a0000/mywork/commonLLM/opensource/nnnew/rewrite-app-quickstart/origin/output.txt', 'a+') as file:
        file.write(content)


text = ""
with open("/Users/a0000/mywork/commonLLM/opensource/nnnew/rewrite-app-quickstart/origin/freebuf-01.txt", 'r') as file:
    # 逐行读取内容
    for line in file:
        # 打印每一行的内容（去除末尾的换行符）
        text = text + line.strip() + "。"
            # print()
# print(text)
segs = re.split("(。|？|，)", text)
buffer = ""
for line in segs:
    if len(buffer) > 250:
        askGPT3(buffer)
        # print(buffer)
        print()
        buffer = line
    else:
        buffer = buffer + line
# print(buffer)
askGPT3(buffer)