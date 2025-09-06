# Implementa la función summarize y el CLI.
# Requisitos:
# - summarize(nums) -> dict con claves: count, sum, avg
# - Valida que nums sea lista no vacía y elementos numéricos (acepta strings convertibles a float).
# - CLI: python -m app "1,2,3" imprime: sum=6.0 avg=2.0 count=3

def summarize(nums):
    if not isinstance(nums, list) or not nums:
        raise ValueError(f"\n[!] La lista no puede ser vacía y debe ser tipo list")
    try:
        lista_floats = [float(x) for x in nums]
    except Exception:
        raise ValueError(f"\n[!]Todos los elementos deben ser numéricos")
    count = len(lista_floats)
    total = sum(lista_floats)
    promedio = total / count
    return {"count": count, "sum": total, "avg": promedio}


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        argumento = sys.argv[1]
    else:
        ""
    numeros = [arg.strip() for arg in argumento.split(",") if arg.strip()]
    resultado = summarize(numeros)
    print(f"\n[+] sum={resultado['sum']} avg={resultado['avg']} count={resultado['count']}")
