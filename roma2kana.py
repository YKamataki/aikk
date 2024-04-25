def romaji_to_kana_convert(input_string):
    kana_table = {
        'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お',
        'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ',
        'sa': 'さ', 'shi': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ',
        'ta': 'た', 'chi': 'ち', 'tsu': 'つ', 'te': 'て', 'to': 'と',
        'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
        'ha': 'は', 'hi': 'ひ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ',
        'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も',
        'ya': 'や', 'yu': 'ゆ', 'yo': 'よ',
        'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ',
        'wa': 'わ', 'wo': 'を', 'nn': 'ん',

        'ga': 'が', 'gi': 'ぎ', 'gu': 'ぐ', 'ge': 'げ', 'go': 'ご',
        'za': 'ざ', 'ji': 'じ', 'zu': 'ず', 'ze': 'ぜ', 'zo': 'ぞ',
        'da': 'だ', 'di': 'ぢ', 'du': 'づ', 'de': 'で', 'do': 'ど',
        'ba': 'ば', 'bi': 'び', 'bu': 'ぶ', 'be': 'べ', 'bo': 'ぼ',
        'pa': 'ぱ', 'pi': 'ぴ', 'pu': 'ぷ', 'pe': 'ぺ', 'po': 'ぽ',

        'kya': 'きゃ', 'kyu': 'きゅ', 'kyo': 'きょ',
        'sha': 'しゃ', 'shu': 'しゅ', 'sho': 'しょ',
        'cha': 'ちゃ', 'chu': 'ちゅ', 'cho': 'ちょ',
        'nya': 'にゃ', 'nyu': 'にゅ', 'nyo': 'にょ',
        'hya': 'ひゃ', 'hyu': 'ひゅ', 'hyo': 'ひょ',
        'mya': 'みゃ', 'myu': 'みゅ', 'myo': 'みょ',
        'rya': 'りゃ', 'ryu': 'りゅ', 'ryo': 'りょ',

        'gya': 'ぎゃ', 'gyu': 'ぎゅ', 'gyo': 'ぎょ',
        'ja': 'じゃ', 'ju': 'じゅ', 'jo': 'じょ',
        'bya': 'びゃ', 'byu': 'びゅ', 'byo': 'びょ',
        'pya': 'ぴゃ', 'pyu': 'ぴゅ', 'pyo': 'ぴょ',
    }
    # 与えられた文字列を仮名に変換し、変換できた部分と残りの文字列を返す
    for length in range(min(len(input_string), 3), 0, -1):  # 最大3文字をチェック
        if input_string[:length] in kana_table:
            return kana_table[input_string[:length]], input_string[length:]
    return '', input_string  # 変換不可能な場合