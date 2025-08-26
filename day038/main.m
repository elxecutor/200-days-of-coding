% Day 038: Random Sine Wave
f = randi([1, 10]);
t = linspace(0, 2*pi, 1000);
y = sin(f*t);
plot(t, y);
title(['Random Sine Wave, f = ' num2str(f) ' Hz']);
xlabel('Time');
ylabel('Amplitude');
grid on;
