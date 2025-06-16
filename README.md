# Meu Pacote de Processamento de Imagens

Este é um pacote simples para demonstração de criação de pacotes Python, focado em operações básicas de imagem.

## Instalação

Use o gerenciador de pacotes pip para instalar o pacote:

```bash
pip install imagens_processamento.py


## Uso
from imagens_processamento.py.main import abrir_imagem, converter_para_tons_de_cinza, salvar_imagem

# Exemplo de uso
img_original = abrir_imagem("caminho/para/sua/imagem.jpg")
if img_original:
    img_cinza = converter_para_tons_de_cinza(img_original)
    salvar_imagem(img_cinza, "caminho/para/sua/imagem_cinza.jpg")

 ## Autor
 # Joao Gabriel O. Carvalho   

# Licença
# MIT