#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script para descomentar líneas 3814-4137 del archivo EL3204_01.tex

import os

file_path = r'c:\Users\Erik\Desktop\[Github] Auxiliares\Auxiliares\Proyecto Libro DIE\Libro DIE\EL3204_01\EL3204_01.tex'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Descomentar líneas 3814-4137 (índices 3813-4136 en Python)
count = 0
for i in range(3813, min(4137, len(lines))):
    if lines[i].startswith('%'):
        lines[i] = lines[i][1:]  # Quitar el primer carácter '%'
        count += 1

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("✓ Descomentado completado exitosamente!")
print(f"✓ Procesadas {count} líneas descomentadas de {min(4137, len(lines))-3813} líneas totales")
