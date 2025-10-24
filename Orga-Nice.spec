# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['updated_finals.py'],
    pathex=[],
    binaries=[],
    datas=[('undo_confirmation.mp3', '.'), ('success.mp3', '.'), ('organizingfiles_sound.mp3', '.'), ('clicksound.mp3', '.'), ('welcome.mp3', '.'), ('continue.mp3', '.'), ('guide.mp3', '.'), ('valid_format.mp3', '.'), ('music.mp3', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Orga-Nice',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
