import random

# Classe Pokemon
class Pokemon:
    def __init__(self, nome, tipo, nivel=1):
        self.nome = nome
        self.tipo = tipo
        self.nivel = nivel

    def __str__(self):
        return f"{self.nome} (Tipo: {self.tipo}, Nível: {self.nivel})"


# Classe Area
class Area:
    def __init__(self, nome, pokemons):
        self.nome = nome
        self.pokemons = pokemons

    def explorar(self):
        if self.pokemons:
            return random.choice(self.pokemons)
        return None

    def __str__(self):
        return f"Área: {self.nome}"


# Classe Player
class Player:
    def __init__(self, nome):
        self.nome = nome
        self.pokedex = []

    def capturar(self, pokemon):
        self.pokedex.append(pokemon)
        print(f"{self.nome} capturou um {pokemon}!")

    def mostrar_pokedex(self):
        print(f"Pokedex de {self.nome}:")
        for pokemon in self.pokedex:
            print(pokemon)

    def __str__(self):
        return f"Jogador: {self.nome}"


# Classe Game
class Game:
    def __init__(self, jogador, areas):
        self.jogador = jogador
        self.areas = areas

    def jogar(self):
        print("Bem-vindo ao jogo de captura de Pokémon!")
        while True:
            print("\nÁreas disponíveis para explorar:")
            for i, area in enumerate(self.areas):
                print(f"{i + 1}. {area}")

            escolha = input("Escolha uma área para explorar (ou digite 'sair' para encerrar): ")
            if escolha.lower() == 'sair':
                break

            try:
                indice_area = int(escolha) - 1
                area_escolhida = self.areas[indice_area]
                print(f"Explorando a {area_escolhida}...")
                pokemon_encontrado = area_escolhida.explorar()
                if pokemon_encontrado:
                    print(f"Você encontrou um {pokemon_encontrado}!")
                    capturar = input("Deseja capturar este Pokémon? (s/n): ")
                    if capturar.lower() == 's':
                        self.jogador.capturar(pokemon_encontrado)
                else:
                    print("Nenhum Pokémon encontrado desta vez.")
            except (ValueError, IndexError):
                print("Escolha inválida. Tente novamente.")

        print("Jogo encerrado. Sua coleção de Pokémon:")
        self.jogador.mostrar_pokedex()


# Exemplo de uso
if __name__ == "__main__":
    # Criando alguns Pokémon
    pikachu = Pokemon("Pikachu", "Elétrico")
    charmander = Pokemon("Charmander", "Fogo")
    bulbasaur = Pokemon("Bulbasaur", "Planta")

    # Criando áreas com Pokémon
    floresta = Area("Floresta", [pikachu, bulbasaur])
    montanha = Area("Montanha", [charmander])

    # Criando um jogador
    jogador = Player("Ash")

    # Criando o jogo
    jogo = Game(jogador, [floresta, montanha])

    # Iniciando o jogo
    jogo.jogar()
