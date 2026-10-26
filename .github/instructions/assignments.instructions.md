---
description: "Instruções para usar sempre que criar ou editar arquivos markdown de assignment, garantindo consistência e clareza para os alunos."
applyTo: "assignments/**/*.md"
---

# Diretrizes de Estrutura para Markdowns de Tarefas

Todos os arquivos Markdown de tarefas devem seguir a estrutura definida em [`templates/assignment-template.md`](../../templates/assignment-template.md):

- O arquivo da tarefa deve se chamar `README.md`.
- Preserve a ordem, os níveis e o texto dos cabeçalhos do template, incluindo emojis. Não traduza nem substitua os cabeçalhos.
- Preencha todos os placeholders; não deixe instruções entre colchetes no resultado final.
- Mantenha as duas tarefas previstas no template. Dê a cada uma um título específico e orientado à ação.
- Escreva o objetivo em 1 ou 2 frases, resumindo o que o aluno aprenderá ou construirá.
- Em `Descrição`, explique claramente o que o aluno deve fazer.
- Em `Requisitos`, mantenha a frase `O programa concluído deve:` e liste os resultados esperados em tópicos específicos e verificáveis.
- Inclua exemplos de entrada e saída em blocos de código quando ajudarem a esclarecer os requisitos.
- Não acrescente seções fora da estrutura do template, a menos que isso seja solicitado explicitamente.

Os cabeçalhos e subtítulos obrigatórios são:

```markdown
# 📘 Atividade: [Título da Atividade]

## 🎯 Objetivo

## 📝 Tarefas

### 🛠️ [Título da Tarefa 1]

#### Descrição

#### Requisitos
O programa concluído deve:

### 🛠️ [Título da Tarefa 2]

#### Descrição

#### Requisitos
O programa concluído deve:
```