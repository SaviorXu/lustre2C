import os
import re
import sys
import cfg

def get_all_terminal_kw(file_path):
    terminal_kw = set()
    with open(file_path) as fp:
        for line in fp.readlines():
            if "->" in line:
                infos = line.strip().split("->")[1].split(" ")
                for info in infos:
                    if cfg.TERMINAL.fullmatch(info):
                        terminal_kw.add(info)
    return terminal_kw


if __name__ == '__main__':
    terminals = get_all_terminal_kw(sys.argv[1])
    signals = list()
    for terminal in terminals:
        if terminal[0] >= 'a' and terminal[0] <= 'z':
            print('"' + terminal.upper() + "\",")
        else:
            signals.append(terminal)
    for signal in signals:
        print(signal)