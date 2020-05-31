rm -rfv greencubic_exe/data
cp -rv data greencubic_exe/data
cp -rvu WhatsNew.txt greencubic_exe/WhatsNew.txt
pyinstaller -F -w -i data/icon.ico --distpath greencubic_exe GreenCubic.py
rm GreenCubic.spec
