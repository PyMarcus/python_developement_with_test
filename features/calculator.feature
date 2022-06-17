# language: pt

Funcionalidade: Resolve soma
    Cenario:  somar dois valores
    Quando sum "2" com "2"
    Entao O resultado é "4"
    # Example: 2 + 2 = 


    Cenario:  somar dois valores de ponto flutuante
    Quando sum "2.0" com "2.0"
    Entao O resultado é "4.0"
    # Example: 2 + 2 = 4
