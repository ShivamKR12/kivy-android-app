[app]
# title = My App
# package.name = myapp
title = Pygame App
package.name = pygameapp
package.domain = org.test

version = 0.1

source.dir = .
source.include_exts = py,png,jpg,kv,ttf

# requirements = python3,kivy
requirements = python3,pygame

android.bootstrap = sdl2

android.permissions = INTERNET

android.archs = arm64-v8a

# (optional but safe defaults)
fullscreen = 1
orientation = portrait

[buildozer]
warn_on_root = 0
