import re
import os
import shutil
from typing import List



def match_dump(matcher, items) -> str:
    g = matcher.group()
    if not need_replace(matcher):
        return g

    items.append(g)
    return g


def match_convert(matcher: re.Match, items: List[str]) -> str:
    g = matcher.group()
    if not need_replace(matcher):
        return g

    return f'"{items.pop(0)}"'


system_strs = ['play music', 'play sound', '$']
def need_replace(matcher: re.Match) -> bool:
    """
    ゲームシステムの文字は対象外にする
    """
    g = matcher.group()
    if g == '':
        return False

    s = matcher.start()
    prevLfIdx = max(matcher.string.rfind('\n', 0, s), 0)
    checkstr = matcher.string[prevLfIdx:s]

    if any(gs in checkstr for gs in system_strs):
        return False

    return True


def create_trans_input(input_file: str, start_line: int):
    """
    翻訳データ抽出用
    """
    with open(input_file, encoding='utf-8') as f:
        input = f.readlines()

    label = ''.join(input[start_line:])
    #　エスケープ文字「\"」は扱い面倒なので、セリフではめったに使わないバッククォートに一旦おく
    escaped = re.sub(r'\\"', r'`', label)
    items = []
    # 「"」で囲まれた範囲を対象とする
    re.sub(r"([\"])[^\1]*?\1", lambda x: match_dump(x, items), escaped)

    # htmlぽいものとして書き出すので、別途Chromeで翻訳してテキストを管理する
    with open(f'{input_file}_labels.html', mode='w', encoding='utf-8') as f:
        t = '</p>\n<p>'.join(items)
        f.write(re.sub(r'"', r'', t))


def transrate(input_file: str, translated_file: str, start_line: int) -> str:
    """
    日本語データの適用
    """
    with open(input_file, encoding='utf-8') as f:
        input = f.readlines()

    with open(translated_file, encoding='utf-8') as f:
        translated = [re.sub('\n', '', x) for x in f.readlines() if x != '\n']

    label_str = ''.join(input[start_line:])
    escaped = re.sub(r'\\"', r'`', label_str)
    replaced = re.sub(r"([\"])[^\1]*?\1",
                      lambda x: match_convert(x, translated), escaped)
    unescaped = re.sub(r'`', r'\\"', replaced)

    return''.join(input[:start_line]) + unescaped

def trans_gui(input_file:str)->str:
    """
    フォント置換
    """
    with open(input_file, encoding='utf-8') as f:
        input = f.read()
    return re.sub(r'"Louis George Cafe.ttf"', r'"SourceHanSansLite.ttf"', input)

# define
script_file = 'script.rpy'
script_org_file = script_file+'.org'
translate_file = 'translated.txt'
label_start_line = 1006

gui_file = 'gui.rpy'
gui_org_file = gui_file + '.org'

# back up
if not os.path.exists(script_org_file):
    shutil.copy2(script_file, script_org_file)

if not os.path.exists(gui_org_file):
    shutil.copy2(gui_file, gui_org_file)


# # 翻訳用データ抽出
# create_trans_input(org_file, label_start_line)

# 翻訳データ置き換え
script_trans = transrate(script_org_file, label_start_line)
with open(script_file, mode='w', encoding='utf-8') as f:
    f.write(script_trans)


# フォント名置き換え
gui_trans = trans_gui(gui_org_file)
with open(gui_file, mode='w', encoding='utf-8') as f:
    f.write(gui_trans)