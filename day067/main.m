
% Day 067: Random Noise Addition to Sine Wave

x = linspace(0, 2*pi, 100);
y = sin(x);
noise = randn(size(x)) * 0.2;
y_noisy = y + noise;
plot(x, y, 'b', x, y_noisy, 'r');
legend('Original', 'Noisy');
title('Sine Wave with Random Noise');
xlabel('x'); ylabel('y');
