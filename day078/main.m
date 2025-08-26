
% Day 078: Random Sine Wave Generation and Plot

f = randi([1, 10]);
t = linspace(0, 2*pi, 1000);
y = sin(f*t);
fprintf('Frequency: %d Hz\n', f);
figure;
plot(t, y);
title(['Random Sine Wave, f = ' num2str(f) ' Hz']);
xlabel('Time'); ylabel('Amplitude');
grid on;
