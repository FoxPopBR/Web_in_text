# Conversor Texto do HTML para Texto formatado Markdown

Este script Python permite converter conteúdo de texto no código HTML de um web site em texto formatado Markdown. 
Utilizando uma interface gráfica simples baseada em Tkinter, os usuários podem inserir a URL desejada, e o script se encarrega de extrair o texto HTML, converter para Markdown e exibir o resultado. 
Além disso, o Markdown gerado é salvo em um arquivo local para uso posterior.

## Características Principais

- **Extração de Conteúdo HTML**: Acessa o conteúdo HTML de páginas web utilizando a URL fornecida.
- **Conversão para Markdown**: Utiliza a biblioteca `html2text` para converter o HTML em Markdown, ignorando elementos como imagens e links para simplificar o texto.
- **Interface Gráfica**: Permite a fácil inserção de URLs e visualização do Markdown convertido.
- **Salvar Resultados**: O texto em Markdown é salvo automaticamente em um arquivo `.md`.

## Como Usar

1. Inicie o script.
2. No campo de entrada, digite a URL da página da qual deseja extrair o texto.
3. Clique em "Carregar e Converter" para iniciar o processo.
4. O texto convertido será exibido na interface e salvo em um arquivo chamado `saida.md` no diretório do script.

## Requisitos

- Python 3.x
- Tkinter
- `html2text`: Pode ser instalado via pip com `pip install html2text`.
- `tkhtmlview`: Para exibir conteúdo HTML/Markdown na interface gráfica. Instale via pip com `pip install tkhtmlview`.

## Funções

### `carregar_pagina_e_converter_para_markdown()`

Essa função carrega o conteúdo HTML da URL fornecida, converte para Markdown e atualiza a interface gráfica com o resultado. Em caso de erro na carga da página, um aviso é exibido.

### `converter_html_para_markdown(html)`

Recebe uma string HTML como entrada e retorna uma string formatada em Markdown, utilizando a configuração para ignorar imagens e links.

### `salvar_markdown_em_arquivo(markdown_content)`

Salva o conteúdo Markdown gerado em um arquivo `saida.md`, permitindo o acesso ao texto convertido fora da aplicação.

---

Criado com ❤ por [FoxPopBR].
