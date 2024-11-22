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
   
---

## Exemplos

### Exemplo 01
- Entrada:
   ```bash
   summary {
       title: "Avanços em Redes Neurais Profundas para Reconhecimento de Imagens"
       text: "Nos últimos anos, as redes neurais profundas (DNNs) têm se destacado como uma das principais abordagens para reconhecimento de imagens em larga escala. Com a introdução de técnicas como o aprendizado por transferência, que utiliza modelos previamente treinados em grandes datasets, o desempenho em tarefas como reconhecimento facial e classificação de objetos melhorou significativamente. Além disso, as melhorias em arquiteturas como as Redes Neurais Convolucionais (CNNs) e a adoção de GPUs para acelerar o treinamento, resultaram em uma revolução no campo. Embora o treinamento de redes profundas ainda seja uma tarefa intensiva em termos de tempo e recursos computacionais, as vantagens em termos de precisão são inegáveis."
       focus: ["redes neurais profundas", "reconhecimento de imagens", "aprendizado por transferência", "CNNs", "GPUs"]
       num_ideas: 4
       personal_comment: "O artigo aborda as melhorias substanciais nas técnicas de reconhecimento de imagens, que têm impacto direto em diversas aplicações como segurança e saúde."
   }

- Saída:
   ```bash
   # Resumo: Avanços em Redes Neurais Profundas para Reconhecimento de Imagens
   
   ## Ideias Principais
   1. Redes neurais profundas (DNNs) como a principal abordagem para reconhecimento de imagens.
   2. Aprendizado por transferência e o uso de modelos previamente treinados.
   3. Melhoria nas arquiteturas, especialmente nas CNNs, para maior precisão.
   4. Uso de GPUs para acelerar o treinamento de redes profundas.
   
   ## Comentário Pessoal
   O artigo aborda as melhorias substanciais nas técnicas de reconhecimento de imagens, que têm impacto direto em diversas aplicações como segurança e saúde.

### Exemplo 02
- Entrada:
   ```bash
   summary {
       title: "Ética e Implicações Sociais da Inteligência Artificial"
       text: "A rápida evolução das tecnologias de inteligência artificial (IA) levantou uma série de questões éticas e sociais que precisam ser discutidas. A automação de processos através de IA pode levar a grandes ganhos de eficiência, mas também coloca em risco empregos em setores como manufatura e transporte. Além disso, a IA tem o potencial de perpetuar preconceitos e discriminação, já que os algoritmos podem refletir vieses presentes nos dados de treinamento. Por outro lado, o uso de IA na medicina, como diagnóstico assistido por máquina e tratamentos personalizados, pode melhorar a qualidade de vida de milhões de pessoas. Portanto, o uso ético da IA é essencial para garantir que seus benefícios sejam distribuídos de forma justa e equitativa."
       focus: ["ética em IA", "automação", "preconceitos", "discriminação", "IA na medicina"]
       num_ideas: 5
       personal_comment: "Este artigo destaca tanto os benefícios quanto os riscos associados à IA, destacando a necessidade de regulamentação para seu uso ético."
   }

- Saída:
   ```bash
   # Resumo: Ética e Implicações Sociais da Inteligência Artificial
   
   ## Ideias Principais
   1. A automação através de IA pode gerar ganhos de eficiência, mas também ameaça empregos.
   2. A IA pode perpetuar preconceitos e discriminação, refletindo vieses dos dados.
   3. Uso de IA na medicina pode melhorar o diagnóstico e tratamentos personalizados.
   4. A necessidade de regulamentação ética para garantir o uso justo da IA.
   5. Benefícios e riscos da IA precisam ser equilibrados de forma justa e equitativa.
   
   ## Comentário Pessoal
   Este artigo destaca tanto os benefícios quanto os riscos associados à IA, destacando a necessidade de regulamentação para seu uso ético.

### Exemplo 03
- Entrada:
   ```bash
   summary {
       title: "O Impacto das Mudanças Climáticas e a Busca por Soluções Sustentáveis"
       text: "O aquecimento global causado pela emissão de gases de efeito estufa tem sido uma das principais ameaças ao meio ambiente nas últimas décadas. As consequências das mudanças climáticas incluem o aumento da frequência de desastres naturais, como enchentes e secas, além do derretimento das calotas polares. Em resposta a essa crise, diversos países têm adotado políticas para reduzir suas emissões de carbono e promover o uso de fontes de energia renováveis, como a solar e a eólica. A transição para uma economia sustentável requer investimentos em novas tecnologias e uma mudança cultural para reduzir o consumo excessivo de recursos naturais. Contudo, a adoção de soluções sustentáveis precisa ser global e cooperativa, uma vez que o impacto das mudanças climáticas não respeita fronteiras nacionais."
       focus: ["mudanças climáticas", "emissões de carbono", "energias renováveis", "economia sustentável", "soluções globais"]
       num_ideas: 6
       personal_comment: "A luta contra as mudanças climáticas exige ações coordenadas entre países e investimentos em novas tecnologias para um futuro sustentável."
   }

- Saída:
   ```bash
   # Resumo: O Impacto das Mudanças Climáticas e a Busca por Soluções Sustentáveis
   
   ## Ideias Principais
   1. O aquecimento global causado pelas emissões de gases de efeito estufa está afetando o meio ambiente.
   2. As mudanças climáticas têm gerado desastres naturais mais frequentes, como enchentes e secas.
   3. Políticas de redução das emissões de carbono estão sendo implementadas em diversos países.
   4. A promoção de fontes de energia renováveis, como solar e eólica, é uma das soluções adotadas.
   5. A transição para uma economia sustentável exige mudanças culturais e tecnológicas.
   6. A colaboração global é essencial para enfrentar as mudanças climáticas de maneira eficaz.
   
   ## Comentário Pessoal
   A luta contra as mudanças climáticas exige ações coordenadas entre países e investimentos em novas tecnologias para um futuro sustentável.
