def valida_frete(task):
    if(10 < task['dimensao']['altura'] < 200) and (6 < task['dimensao']['largura'] < 140) and (task['peso'] > 0):
        entrega_ninja = {
            "nome": "Entrega Ninja",
            "valor_frete": (task['peso'] * 0.3) / 10,
            "prazo_dias": 6
        }
    else:
        entrega_ninja = None

    if(5 < task['dimensao']['altura'] < 140) and (13 < task['dimensao']['largura'] < 125) and (task['peso'] > 0):
        entrega_kabum = {
            "nome": "Entrega KaBuM",
            "valor_frete": (task['peso'] * 0.2) / 10,
            "prazo_dias": 4
        }
    else:
        entrega_kabum = None
    return entrega_ninja, entrega_kabum

def valida_retorno(entrega_ninja, entrega_kabum):
    if(entrega_kabum is not None) and (entrega_ninja is not None):
        return [entrega_ninja, entrega_kabum]
    elif(entrega_kabum is not None):
        return [entrega_kabum]
    elif(entrega_ninja is not None):
        return [entrega_ninja]
    else:
        return []
