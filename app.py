import curses

from roma2kana import romaji_to_kana_convert

def main(stdscr):
    # curses.curs_set(0)  # カーソル非表示
    stdscr.nodelay(True)  # 非ブロッキングモード
    input_str = ''
    display_str = ''
    while True:
        key = stdscr.getch()
        if key == ord('q'):  # 'q'で終了
            break
        elif key != -1:
            char = chr(key)
            if char.isalpha():  # アルファベットのみ処理
                input_str += char.lower()  # 小文字に統一
                converted, input_str = romaji_to_kana_convert(input_str)
                if converted:
                    display_str += converted
            stdscr.clear()
            stdscr.addstr(0, 0, "Combined: " + display_str + input_str)  # 結合された文字を表示

if __name__ == '__main__':
    curses.wrapper(main)