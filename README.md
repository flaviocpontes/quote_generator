# Quote Generator

Este é um gerador de fluxo de "cotações" para uso no desafio de contratação da Toro.

## Como usar

O projeto foi feito para criar uma imagem de Docker para uso no desafio.

Para rodar basta usar o `docker build .` e criar um container local.

Preferencialmente se deve usar o container hospedado no Docker Hub com o comando `docker run -p 8080:8080 toroinvestimentos/quotesmock`

O fluxo de cotações será acessado no path `/quotes`