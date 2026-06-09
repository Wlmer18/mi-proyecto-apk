[app]
title = PSX Bridge
package.name = psxbridge
package.domain = org.wilmer
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,flask,requests
orientation = portrait
fullscreen = 0

# Configuración de Android
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.ndk_api = 21
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
