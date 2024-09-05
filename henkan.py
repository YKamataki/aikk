from openai import OpenAI

def henkan(ipt:str, client) -> str:
    # get response
    res = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {'role': 'system', 'content': 'あなたはかな漢字変換器です。変換結果のみを出力すること。'},
                {'role': 'system', 'content': '入力された文章をかな漢字変換してください。'},
                {'role': 'user', 'content': ipt}
                ]
            )
    return res.choices[0].message

