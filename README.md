    Los últimos cuatro dígitos del orden 2023202320232023 son: 3363

    La lógica de la solución es la siguiente:
    
    Se trata de la sucesión de Tribonacci con valores iniciales son 2023, 2024 y 2025, y los siguientes valores se obtienen de la siguiente manera: 
    2023+2024+2025=6072, 
    2024+2025+6072=10121, 
    y así sucesivamente. 

    Para hallar el orden 2023202320232023,  se deben utilizar estrategias de la matemática para solucionar.
    
    Matriz de transformación que se obtiene al observar la relación de recurrencia que define la secuencia de Tribonacci:
    F(n) = F(n-1)+F(n-2)+F(n-3)
    Esta relación se puede expresar de manera matricial utilizando un vector de columnas que contiene 
    los términos de la secuencia:
          ┌───   ───┐ 
          │  F(n)   │ 
    Xn =  │ F(n-1)  │ 
          │ F(n-2)  │ 
          └───   ───┘ 
    La relación de recurrencia se puede expresar
    como una multiplicación de matrices:
        Xn = A x Xn-1
    
    ┌───   ───┐     ┌───  ───┐    ┌───               ───┐
    │  F(n)   │     │ 1 1 1  │    │  F(n)+F(n-1)+F(n-2) │
    │ F(n-1)  │  X  │ 1 0 1  │  = │        F(n)         │
    │ F(n-2)  │     │ 0 1 0  │    │       F(n-1)        │
    └───   ───┘     └───  ───┘    └───               ───┘
