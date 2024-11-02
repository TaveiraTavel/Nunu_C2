class Colors:
    CYAN = '\033[96m'
    ERRO = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def color(text, colors):
    str_colors = ''
    i = 0
    for color in colors:
        str_colors += color
        i = i + 1
    
    return str_colors + text + (Colors.ENDC * i)

def error(text):
    return color(text, Colors.ERRO) + '\n'

def info(text):
    return color(text, [Colors.CYAN, Colors.BOLD])

def bold(text):
    return color(text, Colors.BOLD)
