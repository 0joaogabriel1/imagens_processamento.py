from PIL import Image

def abrir_imagem(caminho_imagem):
    """Abre uma imagem dado seu caminho."""
    try:
        img = Image.open(caminho_imagem)
        print(f"Imagem '{caminho_imagem}' aberta com sucesso.")
        return img
    except FileNotFoundError:
        print(f"Erro: Imagem não encontrada em '{caminho_imagem}'")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao abrir a imagem: {e}")
        return None

def converter_para_tons_de_cinza(imagem_obj):
    """Converte uma imagem para tons de cinza."""
    if imagem_obj:
        print("Convertendo imagem para tons de cinza...")
        return imagem_obj.convert("L")
    return None

def salvar_imagem(imagem_obj, caminho_saida):
    """Salva uma imagem no caminho especificado."""
    if imagem_obj:
        imagem_obj.save(caminho_saida)
        print(f"Imagem salva em '{caminho_saida}'.")