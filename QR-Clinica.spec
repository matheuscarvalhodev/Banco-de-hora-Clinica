# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['sys_qr_code.py'],
             pathex=['C:\\Users\\Matheus\\Desktop\\QR_Ufopa'],
             binaries=[],
             datas=[('leitor_qr.ui', '.'), ('libiconv.dll', '.'), ('libzbar-64.dll', '.')],
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
          [],
          exclude_binaries=True,
          name='QR-Clinica',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='_imagens\\clinica-_2_.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='QR-Clinica')
