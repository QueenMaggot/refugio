
# convert_to_utf8.py
input_file = 'backup_utf8.json'
output_file = 'backup_utf8_fixed.json'

# Intenta leer como latin1 (ISO-8859-1) o cp1252
with open(input_file, 'r', encoding='latin1') as f:
    content = f.read()

# Guarda como UTF-8 válido
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Archivo convertido y guardado como {output_file}")