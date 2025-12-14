[app]
title = GameMod
package.name = gamemod
package.domain = com.example.gamemod
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,plyer,dateutil,android
orientation = portrait
fullscreen = 0
p4a.hook = hook.py
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.sdk = 24
android.ndk = 23b
android.private_storage = True
android.arch = arm64-v8a,armeabi-v7a
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.arch = arm64
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
osx.python_version = 3
osx.kivy_version = 2.1.0
osx.sdk_version = 10.13
osx.deployment_target = 10.12

[buildozer]
log_level = 2
warn_on_root = 1
android.accept_sdk_license = True