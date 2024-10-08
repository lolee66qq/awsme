def mahos():
    anim = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□","[\x1b[1;92m■■\x1b[0m□□□□□□□□", "[\x1b[1;93m■■■\x1b[0m□□□□□□□", "[\x1b[1;95m■■■■\x1b[0m□□□□□□", "[\x1b[1;94m■■■■■\x1b[0m□□□□□", "[\x1b[38;5;26m■■■■■■\x1b[0m□□□□", "[\x1b[1;96m■■■■■■■\x1b[0m□□□", "[\x1b[38;5;86m■■■■■■■■\x1b[0m□□", "[\x1b[38;5;96m■■■■■■■■■\x1b[0m□", "[\x1b[38;5;203m■■■■■■■■■■\x1b[0m]"]
    am = ('\x1b[38;5;203m','\x1b[38;5;203m','\x1b[38;5;203m','\x1b[38;5;203m','\x1b[38;5;203m','\x1b[38;5;203m')
# coding: utf-8

# Author   : 𝐒𝐃𝐌
# Facebook : fb.com/𝐒𝐃𝐌
# Github   : حبيبي ولله
# Twitter  : 𓆩 ⏤͟͞𝐒𝐃𝐌 ⇄ نـمـࢪود⏤͟͞🇷🇺⃤ 𓆪
# Youtube  : 𓆩 ⏤͟͞𝐒𝐃𝐌 ⇄ نـمـࢪود⏤͟͞🇷🇺⃤ 𓆪
# 1st Release : 12-June-2023
###############
a1 = '\x1b[1;31m'  # أحمر
a4 = '\x1b[1;33m'  # أصفر
a2 = '\x1b[1;34m'  # أزرق
M = '\033[2;36m' #سماوي
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a9 = '\x1b[1;37m'  # أبيض
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a16 ='\x1b[38;5;48m'
a40 = '\x1b[38;5;117m'  # أزرق سماوي
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
#############################
import os
import sys
from sys import version_info as ver
from time import sleep as ghum
from datetime import datetime
import shutil
import base64
import zlib
import marshal
import py_compile
import subprocess
try:
    from pathlib2 import Path
except ImportError:
    from pathlib import Path

__import__("colorama").just_fix_windows_console() if os.name == "nt" else None

# messages
err = "\033[1;31m[\033[1;34m~\033[1;31m]\033[0m "
suc = "\033[1;32m[\033[1;97m+\033[1;32m]\033[0m "
msg = err + "Oh! Damn Input\n"
_inp_ = suc + "Input your .py-file: "
inv = err + "Invalid Choice!\n"
fe = err + "File Not Found!"
usp = err + "Python Version not Supported"
done = suc + "Your Script is Compiled Successfully!"
_exit_ = suc + "Tool Exited!\n"
note = """
 <---- [ :Note: ] ---->

    # Encryptionn loop can't be 0
    # Char Encryption loop Limit 5
    # Base2 Encryption loop Limit 3
    # Base16, Base32 Encryption loop Limit 13
    # Others Encryption loop limit 40
    
    * Try to Use the same Python Version to run the Crypted Script. Some will not work on different Py Version
    * You can do it more times after running the tool again and crypting your last crypt

 <---- [ :END: ] ---->

"""

# Version Optimizing
if ver[0] == 2:
    def int_inp(data):
        return input(data)
    def str_inp(data):
        return raw_input(data)
elif ver[0] == 3:
    def int_inp(data):
        return int(input(data))
    def str_inp(data):
        return str(input(data))
else:
    print(err + "Oops! Python Version not Supported")

# clearing the terminal
cls = lambda: os.system("clear") if os.name == "posix" else (os.system("cls") if os.name == "nt" else None)

cls()

# banner
os.system('pip install python-cfonts')
import requests
print(('—'*25)+'\n• The programmer ☆𝑆𝐷𝑀☆ Nimrod •\n'+('—'*25))
print('\n   ''\x1b[38;5;153m'' ''\x1b[38;5;153m'' \n░██████╗██████╗░███╗░░░███╗\n██╔════╝██╔══██╗████╗░████║\n╚█████╗░██║░░██║██╔████╔██║\n░╚═══██╗██║░░██║██║╚██╔╝██║\n██████╔╝██████╔╝██║░╚═╝░██║\n╚═════╝░╚═════╝░╚═╝░░░░░╚═╝')
print(a21+'▭▬'*15)
print(a14+' المبرمج نمرود | @I_213')
print(a21+'▭▬'*15)
print(a14+' المبرمج سلفادور | @Me_Nimrod')
print(a21+'▭▬'*15)

print(a16+' [01] Char [👀] ') 
print(a21+'▭▬'*15)
print(a16+' [02] Base2 [🔥] ') 
print(a21+'▭▬'*15)
print(a16+' [03] Base16 [🍓] ') 
print(a21+'▭▬'*15)
print(a16+' [04] Base32 [😩]') 
print(a21+'▭▬'*15)
print(a16+' [05] Base64 [⚡] ') 
print(a21+'▭▬'*15)
print(a16+' [06] Base85  [Only py3] [🐊] ') 
print(a21+'▭▬'*15)
print(a16+' [07] Zlib [😜] ')
print(a21+'▭▬'*15)
print(a16+' [08] Marshal [🔒] ') 
print(a21+'▭▬'*15)
print(a16+' [09] pycompile [🐲] ') 
print(a21+'▭▬'*15)
print(a16+' [10] Cythonize [Only py3] [☠️] ') 
print(a21+'▭▬'*15)
print(a16+' [11] Zlib, Base16 [😀] ') 
print(a21+'▭▬'*15)
print(a16+' [12] Zlib, Base32 [😉] ') 
print(a21+'▭▬'*15)
print(a16+' [13] Zlib, Base64 [😴] ')
print(a21+'▭▬'*15) 
print(a16+' [14] Marshal, Zlib [😅] ') 
print(a21+'▭▬'*15)
print(a16+' [15] Marshal, Base16 [😑] ') 
print(a21+'▭▬'*15)
print(a16+' [16] Marshal, Base32 [🙃] ') 
print(a21+'▭▬'*15)
print(a16+' [17] Marshal, Base64 [💤] ') 
print(a21+'▭▬'*15)
print(a16+' [18] Base16, Zlib, Marshal [😈] ') 
print(a21+'▭▬'*15)
print(a16+' [19] Base32, Zlib, Marshal [🏴‍☠️] ') 
print(a21+'▭▬'*15)
print(a16+' [20] Base64, Zlib, Marshal [💬] ') 
print(a21+'▭▬'*15)
print(a16+' [21] Base85, Zlib, Marsha [Only py3] [🧊] ') 


credit = """# Compiled by : Mi-PyCrypt
# Author      : 𝐒𝐃𝐌
# Github      : github.com/𝐒𝐃𝐌
# Python      : %s
# Time        : %s

""" % (sys.version.split()[0], (datetime.now()).strftime("%d-%B-%Y %A %I:%M%p"))
###############
a1 = '\x1b[1;31m'  # أحمر
a4 = '\x1b[1;33m'  # أصفر
a2 = '\x1b[1;34m'  # أزرق
M = '\033[2;36m' #سماوي
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a9 = '\x1b[1;37m'  # أبيض
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a16 ='\x1b[38;5;48m'
a40 = '\x1b[38;5;117m'  # أزرق سماوي
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
#############################
# encryption
def _chr_(_data_):
    return ",".join(["chr(%s)" % str(ord(dick)) for dick in _data_]) if ver[0] == 2 else ",".join(["chr(%s)" % str(dick) for dick in _data_])
def b2encode(_paka_mal_):
    return ''.join([format(ord(char), "08b") for char in _paka_mal_]) if ver[0] == 2 else ''.join([format(dick, "08b") for dick in _paka_mal_])

data = lambda f : f.encode('utf-8')
chr_ = lambda f : _chr_(f)
b2 = lambda f : b2encode(f)
b16 = lambda f : base64.b16encode(f)
b32 = lambda f : base64.b32encode(f)
b64 = lambda f : base64.b64encode(f)
b85 = lambda f : base64.b85encode(f)
zb = lambda f : zlib.compress(f)
marsh = lambda f : marshal.dumps(compile(f, '<Faliure 28-07-2021>', 'exec'))

# restart process
def restart():
    ghum(1); cls(); print(banner); print(menu)

# File Handling
def Encrypt_file(main_input, enc_code, dec_code):
    inp_file = str_inp(_inp_)
    if os.path.exists(inp_file):
        pass
    else:
        sys.exit(fe)
    f_path = Path(inp_file)
    file = f_path.name
    _mal_ = open(file, "r").read()
    while True:
        try:
            count = int_inp(suc + "Encryption Count: ")
            69 / count
            if main_input == 1:
                if count < 6:
                    break
                else:
                    sys.exit(note)
            elif main_input == 2:
                if count < 4:
                    break
                else:
                    sys.exit(note)
            elif 2 < main_input < 5:
                if count < 14:
                    break
                else:
                    sys.exit(note)
            else:
                if count <=40:
                    break
                else:
                    sys.exit(note)
            break
        except ValueError:
            print(msg)
        except ZeroDivisionError:
            print(note)

    for _enc_ in range(count):
        try:
            if main_input != 14 and main_input != 8 and main_input != 7:
                _mal_ = 'eval("exec((_1nf3r10r_)(%s))")' % repr(eval(enc_code)) if ver[0] == 3 else "exec((_1nf3r10r_)(%s))" % repr(eval(enc_code))
            else:
                _mal_ = "exec((_1nf3r10r_)(%s))" % repr(eval(enc_code))
        except TypeError as er:
            print(err + er)
    NewFile = file.replace(".py", "") + "_crypt.py"
    with open(NewFile, "w") as out:
        out.write(credit + dec_code + _mal_)
        out.close()
    path = os.path.abspath(NewFile)
    print(done)
    print(suc + "Output Path: " + path)

def pycompile():
    inp_file = str_inp(_inp_)
    if os.path.exists(inp_file):
        pass
    else:
        sys.exit(fe)
    f_path = Path(inp_file)
    file = f_path.name
    NewFile = file.replace(".py", "") + "_crypt.py"
    py_compile.compile(file, NewFile)
    path = os.path.abspath(NewFile)
    print(done)
    print(suc + "Output Path: " + path)

def cythonize():
    inp_file = str_inp(_inp_)
    if os.path.exists(inp_file):
        pass
    else:
        sys.exit(fe)
    f_path = Path(inp_file)
    file = f_path.name
    NewFile = file.replace(".py", "")
    try:
        from distutils.core import setup
        from distutils.extension import Extension
        from Cython.Build import cythonize
    except ImportError:
        subprocess.run("pip install cython", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
        cythonize()
    extensions = [
        Extension(NewFile, [NewFile + ".py"]),
    ]
    setup(
        script_name=__file__,
        script_args=["build_ext", "--inplace"],
        ext_modules=cythonize(extensions, language_level=3),
    )
    path = os.path.dirname(os.path.abspath(__file__))
    print(done)
    print(suc + "Output Path: " + path)

# menus
def main():
    try:
        u_i = int_inp(suc + "اختر فرخي: ")
        if u_i == 0:
            sys.exit(_exit_)
        elif u_i == 99:
            if ver[0] == 2:
                print(err + "Use python3 to Update!")
            elif ver[0] == 3:
                subprocess.run("git pull origin", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
                print(suc + "Tool Updated Successfully!")
                restart(); main()
            else:
                None
        elif u_i == 69:
            try:
                shutil.rmtree("__pycache__")
            except FileNotFoundError if ver[0] == 3 else OSError:
                pass
            try:
                shutil.rmtree("build")
            except FileNotFoundError if ver[0] == 3 else OSError:
                pass
            print(suc + "Clean Done!")
            restart(); main()
        elif u_i == 70:
            print(note)
        elif u_i == 71:
            print(suc + """Check Your Internet Connection and Keep Patience for Installing Dependencies,
    Otherwise Do it on your own by running 'pip3 install -r requirements.txt' and 
    'pip2 install -r requirements.txt'""")
            print(suc + "Please Wait until Install is Done!...")
            os.system("pip3 install -r requirements.txt") if ver[0] == 3 else os.system("pip2 install -r requirements.txt")
            print(suc + "Install Done!")
            restart(); main()

        # single encryption
        elif u_i == 1:
            enc = "chr_(data(_mal_))"
            run = "_1nf3r10r_ = lambda __1nf3r10r__ : ''.join(eval(__1nf3r10r__));"
            Encrypt_file(u_i, enc, run)
        elif u_i == 2:
            enc = "b2(data(_mal_))[::-1]"
#             run = """# Note: You have to install base2 for running this tool, pip2 or pip install base2-Inferior.
# _1nf3r10r_ = lambda __1nf3r10r__ : __import__('base2').b2decode(__1nf3r10r__[::-1]);"""
            run = "_1nf3r10r_ = lambda __1nf3r10r__ : ''.join(chr(int((__1nf3r10r__[::-1])[i:i+8], 2)) for i in range(0, len(__1nf3r10r__), 8));"
            # run = "from src.base2 import b2decode;_1nf3r10r_ = lambda __1nf3r10r__ : b2decode(__1nf3r10r__[::-1]);"
            Encrypt_file(u_i, enc, run)
        elif u_i == 3:
            enc = "b16(data(_mal_))[::-1]"
            run = "_1nf3r10r_ = lambda __1nf3r10r__ : __import__('base64').b16decode(__1nf3r10r__[::-1]);"
            Encrypt_file(u_i, enc, run)
        elif u_i == 4:
            enc = "b32(data(_mal_))[::-1]"
            run = "_1nf3r10r_ = lambda __1nf3r10r__ : __import__('base64').b32decode(__1nf3r10r__[::-1]);"
            Encrypt_file(u_i, enc, run)
        elif u_i == 5:
            enc = "b64(data(_mal_))[::-1]"
            run = "_1nf3r10r_ = lambda __1nf3r10r__ : __import__('base64').b64decode(__1nf3r10r__[::-1]);"
            Encrypt_file(u_i, enc, run)
        elif u_i == 6:
            enc = "b85(data(_mal_))[::-1]"
            run = "_1nf3r10r_ = lambda __1nf3r10r__ : __import__('base64').b85decode(__1nf3r10r__[::-1]);"
            Encrypt_file(u_i, enc, run) if ver[0] == 3 else sys.exit(usp)
        elif u_i == 7:
            enc = "zb(data(_mal_))[::-1]"
            run = "_1nf3r10r_ = lambda __1nf3r10r__ : __import__('zlib').decompress(__1nf3r10r__[::-1]);"
            Encrypt_file(u_i, enc, run)
        elif u_i == 8:
            enc = "marsh(data(_mal_))[::-1]"
            run = "_1nf3r10r_ = lambda __1nf3r10r__ : __import__('marshal').loads(__1nf3r10r__[::-1]);"
            Encrypt_file(u_i, enc, run)
        elif u_i == 9:
            pycompile()
        elif u_i == 10:
            cythonize() if ver[0] == 3 else sys.exit(usp)

        # mixed encryption
        elif u_i == 11:
            enc = "b16(zb(data(_mal_)))[::-1]"
            run = "_1nf3r10r_ = lambda __1nf3r10r__ : __import__('zlib').decompress(__import__('base64').b16decode(__1nf3r10r__[::-1]));"
            Encrypt_file(u_i, enc, run)
        elif u_i == 12:
            enc = "b32(zb(data(_mal_)))[::-1]"
            run = "_1nf3r10r_ = lambda __1nf3r10r__ : __import__('zlib').decompress(__import__('base64').b32decode(__1nf3r10r__[::-1]));"
            Encrypt_file(u_i, enc, run)
        elif u_i == 13:
            enc = "b64(zb(data(_mal_)))[::-1]"
            run = "_1nf3r10r_ = lambda __1nf3r10r__ : __import__('zlib').decompress(__import__('base64').b64decode(__1nf3r10r__[::-1]));"
            Encrypt_file(u_i, enc, run)
        elif u_i == 14:
            enc = "zb(marsh(data(_mal_)))[::-1]"
            run = "_1nf3r10r_ = lambda __1nf3r10r__ : __import__('marshal').loads(__import__('zlib').decompress(__1nf3r10r__[::-1]));"
            Encrypt_file(u_i, enc, run)
        elif u_i == 15:
            enc = "b16(marsh(data(_mal_)))[::-1]"
            run = "_1nf3r10r_ = lambda __1nf3r10r__ : __import__('marshal').loads(__import__('base64').b16decode(__1nf3r10r__[::-1]));"
            Encrypt_file(u_i, enc, run)
        elif u_i == 16:
            enc = "b32(marsh(data(_mal_)))[::-1]"
            run = "_1nf3r10r_ = lambda __1nf3r10r__ : __import__('marshal').loads(__import__('base64').b32decode(__1nf3r10r__[::-1]));"
            Encrypt_file(u_i, enc, run)
        elif u_i == 17:
            enc = "b64(marsh(data(_mal_)))[::-1]"
            run = "_1nf3r10r_ = lambda __1nf3r10r__ : __import__('marshal').loads(__import__('base64').b64decode(__1nf3r10r__[::-1]));"
            Encrypt_file(u_i, enc, run)
        elif u_i == 18:
            enc = "b16(zb(marsh(data(_mal_))))[::-1]"
            run = "_1nf3r10r_ = lambda __1nf3r10r__ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__1nf3r10r__[::-1])));"
            Encrypt_file(u_i, enc, run)
        elif u_i == 19:
            enc = "b32(zb(marsh(data(_mal_))))[::-1]"
            run = "_1nf3r10r_ = lambda __1nf3r10r__ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__1nf3r10r__[::-1])));"
            Encrypt_file(u_i, enc, run)
        elif u_i == 20:
            enc = "b64(zb(marsh(data(_mal_))))[::-1]"
            run = "_1nf3r10r_ = lambda __1nf3r10r__ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__1nf3r10r__[::-1])));"
            Encrypt_file(u_i, enc, run)
        elif u_i == 21:
            enc = "b85(zb(marsh(data(_mal_))))[::-1]"
            run = "_1nf3r10r_ = lambda __1nf3r10r__ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode(__1nf3r10r__[::-1])));"
            Encrypt_file(u_i, enc, run) if ver[0] == 3 else sys.exit(usp)

        else:
            print(inv)
            restart(); main()

    except (ValueError):
        print(msg)
        restart(); main()
    except (KeyboardInterrupt, EOFError):
        sys.exit("\n" + suc + "Canceled!\n")


if __name__ == "__main__":
    main()
