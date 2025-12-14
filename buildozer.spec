[app]
title = 极速换肤2.0.0  # APP名称
version = 2.0.0  # 版本号（必填）
package.name = gameskinmod  # 包名（小写无空格）
package.domain = org.yourname  # 自定义域名
source.dir = .  # 源码目录
source.include_exts = py,png,jpg,kv,atlas  # 包含文件类型
source.exclude_exts = pyc,pyo,pyd,gitignore,md  # 排除无用文件
source.include_dirs = assets  # 内置文件目录
requirements = python3,kivy==2.3.0,plyer==2.1.0,python-dateutil==2.8.2,pillow==10.2.0
android.sdk = 24  # 最低安卓版本
android.api = 33  # 目标安卓API
android.ndk = 25b  # 适配Kivy的NDK版本
android.buildtools = 33.0.2  # 构建工具版本
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.request_legacy_external_storage = True  # 安卓10+读写权限适配
android.release = False  # Debug模式
android.icon = icon.png  # APP图标

[buildozer]
log_level = 2  # 日志级别
warn_on_root = 1  # 根目录警告
build_dir = .buildozer  # 构建目录