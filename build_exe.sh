rm -rfv greencubic_exe/data
pyinstaller -w -i data/icon.ico --distpath greencubic_exe GreenCubic.py
cp -rv data greencubic_exe/data
cp -rvu WhatsNew.txt greencubic_exe/WhatsNew.txt
cp -rv dist/GreenCubic/* greencubic_exe
cp -rvu settings.ini greencubic_exe/settings.ini
rm -rfv greencubic_exe/GreenCubic
rm GreenCubic.spec
rm -rfv dist/GreenCubic

