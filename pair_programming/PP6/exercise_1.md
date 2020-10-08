PP6 - 8th October 2020

Coder: Matthew Stewart, Carlos Robles

Sharer: Boer Zhang 

Listener: Seeam Noor

## Exercise 1

(1) Graph done on paper.

Function is: $f(x,y)=exp(-(sin(x)-cos(y))^2)$

(2) Trace:

| trace   | elem op.    | value      | elem der.               | $\nabla_{x}$| $\nabla_{y}$ |
| :---:   | :------:    | :------:   | :--------------------:  | :---------: | :----------: |
| $x_1$   | $x$         |  $\pi/2$   | $\dot{x_1}$             |         1   |      0       |
| $x_2$   | $y$         |  $\pi/3$   | $\dot{x_2}$             |         0   |      1       |
| $x_3$   | $sin(x_1)$  |  $1$       | $cos(x_1)\dot{x_1}$.    |         0   |      0       |
| $x_4$   | $cos(x_2)$  |  $1/2$     | $-sin(x_2)\dot{x_2}$.   |         0   | $-\sqrt{3}/2$|
| $x_5$   | $x_3 - x_4$ |  $1/2$     | $\dot{x_3} - \dot{x_4}$ |         0   | $\sqrt{3}/2$ |
| $x_6$   | $x^2_5$     |  $1/4$     | $2x_5 \dot{x_5}$        |         0   | $\sqrt{3}/2$ |
| $x_7$   | $-x_6$      |  $-1/4$    | $-x_6$                  |         0   | $-\sqrt{3}/2$                   |
| $x_8$   | $exp(x_7)$  | $exp(-1/4)$| $exp(x_7) \dot{x_7}$    |         0   | $-\frac{\sqrt{3}}{2} exp(-1/4)$ |


(3) Evaluation at $f(\pi/2, \pi/3) = exp(-1/4)$

(4) $\frac{df}{dx}(\pi/2, \pi/3) = 0$

$\frac{df}{dy}(\pi/2, \pi/3) = -\frac{\sqrt{3}}{2} exp(-1/4)$