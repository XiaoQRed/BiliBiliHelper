# -*- mode: python -*-

import sys
sys.path.append("Src")

block_cipher = None


# 编译前请将pathex更改为你储存的项目路径
a = Analysis(['main.py'],
             pathex=['C:\\Users\\TheWanderingCoel\\Desktop\\BiliBiliHelper'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='BiliBiliHelper',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
