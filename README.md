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

Para calcular los términos de la secuencia de Tribonacci debemos realizar las potencias de A dependiendo del número de orden a obtener.

A<sup>**_n-3_**</sup> para obtener el orden **_n_** de la secuencia de Tribonacci.

El exponente **_n-3_** se elige porque la secuencia de Tribonacci se define a partir de los primeros tres términos F(0), F(1), F(2), y al elevar la matriz a la potencia **_n-3_**, estamos calculando las iteraciones adicionales hasta llegar al término F(**_n_**).

El cálculo de A<sup>**_n-3_**</sup> para el orden **2023202320232023** consume mucho tiempo, por lo que es necesario recurrir al cáculo de la exponenciación rápida.

El algoritmo se basa en la propiedad de que cualquier potencia de una matriz se puede expresar como una combinación de potencias de orden 2, aplicando repetidas veces la propiedad A<sup>**_mn_**</sup> = (A<sup>**_m_**</sup>)<sup>**_n_**</sup>.

1. **Inicio**:

      Se inicia el resultado con la matriz identidad y se establece el exponente al que se desea elevar la matriz.

2. **Bucle**:

      En cada iteración se verifica si el bit más significativo del exponente es 1. Si es 1, multiplica la matriz resultado por la matriz original A.

      Actualiza la matriz A multiplicándola por sí misma.

      Divide el exponente por 2.

3. **Resultado Final**:

      Después de salir del bucle la matriz resultado contendrá A<sup>**_exponente_**</sup>

El resultado de la potencia luego se multiplica por el vector inicial **[2025, 2024, 2023]** para obtener los términos correspondientes de la secuencia de Tribonacci.

Por último explicaré el uso del operador módulo **%** para obtener los últimos 4 dígitos de un número, y así se evita el desbordamiento y se simplican los resultados.

Cuando se realiza una operación como a x b mod 10000, el resultado será el resto de la división de (a x b) por 10000. Así se obtienen los últimos 4 dígitos del resultado.
Esto es útil cuando trabajamos con números muy grandes y sólo estamos interesados en una cantidad específica de dígitos del resultado.


