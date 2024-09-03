#!/usr/bin/env python3

import os
import subprocess

subprocess.run([
	"git",
	"-c",
	"advice.detachedHead=false",
	"clone",
	"--depth",
	"1",
	"--branch",
	"5.0",
	"https://github.com/raysan5/raylib.git",
])
os.chdir("./raylib/src")

subprocess.run([
	"make",
	"PLATFORM=PLATFORM_DESKTOP",
])
