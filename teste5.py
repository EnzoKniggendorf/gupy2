def inverter_string(s):
    invertida = ''
    for char in s:
        invertida = char + invertida
    return invertida

string_informada = "Python"
print(inverter_string(string_informada))  # Saída: nohtyP
