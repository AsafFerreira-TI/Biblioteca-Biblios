# Biblioteca Biblios

## Descrição
  A Biblioteca Biblios é um app tipo TUI (Terminal User Interface), responsável por gerenciar Livros, Leitores e Reservas de uma biblioteca. 
  Este App foi construído totalmente em Python, usando conceitos de CRUD (Create, Read, Update, Delete), POO (Programação Orientada a Objetos), e que utiliza as bibliotecas [SQLite3](https://sqlite.org/), [SQLAlchemy](https://www.sqlalchemy.org/) e [Tabulate](https://github.com/astanin/python-tabulate) para gerenciar os dados cadastrados.

   Este App foi desenvolvido a fim de auxiliar bibliotecários a ordenar as informações sobre os livros de sua biblioteca, sobre os frequentadores (leitores), além de ser um forte aliado para gerenciar as reservas feitas por leitores. 

  É extremamente útil, simples, de fácil manuseio e de ótima qualidade.

## Como instalar?

 Sobre a instalação, é totalmente simples. Porém, de antemão, estes são os pré-requisitos:
  
 ### Pré-requisitos
 
   1. Ter [Python](https://www.python.org/) (versão 3.13+) instalado em sua máquina local;

   2. Ter [Git](https://git-scm.com/) instalado em sua máquina local;
   
   3. Criar um virtual environment e ativá-lo:

    Para Linux (versões Debian/Ubuntu):

    ``` sudo apt install python3-venv ```
    ``` cd caminho/para/a/pasta/principal ```
    ``` python3 -m venv .venv ```
    ``` source .venv/bin/activate ```
    
    Para Windows:
    ``` python -m venv nome_do_ambiente_virtual ```
    ``` .\nome_do_ambiente_virtual\Scripts\Activate.ps1 ```

   4. Instalar as bibliotecas SQLAlchemy e Tabulate:

    ``` pip install SQLAlchemy ```

    ``` pip install tabulate ```

### Instalação:

Tendo já instalados os pré-requisitos em sua máquina local, basta executar no terminal:

```git clone https://github.com/AsafFerreira-TI/Biblioteca-Biblios.git```
 

Feito isso, você já tem tudo em mãos para executar este programa em sua máquina!

## Instruções de Uso

### Página Inicial:
 Esta é a página inicial do projeto:

```Seja bem-vindo ao Biblios, seu gerenciador de biblioteca!```
``` O que você deseja fazer hoje?```
```1 - Cadastrar;```
```2 - Consultar;```
```3 - Atualizar;```
```4 - Excluir;```
```5 - Sair; ```

 Aqui, você pode escolher o menus. Basta inserir o número do menu que você deseja navegar.

 ### 1 - Cadastrar
 
  No menu "Cadastrar", você pode escolher cadastrar Livros, Leitores ou Reservas. 

  #### Livros: 
    Você deve cadastrar Título, Autor, Ano de Publicação, Editora e Categoria do livro desejado.
  #### Leitores: 
    Você deve cadastrar nome, sobrenome, e-mail, telefone e endereço do leitor.
  #### Reservas: 
    Você deve referenciar o ID do cliente que fez a reserva, o ID do livro que ele escolheu, a data da reserva e o prazo de validade da reserva.
 ### 2 - Consultar
  No Menu "Consultar", você pode consultar dados de Livros, Leitores ou Reservas realizadas.
 ### 3 - Atualizar
  No Menu "Atualizar", você pode escolher atualizar dados de Livros, Leitores ou Reservas. 

    Nota: No menu "Reservas", há um campo chamado "Status", com valor "1", que é criado automaticamente. 
     Quando uma reserva está inativa (em casos de finalização de prazos), é recomendado atualizar seu Status para 0.
 ### 4 - Excluir
  Em "Excluir", você pode excluir dados de Livros, Leitores ou Reservas desejados.
 ### 5 - Sair
  Em "Sair", o programa é desligado automaticamente, encerrando a performance e guardando seus dados.

Em suma, os dados estarão seguros, pois um arquivo .db é criado para armazená-los. 

## Licença


  TERMOS E CONDIÇÕES PARA USO, REPRODUÇÃO E DISTRIBUIÇÃO

1. Definições.

"Licença" significa os termos e condições para uso, reprodução e distribuição conforme definidos nas Seções 1 a 9 deste documento.
"Licenciador" significa o titular dos direitos autorais ou a entidade autorizada pelo titular dos direitos autorais que está concedendo a Licença.
"Entidade Jurídica" significa a união da entidade atuante e todas as outras entidades que a controlam, são controladas por ela ou estão sob controle comum com essa entidade. Para os fins desta definição, "controle" significa (i) o poder, direto ou indireto, de dirigir a gestão ou direção de tal entidade, seja por contrato ou de outra forma, ou (ii) a posse de cinquenta por cento (50%) ou mais das ações em circulação com direito a voto, ou (iii) a titularidade beneficiária de tal entidade.
"Você" (ou "Seu") significa um indivíduo ou Entidade Jurídica que exerce as permissões concedidas por esta Licença.
Forma "Fonte" significa a forma preferida para realizar modificações, incluindo, mas não se limitando a, código-fonte de software, fonte de documentação e arquivos de configuração.
Forma "Objeto" significa qualquer forma resultante da transformação mecânica ou tradução de uma Forma Fonte, incluindo, mas não se limitando a, código objeto compilado, documentação gerada e conversões para outros tipos de mídia.
"Trabalho" significa a obra autoral, seja na Forma Fonte ou na Forma Objeto, disponibilizada sob esta Licença, conforme indicado por um aviso de direitos autorais incluído ou anexado ao trabalho (um exemplo é fornecido no Apêndice abaixo).
"Obras Derivadas" significa qualquer trabalho, seja na Forma Fonte ou na Forma Objeto, baseado (ou derivado) do Trabalho e para o qual as revisões editoriais, anotações, elaborações ou outras modificações representam, como um todo, uma obra autoral original. Para os fins desta Licença, Obras Derivadas não incluem trabalhos que permaneçam separáveis do Trabalho ou que meramente se conectem (ou vinculem pelo nome) às interfaces do Trabalho e de suas Obras Derivadas.
"Contribuição" significa qualquer obra autoral, incluindo a versão original do Trabalho e quaisquer modificações ou adições a esse Trabalho ou a suas Obras Derivadas, que seja intencionalmente submetida ao Licenciador para inclusão no Trabalho pelo titular dos direitos autorais ou por um indivíduo ou Entidade Jurídica autorizada a submeter em nome do titular dos direitos autorais. Para os fins desta definição, "submetida" significa qualquer forma de comunicação eletrônica, verbal ou escrita enviada ao Licenciador ou seus representantes, incluindo, mas não se limitando a, comunicação em listas de discussão eletrônicas, sistemas de controle de versão de código-fonte e sistemas de rastreamento de problemas gerenciados por, ou em nome do Licenciador, com o propósito de discutir e melhorar o Trabalho, mas excluindo comunicação expressamente marcada ou designada por escrito pelo titular dos direitos autorais como "Não é uma Contribuição".
"Contribuidor" significa o Licenciador e qualquer indivíduo ou Entidade Jurídica em nome de quem uma Contribuição foi recebida pelo Licenciador e posteriormente incorporada ao Trabalho.

2. Concessão de Licença de Direitos Autorais.
Sujeito aos termos e condições desta Licença, cada Contribuidor concede a Você, por meio desta, uma licença de direitos autorais perpétua, mundial, não exclusiva, sem cobrança de royalties, irrevogável para reproduzir, preparar Obras Derivadas de, exibir publicamente, executar publicamente, sublicenciar e distribuir o Trabalho e tais Obras Derivadas na Forma Fonte ou na Forma Objeto.
3. Concessão de Licença de Patente.
Sujeito aos termos e condições desta Licença, cada Contribuidor concede a Você, por meio desta, uma licença de patente perpétua, mundial, não exclusiva, sem cobrança de royalties, irrevogável (exceto conforme disposto nesta seção) para fabricar, ter fabricado, usar, oferecer para venda, vender, importar e transferir de outra forma o Trabalho, sendo que tal licença se aplica apenas às reivindicações de patente licenciáveis por tal Contribuidor que sejam necessariamente infringidas por sua(s) Contribuição(ões) isoladamente ou pela combinação de sua(s) Contribuição(ões) com o Trabalho ao qual tal(is) Contribuição(ões) foi(ram) submetida(s). Se Você iniciar litígio de patente contra qualquer entidade (incluindo uma reconvenção ou contrademanda em uma ação judicial) alegando que o Trabalho ou uma Contribuição incorporada ao Trabalho constitui violação direta ou contributiva de patente, então qualquer licença de patente concedida a Você sob esta Licença para esse Trabalho será encerrada na data em que tal litígio for ajuizado.
4. Redistribuição.
Você pode reproduzir e distribuir cópias do Trabalho ou de Obras Derivadas dele em qualquer meio, com ou sem modificações, e na Forma Fonte ou na Forma Objeto, desde que Você cumpra as seguintes condições:
(a) Você deve fornecer a quaisquer outros destinatários do Trabalho ou das Obras Derivadas uma cópia desta Licença; e
(b) Você deve fazer com que quaisquer arquivos modificados contenham avisos proeminentes indicando que Você alterou os arquivos; e
(c) Você deve manter, na Forma Fonte de quaisquer Obras Derivadas que Você distribua, todos os avisos de direitos autorais, patentes, marcas registradas e atribuição da Forma Fonte do Trabalho, excluindo aqueles avisos que não se aplicam a nenhuma parte das Obras Derivadas; e
(d) Se o Trabalho incluir um arquivo de texto "NOTICE" como parte de sua distribuição, então quaisquer Obras Derivadas que Você distribua devem incluir uma cópia legível dos avisos de atribuição contidos nesse arquivo NOTICE, excluindo aqueles que não se aplicam a nenhuma parte das Obras Derivadas, em pelo menos um dos seguintes locais: dentro de um arquivo de texto NOTICE distribuído como parte das Obras Derivadas; dentro da Forma Fonte ou da documentação, se fornecida junto com as Obras Derivadas; ou, dentro de uma exibição gerada pelas Obras Derivadas, se e onde tais avisos de terceiros normalmente aparecem. O conteúdo do arquivo NOTICE é apenas para fins informativos e não modifica a Licença. Você pode adicionar seus próprios avisos de atribuição dentro das Obras Derivadas que distribui, ao lado ou como um adendo ao texto NOTICE do Trabalho, desde que tais avisos adicionais de atribuição não possam ser interpretados como modificadores da Licença.
Você pode adicionar sua própria declaração de direitos autorais às suas modificações e pode fornecer termos e condições de licença adicionais ou diferentes para uso, reprodução ou distribuição de suas modificações, ou para qualquer Obra Derivada como um todo, desde que seu uso, reprodução e distribuição do Trabalho, de outra forma, cumpra as condições estabelecidas nesta Licença.
5. Submissão de Contribuições.
A menos que Você declare explicitamente o contrário, qualquer Contribuição intencionalmente submetida para inclusão no Trabalho por Você ao Licenciador será considerada sob os termos e condições desta Licença, sem quaisquer termos ou condições adicionais. Não obstante o acima exposto, nada aqui substituirá ou modificará os termos de qualquer acordo de licença separado que Você possa ter celebrado com o Licenciador em relação a tais Contribuições.
6. Marcas Registradas.
Esta Licença não concede permissão para usar os nomes comerciais, marcas registradas, marcas de serviço ou nomes de produtos do Licenciador, exceto conforme necessário para uso razoável e habitual ao descrever a origem do Trabalho e reproduzir o conteúdo do arquivo NOTICE.
7. Isenção de Garantia.
A menos que exigido por lei aplicável ou acordado por escrito, o Licenciador fornece o Trabalho (e cada Contribuidor fornece suas Contribuições) "NO ESTADO EM QUE SE ENCONTRA" ("AS IS"), SEM GARANTIAS OU CONDIÇÕES DE QUALQUER TIPO, expressas ou implícitas, incluindo, sem limitação, quaisquer garantias ou condições de TITULARIDADE, NÃO VIOLAÇÃO, COMERCIABILIDADE ou ADEQUAÇÃO A UM DETERMINADO FIM. Você é o único responsável por determinar a adequação de usar ou redistribuir o Trabalho e assume quaisquer riscos associados ao exercício das permissões sob esta Licença.
8. Limitação de Responsabilidade.
Em nenhuma circunstância e sob nenhuma teoria jurídica, seja por ato ilícito (incluindo negligência), contrato ou de outra forma, a menos que exigido por lei aplicável (tais como atos dolosos e gravemente negligentes) ou acordado por escrito, qualquer Contribuidor será responsável perante Você por danos, incluindo quaisquer danos diretos, indiretos, especiais, incidentais ou consequentes de qualquer natureza decorrentes desta Licença ou do uso ou incapacidade de usar o Trabalho (incluindo, mas não se limitando a, danos por perda de boa vontade, interrupção de trabalho, falha ou mau funcionamento de computador, ou quaisquer outros danos ou perdas comerciais), mesmo que tal Contribuidor tenha sido avisado da possibilidade de tais danos.
9. Aceitação de Garantia ou Responsabilidade Adicional.
Ao redistribuir o Trabalho ou Obras Derivadas dele, Você pode optar por oferecer, e cobrar por, aceitação de suporte, garantia, indenização ou outras obrigações e/ou direitos de responsabilidade consistentes com esta Licença. No entanto, ao aceitar tais obrigações, Você pode agir apenas em seu próprio nome e sob sua exclusiva responsabilidade, não em nome de qualquer outro Contribuidor, e somente se Você concordar em indenizar, defender e isentar cada Contribuidor de qualquer responsabilidade incorrida por, ou reivindicações apresentadas contra, tal Contribuidor em razão de você aceitar qualquer garantia ou responsabilidade adicional.
FIM DOS TERMOS E CONDIÇÕES

Copyright 2026 Asaf Ferreira

Licenciado sob a Licença Apache, Versão 2.0 (a "Licença");
você não pode usar este arquivo exceto em conformidade com a Licença.
Você pode obter uma cópia da Licença em
http://www.apache.org/licenses/LICENSE-2.0

A menos que exigido por lei aplicável ou acordado por escrito, o software distribuído sob a Licença é distribuído "NO ESTADO EM QUE SE ENCONTRA",
SEM GARANTIAS OU CONDIÇÕES DE QUALQUER TIPO, expressas ou implícitas.

### Soli Deo Gloria!