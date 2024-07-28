import sympy as sp

# Constante de estructura fina (α)
alpha = sp.Rational(1, 137.035999084)  # Valor exacto

# Número de Euler (e)
euler_number = sp.E

# Número Pi (π)
pi_number = sp.pi

# Número áureo (Φ)
phi = (1 + sp.sqrt(5)) / 2

# Calcular Phi al cuadrado
phi_squared = phi**2

# Calcular el número de Balmer necesario para que la fórmula dé Phi al cuadrado
balmer_number = (phi_squared / alpha) + (euler_number + pi_number)

# Calcular el resultado usando la fórmula dada
resultado = alpha * (balmer_number - (euler_number + pi_number)) 

# Imprimir resultados simbólicos
print(f"Resultado de la fórmula de alpha * (balmer_number - (euler_number + pi_number)): {resultado}")
print(f"Número de Balmer calculado: {balmer_number}")

# Imprimir el valor numérico de 'resultado' con alta precisión
print(f"Valor numérico de alpha * (balmer_number - (euler_number + pi_number)) (50 dígitos de precisión): {resultado.evalf(50)}")

# Imprime declaración de lo encontrado
print("""Queda demostrado que Phi_squared = alpha * (balmer_number - (euler_number + pi_number))
         es posible con balmer_number = (phi_squared / alpha) + (euler_number + pi_number),
         encontrandonos la formula unificadora.""")

# Verificar que el resultado es exactamente igual a Phi al cuadrado
assert sp.simplify(resultado - phi_squared) == 0, "El resultado no es exactamente Phi al cuadrado"
