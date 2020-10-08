PP6 - 8th October 2020

Coder: Matthew Stewart, Carlos Robles

Sharer: Boer Zhang 

Listener: Seeam Noor

## Exercise 2

$f(x,y) = \begin{bmatrix}x^2+y^2\\ exp(x+y) \end{bmatrix}$

Trace:

| trace   | elem op.      | value      | elem der.               | $\nabla_{x}$| $\nabla_{y}$ |
| :---:   | :------:      | :------:   | :--------------------:  | :---------: | :----------: |
| $x_1$   | $x$           |     1      |      $\dot{x_1}$        |       1     |       0      |
| $x_2$   | $y$           |     1      |      $\dot{x_2}$        |       0     |       1      |
| $x_3$   | $x^2_1$       |     1      |      $2 x_1 \dot{x_1}$  |       2     |       0      |
| $x_4$   | $x^2_2$       |     1      |      $2 x_2 \dot{x_2}$  |       0     |       2      |
| $x_5$   | $x_3 + x_4 $  |     2      | $\dot{x_3} + \dot{x_4}$ |       2     |       2      |
| $x_6$   | $x_1 + x_2$   |     2      | $\dot{x_1} + \dot{x_2}$ |       1     |       1      |
| $x_7$   | $exp(x_6)$    |   $exp(2)$ | $\dot{x_6} exp(x_6)$    |   $exp(2)$  |   $exp(2)$   |

$D_p x_7 = \frac{\partial{}x_7}{\partial{}x_1} p_1 + \frac{\partial{}x_7}{\partial{}x_2} p_2$

$D_p x_7 = (\frac{\partial{}x_7}{\partial{}x_6} \frac{\partial{}x_6}{\partial{}x_1}) p_1 + (\frac{\partial{}x_7}{\partial{}x_6} \frac{\partial{}x_6}{\partial{}x_2}) p_2$
