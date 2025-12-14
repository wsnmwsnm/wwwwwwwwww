[app]
title = GameMod
package.name = gamemod
package.domain = org.gamemod
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt
source.exclude_exts = spec,yml
source.exclude_dirs = .git,__pycache__,bin,.buildozer
source.include_patterns = assets/*,icon.png
icon.filename = icon.png
version = 0.1
main.py = main.py
requirements = python3,kivy==2.3.0,plyer==2.1.0
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.ndk = 25b
android.api = 33
android.ndk_api = 21
android.build_tools_version = 33.0.2
android.enable_androidx = True
p4a.branch = master
p4a.bootstrap = sdl2
ios.deployment_target = 
ios.sdk = 
ios.codesign.allowed = False
[buildozer]
log_level = 2
warn_on_root = 1
[android]
arch = armeabi-v7a,arm64-v8a