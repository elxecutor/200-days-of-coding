% Day 091: Random Exponential Decay
x = 0:0.1:5;
y = exp(-x) + rand(size(x))*0.1;
plot(x, y);
title('Random Exponential Decay');
xlabel('x');
ylabel('y');
