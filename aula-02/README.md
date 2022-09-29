# Tarefas da Aula 2

Para fazer as tarefas de hoje, você vai precisar de um computador
com acesso à internet e uma conta no GitHub para acessar o Codespace.

Pra começar, acesse o nosso codespace e crie uma conta no GitHub caso ainda não tenha:

https://code.cs50.io/

Siga as instruções na tela e aguarde até o seu codespace estar configurado.

Você vai precisar fazer pelo menos uma tarefa entre:
- [Caixa eletrônico](#caixa-eletronico) se você estiver se sentindo menos confortável
- [CPF](#cpf) se você estiver se sentindo mais confortável


## Caixa eletronico

Nessa tarefa você precisa desenvolver o código que vai rodar dentro de um caixa eletrônico.

Quando um cliente sacar dinheiro, você precisa garantir que o caixa eletrônico emita o menor número possível de notas de 10, 5, 2 e 1 reais.

"Como eu vou garantir que o número de notas é o mínimo possível?" 
Ótima pergunta! Em ciência da computação, problemas como esse são super comuns. Tão comuns, que os algoritmos usados pra solucionar problemas como esse receberam um nome: "Gananciosos", ou "Greedy".

No caso do nosso problema, podemos imaginar que para encontrar o número mínimo de notas nós teremos que ser "gananciosos", e começar contando da maior denominação disponível pra a gente. Por exemplo, se um clinte pede 28 reais, nós começamos contando pelas notas de 10. Dessa forma, com duas notas de 10, nos cobrimos 20 dos 28 reais, e temos só 7 restantes. Como 8 é menor que 10, seguimos para o denominador seguinte, 5. Contando uma nota de 5, ficamos com 3. Fazemos o mesmo com 2 e depois com 1, para um total de duas notas de 10, uma de 5, uma de 2 e uma de 1: totalizando 5 notas.

### Implementação
Nós [já implementamos](https://github.com/Maronato/maroaulas/blob/main/aula-02/caixa_eletronico.py). a maior parte do problema por você, mas ainda restam algumas funções!

Quando você abrir o problema, verá que temos uma função `main` pronta que chama algumas outras funções. Leia e entenda o funcionamento da `main` e implemente as seguintes funções:
- Implemente `perguntar_reais` de forma que ela pergunte quantos reais o usuário deseja sacar usando `get_int`. Se o usuário te passar um número negativo, seu código deve refazer a pergunta.
- Implemente `calcula_10` de forma que ela retorne o número de notas de 10 que seu caixa eletrônico devolveria ao usuário. Por exemplo, se o valor de `total` for 20, sua função deve retornar 2. Se `total` for 25, sua função também deve retornar 2. Se `total` for 5, sua função deve retornar 0, etc.
- Implemente `calcula_5` da mesma forma, mas para notas de 5.
- Implemente `calcula_2` da mesma forma, mas para notas de 2.
- Implemente `calcula_1` da mesma forma, mas para notas de 1.

### Rodando e testando
Seu programa deve se comportar como o exemplo abaixo:

```bash
$ python caixa_eletronico.py
Quantos reais você quer? 42
Você vai receber 5 notas
```

```bash
$ python caixa_eletronico.py
Quantos reais você quer? -42
Quantos reais você quer? peixe
Quantos reais você quer? 35
Você vai receber 4 notas
```

## CPF

Nessa tarefa você deve implementar um validador de CPF.

> O Cadastro de Pessoa Física (abreviado CPF ou CPF-MF, substituto do Cartão de Identificação do Contribuinte abreviado CIC) é o registro de contribuintes mantido pela Receita Federal do Brasil no qual podem se inscrever, uma única vez, quaisquer pessoas naturais, independentemente de idade ou nacionalidade, inclusive falecidas. Cada inscrito é unicamente identificado por um número de inscrição no CPF composto por 11 dígitos decimais, pessoal e intransferível durante toda a vida, jamais muda senão por decisão judicial.

CPFs são importantes e, por isso, é essencial que não o erremos quando precisarmos compartilha-lo. Falar é fácil, então as pessoas que inventaram o CPF também pensaram em uma forma de prevenir erros de digitação: dois dígitos verificadores no final dele.

Você deve lembrar que CPFs normalmente têm o formato `798.020.920-61`. Acontece que os dois últimos digitos são especiais. Eles têm a função de garantir que todos os digitos anteriores foram digitados corretamente. Esse "número de checagem" (ou "checksum") é algo bem comum em computação, pois nem sempre nós podemos garantir que nossos dados não foram corrompidos ou alterados.

No caso do CPF, esses dois últimos digitos são gerados por um algoritmo que olha todos os números anteriores e calcula um valor com base neles.

Por causa disso, para garantir que um CPF foi digitado corretamente, basta refazer o calculo dos dois últimos digitos e comparar com o valor do CPF. Se eles forem iguais, o CPF é valido!

### Cálculo

Pra checar se o CPF é válido, precisamos fazer dois cálculos: Um pro penúltimo digito e outro pro último. Os dois calculos seguem a mesma lógica, mas são checados independentemente.

Para detalhes de como o algoritmo funciona, veja esse [link](https://ogeradordecpf.com.br/algoritmo/)


### Implementação
Você deve implementar todo o código do seu verificador de CPF. Seu programa deve pedir pro usuário digitar um CPF usando apenas números, e retornar "Válido" ou "Inválido".

Exemplos:
```bash
$ python cpf.py
Qual é o seu CPF? 79802092061
Válido
```
```bash
$ python cpf.py
Qual é o seu CPF? 79802092062
Inválido
```
```bash
$ python cpf.py
Qual é o seu CPF? 123
Inválido
```
