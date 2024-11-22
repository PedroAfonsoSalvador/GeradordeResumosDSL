import sys
from antlr4 import *
from SummaryLexer import SummaryLexer
from SummaryParser import SummaryParser
from SummaryVisitor import SummaryVisitor
from collections import Counter
import spacy

class SummaryInterpreter(SummaryVisitor):
    """
    Classe visitante para interpretar os dados do resumo
    e gerar a saída no formato de resumo.
    """

    def __init__(self):
        # Inicializa o armazenamento de dados e o modelo NLP do spacy
        self.data = {}
        self.nlp = spacy.load("pt_core_news_sm")  # Usando modelo em português do spacy

    def visitTitle(self, ctx):
        """Processa o campo 'title' (título) do resumo."""
        self.data['title'] = ctx.STRING().getText().strip('"')

    def visitText(self, ctx):
        """Processa o campo 'text' (texto) do resumo."""
        self.data['text'] = ctx.STRING().getText().strip('"')

    def visitFocus(self, ctx):
        """Processa o campo 'focus' (foco) do resumo."""
        focus_list = [f.strip('"') for f in ctx.STRING_LIST().getText().split(',')]
        self.data['focus'] = focus_list

    def visitNum_ideas(self, ctx):
        """Processa o campo 'num_ideas' (número de ideias) do resumo."""
        self.data['num_ideas'] = int(ctx.INT().getText())

    def visitComment(self, ctx):
        """Processa o campo 'personal_comment' (comentário pessoal) do resumo."""
        self.data['comment'] = ctx.STRING().getText().strip('"')

    def extract_key_points(self):
        """
        Extrai os pontos chave do campo 'text' usando técnicas de NLP.
        Filtra pelas palavras do campo 'focus' se fornecidas e limita o
        número de ideias conforme especificado em 'num_ideas'.
        """
        text = self.data.get("text", "")
        focus = self.data.get("focus", [])
        num_ideas = self.data.get("num_ideas", 3)

        doc = self.nlp(text)
        words = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]
        
        if focus:
            words = [word for word in words if any(f in word for f in focus)]
        
        return Counter(words).most_common(num_ideas)

    def generate_summary(self):
        """
        Gera um resumo formatado em markdown com os pontos chave
        e o comentário pessoal, caso presente.
        """
        key_points = self.extract_key_points()
        
        # Constrói o cabeçalho do resumo
        summary = f"# Resumo: {self.data.get('title', 'Sem título')}\n\n"
        
        # Adiciona as ideias principais
        summary += "## Ideias Principais\n"
        summary += "\n".join(f"{i+1}. {point[0].capitalize()}" for i, point in enumerate(key_points)) + "\n\n"

        # Adiciona o comentário pessoal, se presente
        if "comment" in self.data:
            summary += "## Comentário Pessoal\n"
            summary += f"{self.data['comment']}\n"
        
        return summary

def main(input_file):
    """
    Função principal para processar o arquivo de entrada e gerar o resumo.
    """
    # Abre e analisa o arquivo de entrada
    input_stream = FileStream(input_file)
    lexer = SummaryLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SummaryParser(stream)
    tree = parser.summary()

    # Interpreta os dados analisados e gera o resumo
    interpreter = SummaryInterpreter()
    interpreter.visit(tree)
    print(interpreter.generate_summary())

if __name__ == "__main__":
    # Verifica o uso correto e chama a função principal
    if len(sys.argv) != 2:
        print("Uso: python main.py <arquivo_de_entrada>")
        sys.exit(1)

    main(sys.argv[1])
