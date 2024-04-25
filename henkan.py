from openai import OpenAI

def henkan(ipt:str, c) -> str:
    # get response
    messages = c.chat
    return messages[0]

