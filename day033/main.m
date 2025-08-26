% Day 033: Random Signal Generation
fs = 1000;
t = 0:1/fs:1-1/fs;
signal = randn(size(t));
plot(t, signal);
title('Random Signal');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;
