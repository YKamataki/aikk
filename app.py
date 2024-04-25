import curses

from roma2kana import romaji_to_kana_convert

def main(stdscr):
    curses.curs_set(0)  # カーソル非表示
    stdscr.nodelay(True)  # 非ブロッキングモード
    input_str = ''
    display_str = ''

    # 表示を初期化
    stdscr.clear()
    stdscr.addstr(0, 0, "> " + display_str + input_str)  # 結合された文字を表示
    while True:
        key = stdscr.getch()
        if key == ord('q') or \
            key == ord('c') or \
            key == ord('v'):
            break
        if key == ord("\n"):  # Enterで変換
            stdscr.clear()
            stdscr.addstr(0, 0, "> " + display_str + input_str)  # 結合された文字を表示
            stdscr.addstr(1, 0, "Not Implemented\n")
        elif key != -1:
            char = chr(key)
            if char.isalpha():  # アルファベットのみ処理
                input_str += char.lower()  # 小文字に統一
                converted, input_str = romaji_to_kana_convert(input_str)
                if converted:
                    display_str += converted
            stdscr.clear()
            stdscr.addstr(0, 0, "> " + display_str + input_str)  # 結合された文字を表示

if __name__ == '__main__':
    curses.wrapper(main)
