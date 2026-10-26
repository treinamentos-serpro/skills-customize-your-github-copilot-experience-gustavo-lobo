# 📘 Atividade: Testes Automatizados com unittest

## 🎯 Objetivo

Aprenda a criar e executar testes automatizados para funções Python usando o módulo `unittest`, que faz parte da biblioteca padrão. Você também praticará como usar falhas de teste para encontrar e corrigir um erro no código.

## 📝 Tarefas

### 🛠️ Escrever testes para funções simples

#### Descrição
Complete os testes iniciais no arquivo `starter-code.py` para verificar as funções de soma e de identificação de números pares. Use os exemplos fornecidos como ponto de partida e acrescente casos que ajudem a verificar diferentes entradas.

#### Requisitos
O programa concluído deve:

- Usar classes derivadas de `unittest.TestCase` para agrupar os testes.
- Ter métodos de teste cujos nomes comecem com `test_`.
- Verificar `add_numbers()` com números positivos, zero e números negativos.
- Verificar `is_even()` com pelo menos um número par e um número ímpar.
- Executar os testes com `python starter-code.py` e apresentar o resultado no terminal.

### 🛠️ Encontrar e corrigir uma falha com testes

#### Descrição
Escreva testes para `apply_discount()` usando o comportamento esperado descrito abaixo. Execute todos os testes, use o resultado para localizar o defeito intencional na função e corrija sua implementação.

#### Requisitos
O programa concluído deve:

- Verificar que `apply_discount(200, 10)` retorna `180`.
- Verificar que `apply_discount(100, 0)` retorna `100`.
- Fazer os testes falharem antes da correção da função e passarem depois dela.
- Executar novamente toda a suíte com `python starter-code.py` e confirmar que todos os testes passam.
