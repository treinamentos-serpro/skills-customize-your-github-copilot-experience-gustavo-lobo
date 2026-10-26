
# 📘 Atividade: Jogos em Python

## 🎯 Objetivo

Pratique manipulação de strings, loops, condicionais e entrada de dados em Python ao criar um jogo da Forca. Você também usará seleção aleatória para escolher a palavra que o jogador deverá adivinhar.

## 📝 Tarefas

### 🛠️ Preparar a palavra e o estado do jogo

#### Descrição
Use a lista de palavras fornecida no código inicial para escolher a palavra secreta e preparar as variáveis que acompanharão o progresso da partida.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista `words`.
- Inicializar uma coleção para registrar as letras já adivinhadas.
- Definir o limite de palpites incorretos e inicializar o contador de erros.
- Exibir o progresso da palavra, mostrando `_` para cada letra ainda não adivinhada e as letras corretas em suas posições.

### 🛠️ Implementar a rodada de palpites

#### Descrição
Implemente o loop principal para que o jogador informe letras, acompanhe o progresso e receba o resultado ao vencer ou esgotar as tentativas.

#### Requisitos
O programa concluído deve:

- Solicitar um palpite de letra enquanto a palavra não tiver sido adivinhada e ainda houver tentativas incorretas.
- Atualizar as letras adivinhadas e exibir o progresso após cada palpite.
- Reduzir as tentativas restantes quando o palpite não estiver na palavra.
- Encerrar a partida quando todas as letras forem adivinhadas ou o limite de erros for atingido.
- Exibir uma mensagem de vitória ou derrota; em caso de derrota, revelar a palavra secreta.