### Solución al puzzle
    
Los últimos cuatro dígitos del orden **2023202320232023** son: **3363**

#### La lógica de la solución es la siguiente:
    
Se trata de la sucesión de Tribonacci con valores iniciales son 2023, 2024 y 2025, y los siguientes valores se obtienen de la siguiente manera: 

- orden 2: 2023+2024+2025=6072, 

- orden 3: 2024+2025+6072=10121, 

- y así sucesivamente. 


Para hallar el orden **2023202320232023**, el cálculo consume mucho tiempo y recursos de la computadora. Para evitar esto se deben utilizar estrategias de la matemática para solucionarlo.

Una forma es hallando la **matriz de transformación** de la relación de recurrencia que define la secuencia de Tribonacci, siguiendo los siguientes pasos:

Se determina la relación de recurrencia de la secuencia de Tribonacci:

      F(n) = F(n-1)+F(n-2)+F(n-3)

La relación de recurrencia se puede expresar como una multiplicación de matrices:

        Xn = A . Xn-1

Donde Xn se expresa de manera matricial de la siguiente manera:

          ┌───   ───┐ 
          │  F(n)   │ 
    Xn =  │ F(n-1)  │ 
          │ F(n-2)  │ 
          └───   ───┘ 

A es la matriz de transformación que se utiliza para representar la relación de recurrencia de la secuencia de Tribonacci:

           ┌───  ───┐  
           │ 1 1 1  │  
     A =   │ 1 0 1  │  
           │ 0 1 0  │  
           └───  ───┘

Y el vector columna Xn-1:

            ┌───   ───┐ 
            │ F(n-1)  │ 
    Xn-1 =  │ F(n-2)  │ 
            │ F(n-3)  │ 
            └───   ───┘ 

Entonces Xn = A . Xn-1, quedaría así:

    ┌───   ───┐     ┌───  ───┐    ┌───   ───┐
    │  F(n)   │     │ 1 1 1  │    │  F(n-1) │
    │ F(n-1)  │  =  │ 1 0 1  │  . │  F(n-2) │
    │ F(n-2)  │     │ 0 1 0  │    │  F(n-3) │
    └───   ───┘     └───  ───┘    └───   ───┘

La multiplicación de matrices se realiza de la siguiente manera:

    ┌───   ───┐     ┌───                 ───┐
    │  F(n)   │     │  F(n-1)+F(n-2)+F(n-3) │
    │ F(n-1)  │   = │         F(n-1)        │
    │ F(n-2)  │     │         F(n-2)        │
    └───   ───┘     └───                 ───┘

Esto se utiliza para buscar el primer término de la secuencia de Tribonacci. 

Para calcular los siguientes términos debemos realizar las potencias de A dependiendo del número de orden a obtener.

A<sup>n</sup> para obtener el orden n de la secuencia de Tribonacci.




