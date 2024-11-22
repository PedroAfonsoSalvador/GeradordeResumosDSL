# Gerador de Resumos - DSL

## Equipe
- **Pedro Afonso Cavalcanti Salvador**  

---

## Motivação
O estudo de textos densos e longos, como artigos acadêmicos ou capítulos de livros, é uma tarefa que exige muito tempo e esforço. Este projeto foi criado para facilitar o dia a dia de estudantes e profissionais, oferecendo uma **linguagem de domínio específico (DSL)** que permite automatizar o processo de criação de resumos.  
A ferramenta analisa textos, identifica ideias principais e organiza os conteúdos de forma estruturada e clara, permitindo que os usuários foquem no que realmente importa.

---

## Descrição Informal da Linguagem
A DSL é projetada para ser simples e expressiva. O usuário escreve especificações de resumos em um formato intuitivo, detalhando:
- O título do texto a ser resumido.
- O conteúdo textual.
- Focos específicos (palavras-chave importantes para priorizar no resumo).
- O número de ideias principais desejadas.
- Comentários pessoais para complementar o resumo.

---

## Passo a Passo para Executar o Programa

### Pré-requisitos
1. **Python 3.7 ou superior:** Certifique-se de ter o Python instalado no seu computador. Caso não tenha, baixe em [python.org](https://www.python.org/).  
2. **ANTLR 4:** Instale o ANTLR 4 seguindo as instruções no site oficial ([antlr.org](https://www.antlr.org/)).  

### Etapas
1. Clone o repositório para sua máquina local:
   ```bash
   git clone https://github.com/seu-usuario/resumo-dsl.git
   cd resumo-dsl
2. Gere os arquivos do analisador com o ANTLR:
   ```bash
   antlr4 Summary.g4 -Dlanguage=Python3 -visitor
   Este comando criará os arquivos SummaryLexer.py, SummaryParser.py e SummaryVisitor.py no diretório.

4. Crie o arquivo de entrada:
Crie um arquivo de texto, como input.summary, com o conteúdo no formato da DSL.
Exemplo:
   ```bash
   summary {
       title: "Introdução às Redes Neurais"
       text: "Redes neurais artificiais simulam o funcionamento do cérebro humano. Elas são compostas por neurônios artificiais interligados. São amplamente utilizadas em classificação de imagens, reconhecimento de fala e tradução de idiomas. Um exemplo é o uso em visão computacional, como reconhecimento facial."
       focus: ["redes", "aplicações"]
       num_ideas: 3
       personal_comment: "O texto aborda conceitos importantes e aplicações práticas."
   }

6. Execute o compilador:
   ```bash
   python main.py input.summary
