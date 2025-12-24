# Password Verifier

Aplicação para verificação de força de senha, útil para aplicações que possuem a funcionalidade de geração de novas senhas para o usuário.

## Sobre o projeto

Este projeto foi desenvolvido como prática de desenvolvimento orientada para soluções de segurança da informação.

## Objetivo

Desenvolver um verificador de senhas informadas pelo usuário, onde duas saídas são esperadas:

- Senha OK: A senha atende aos requisitos informados ao usuário.
- Senha fraca: A senha não atende aos requisitos informados ao usuário.

## Tecnologias utilizadas:

### Backend
- Python 3.11: linguagem de programação

### Frontend
- ttkbootstrap: framework para gerenciamento e estilização de componentes UI.

### Ferramentas
- Pyinstaller: empacotador de módulos python e suas dependências em um arquivo executável.

## Monitoração
Como forma de se obter maior controle sobre as execuções da aplicação, uma pasta de *logs* é criada na primeira execução, passando a guardar arquivos texto com informações sobre cada execução ocorrida.