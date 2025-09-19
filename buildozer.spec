[app]

title = Auto app

package.name = carresale

package.domain = su.dolta.carresale

source.dir = ./src/

source.include_exts = py,png,jpg,kv,atlas,ttf,db

version = 0.1

requirements = python3,kivy,SQLAlchemy,kivymd,bcrypt

orientation = portrait

osx.python_version = 3

osx.kivy_version = 2.3.1

fullscreen = 0

android.permissions = android.permission.WRITE_EXTERNAL_STORAGE,android.permission.READ_EXTERNAL_STORAGE,android.permission.CAMERA

android.logcat_filter_custom_tags = False

android.api = 33

android.ndk = 25

android.minapi = 21

android.archs = arm64-v8a

android.allow_backup = True

android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1