# fix_encoding.py
with open('backup_utf8.json', 'r', encoding='iso-8859-1') as f:
    content = f.read()

with open('backup_utf8_fixed.json', 'w', encoding='utf-8') as f:
    f.write(content)