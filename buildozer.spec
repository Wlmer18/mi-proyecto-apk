[app]
title = PSX Bridge
package.name = psxbridge
package.domain = org.wilmer
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Ajustamos la API a una más estándar y compatible
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
# Cambiamos log_level a 2 para tener más detalle si falla
log_level = 2
# warn_on_root = 1 ayuda a que no se detenga por el usuario root
warn_on_root = 1
