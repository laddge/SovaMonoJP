import os
import fontforge
import inputmono
import togoshi


def main():
    PROJECTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
    inputmono_fn = inputmono.main()
    togoshi_fn = togoshi.main()
    font = fontforge.open(inputmono_fn)
    font.mergeFonts(togoshi_fn)
    font.generate(os.path.join(PROJECTDIR, 'fonts/Sova_Mono-Regular.ttf'))


if __name__ == '__main__':
    main()
