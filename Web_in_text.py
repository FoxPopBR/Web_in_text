 # Converter o conteúdo de Texto presente no HTML para Texto formato Markdown
import tkinter as tk
from tkinter import ttk
from tkhtmlview import HTMLLabel
import urllib.request
import html2text

def carregar_pagina_e_converter_para_markdown():
    url = url_entry.get()
    try:
        # Carregar conteúdo HTML da página
        resposta = urllib.request.urlopen(url)
        html = resposta.read().decode('utf-8', errors='ignore')

        # Converter HTML para Markdown
        markdown_content = converter_html_para_markdown(html)

        # Exibir o Markdown na interface
        texto_pagina.set_html(markdown_content)

        # Salvar o Markdown em um arquivo
        salvar_markdown_em_arquivo(markdown_content)
    except Exception as e:
        texto_pagina.set_html(f"Erro ao carregar a página: {e}")

def converter_html_para_markdown(html):
    # Criar um objeto html2text e configurá-lo, se necessário
    h = html2text.HTML2Text()
    # Ignorar imagens e links embutidos, por exemplo (ajuste conforme necessário)
    h.ignore_links = True
    h.ignore_images = True

    # Converter o HTML para Markdown
    markdown_content = h.handle(html)

    return markdown_content

def salvar_markdown_em_arquivo(markdown_content):
    # Salvar o Markdown em um arquivo .md
    nome_arquivo_md = "saida.md"
    with open(nome_arquivo_md, 'w', encoding='utf-8') as arquivo_md:
        arquivo_md.write(markdown_content)

    print(f'Texto convertido para Markdown e salvo em "{nome_arquivo_md}" com sucesso!')

# Criar a janela principal
root = tk.Tk()
root.title("Navegador Simples")

# Criar entrada para URL
url_entry = ttk.Entry(root, width=50)
url_entry.pack(fill=tk.X, padx=10, pady=5)

# Botão para carregar a página e converter para Markdown
botao_carregar = ttk.Button(root, text="Carregar e Converter", command=carregar_pagina_e_converter_para_markdown)
botao_carregar.pack(pady=5)

# Área de texto para exibir a página (agora exibe Markdown)
texto_pagina = HTMLLabel(root, html="<h1>Insira uma URL para começar</h1>")
texto_pagina.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Executar o loop principal da janela
root.mainloop()
