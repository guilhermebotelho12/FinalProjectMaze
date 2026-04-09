# Simulador de Aprendizagem de Rotas em Labirintos

## Descrição
Este projeto consiste num simulador de aprendizagem de rotas em labirintos, onde utilizando determinados algoritmos pré-criados pelos desenvolvedores da aplicação o usuário irá conseguir procurar o caminho desde a casa inicial até às casas finais caso essa ou essas existam.
O projeto tem como propósito ver como diversos algoritmos utilizam as suas próprias maneiras para procurar os caminhos existentes no labirinto criado também pelo utilizador.

## Instalação
Necessita somente de realizar o download da pasta do simulador e abrir o executável.

### Requisitos do sistema
- Sistema Operativo: Windows, macOS, Linux

### Passos para a instalação
**1ºPasso** – Realizar o download da pasta que se encontra no link: 
https://alumniual-my.sharepoint.com/:f:/g/personal/30008890_students_ual_pt/EijOSUgs9AFOmqEFBEE5510Bx64ANdybxphDFLqWi35yTQ?e=LEkNtI

**2ºPasso** – Descompactar o zip para uma localização à sua escolha

**3ºPasso** – Abrir a pasta descompactada e clicar duas vezes no ficheiro “Simulador de Rotas em Labirintos.exe” para correr a aplicação.


Nota: Sempre que aparecer um aviso de segurança por parte do Windows clicar sempre em permitir. 

## Uso
Para o utilizador conseguir visualizar e realizar todos os propósitos pretendidos por este projeto, a aplicação contém várias funcionalidades. As funcionalidades mais importantes são as que foram chamadas de gerais e estas são: Inserir linhas e colunas, Criar, Resolver, Apagar e Salvar. 

**Insert Rows and columns-** Esta funcionalidade permite que o utilizador insira o número que pretende de linhas e colunas para posteriormente a funcionalidade criar, utilize estes valores numéricos passados pelo utilizador para realizar a sua função. Estes valores são passados de forma interativa, ou seja, o utilizador tem dois elementos visuais no ecrã devidamente etiquetados onde este sabe qual valor é para colocar em cada um.

**Create-** Esta permite que o utilizador crie um labirinto no ecrã da aplicação, com os valores passados pela funcionalidade “Inserir linhas e colunas”. Esta funcionalidade verifica também esses valores inseridos, pois consoante o tamanho do utilizador o valor máximo permitido de linhas e colunas pode variar.

**Solve-** O utilizador tem também acesso à funcionalidade “Resolver” que permite que o mesmo, como o próprio nome indica, resolva o labirinto que criou anteriormente. O meio de resolução do labirinto altera consoante o tamanho do mesmo.

**Clear-** O utilizador pode também decidir apagar o labirinto que criou a qualquer momento incluindo enquanto um algoritmo se encontra a resolver o mesmo.

**Save-** Para uma futura análise ou meramente por o utilizador quiser guardar, o mesmo tem então à sua disposição a funcionalidade “Guardar”.

Existem ainda outras funcionalidades, nomeadamente funcionalidades visuais e algorítmicas. As funcionalidades visuais têm como objetivo permitir que o utilizador personalize a aplicação ao seu gosto, e consistem em duas funcionalidades específicas.

**Pick color walls-** Esta funcionalidade permite, através de uma janela secundária que se abre ao clicar no botão com o texto "Pick color" ao lado do texto "Walls color:", escolher a cor desejada para as paredes do labirinto.

**Pick color backgorund-** Esta funcionalidade, à semelhança da anterior, permite que o utilizador selecione uma cor, mas desta vez para o fundo do labirinto em vez de para as paredes.

Por último, existem as funcionalidades algorítmicas, que são as que permitem ao utilizador escolher qual o algoritmo com que pretendem resolver o labirinto que acabaram de criar.

**Flood Fill-** Esta funcionalidade é precisamente o algoritmo de procura Flood Fill. Este algoritmo resolve o labirinto explorando em profundidade, utilizando backtracking para percorrer todas as casas (células) existentes. No final, encontra o melhor caminho possível, caso exista, com base no custo de cada célula.

**Breadth-** Este explora todo o labirinto em largura até encontrar a(s) casa(s) final(is), caso existam. Devido a esta exploração em largura, garante sempre que encontra o menor caminho possível entre a casa inicial e a casa final, se existir uma casa final.

**Depth-** Esta funcionalidade permite que o utilizador explore todo o labirinto em profundidade até encontrar a(s) casa(s) final(is). Utiliza backtracking nos casos em que encontra um beco sem saída, retrocedendo para a última interseção disponível até encontrar uma que ainda tenha vizinhos não visitados.

**A\* Search-** Esta funcionalidade utiliza precisamente o algoritmo “A* Search” para explorar todo o labirinto de forma a encontrar o caminho mais curto entre a casa inicial e a(s) casa(s) final(is), caso existam. Para isto este utiliza uma função heurística para avaliar o custo total do caminho.

## Exemplo de utilização
1.	Iniciar a aplicação seguindo os passos descritos na instalação.
2.	Inserir o número desejado de colunas e linhas.
3.	Escolher as cores para as paredes e fundo do labirinto clicando em ambos os botões "Escolher cor", um de cada vez.
4.	Clicar no botão "Criar" para gerar um labirinto com o número de colunas e linhas especificado anteriormente.
5.	Clicar no botão "Resolver" para encontrar a solução para o labirinto.
6.	Clicar no botão "Guardar" para salvar uma imagem do labirinto na pasta "Imagens" do computador.
7.	Clicar no botão "Limpar" para apagar o labirinto e poder criar outro.

## Licença
Este projeto foi desenvolvido como parte de um projeto escolar e não está licenciado para uso ou distribuição pública. Para qualquer dúvida ou pedido de utilização, por favor, entre em contacto com um dos autores do mesmo.

## Créditos
Este projeto não teria sido possível sem a colaboração e o apoio de várias pessoas. Gostaríamos de agradecer a todos os que contribuíram para o seu sucesso: 

### Equipa de Desenvolvimento 
- **Diogo Almeida** 
- **Guilherme Botelho** 
- **Francisco Furtado** 
- **Filipe Ferreira** 

### Agradecimentos Especiais 
- **Professor Doutor Adrian-Horia Dediu e restantes orientadores** - Orientação e apoio ao longo do projeto 
- **Colegas da Turma** - Feedback e sugestões valiosas 

A todos, os nossos sinceros agradecimentos pelos contributos e dedicação.

# Contactos
Devido a este projeto ter sido realizado com fins escolares, não disponibilizamos contactos para futuras dúvidas ou pedidos.


