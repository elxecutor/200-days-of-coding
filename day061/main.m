
% Day 061: Random Exponential Decay Plot

x = 0:0.1:5;
y = exp(-x) + rand(size(x))*0.1;
figure;
plot(x, y);
title('Random Exponential Decay');
xlabel('x'); ylabel('y');
