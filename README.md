# Dynamic Airflow DAG Generator

Este projeto consiste em um script Python que automatiza a criação de DAGs para o Apache Airflow, baseado em configurações definidas em um arquivo JSON. Ele é ideal para ambientes que necessitam de múltiplos workflows dinâmicos e configuráveis.

## Pré-requisitos

Para executar este projeto, você precisará ter:

- Python 3.6 ou superior
- Apache Airflow 2.x

## Configuração do Ambiente

Certifique-se de que o Apache Airflow esteja corretamente instalado em seu ambiente. Se precisar de ajuda para configurar o Airflow, consulte a [documentação oficial do Airflow](https://airflow.apache.org/docs/).

## Instalação

Para usar este script no seu projeto Airflow, siga os passos abaixo:

1. Clone este repositório em seu ambiente local ou servidor onde o Airflow está instalado:
   ```bash
   git clone https://github.com/szottt/airflow-dynamic.git
   cd seu-projeto
    ```

Certifique-se de que o arquivo dynamic.json, que contém as configurações dos DAGs, está na pasta correta e configurado conforme sua necessidade.

## Uso

O script lê o arquivo de configuração dynamic.json, que deve estar formatado da seguinte maneira:

```json
{
    "Hello-Igor-01": [
        "Hello-Igor-01",
        "0 11 * * *",
        "Dev"
    ],
    "Test-Dag-03": [
        "Test-Dag-03",
        "0 9 * * *",
        "HLG"
    ]
}
```

Cada chave corresponde ao ID de um DAG, o primeiro valor é o nome da DAG o segundo é o schedule do processo e o terceiro São as Tags do projeto.

Após configurar seu arquivo dynamic.json, basta ir para o ariflow que a DAGs sera atualizada.

Contribuindo
Se deseja contribuir para este projeto, por favor, siga estas etapas:

Faça um Fork do repositório.
Crie uma Branch para sua feature (git checkout -b feature/AmazingFeature).
Faça o Commit das suas mudanças (git commit -m 'Add some AmazingFeature').
Faça o Push para a Branch (git push origin feature/AmazingFeature).
Abra um Pull Request.
Licença
Distribuído sob a licença MIT. Veja LICENSE para mais informações.

Contato
<div style="display: inline_block">
  <a href="https://www.linkedin.com/in/igorszot/"><img width="48" height="48" src="https://img.icons8.com/color/48/linkedin.png" alt="linkedin"/></a>
</div>