import os, shutil

def copy_dir(src, dst):
    if os.path.isdir(src):
        os.makedirs(dst, exist_ok=True)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                copy_dir(s, d)
            else:
                shutil.copy(s, d)
    else:
        shutil.copy(src, dst)