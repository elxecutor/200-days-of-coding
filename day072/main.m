% Day 072: Random Signal and FFT Analysis

fs = 500;
t = 0:1/fs:1-1/fs;
signal = randn(size(t));
N = length(signal);
f = (0:N-1)*(fs/N);
Y = abs(fft(signal));
figure;
subplot(2,1,1);
plot(t, signal);
title('Random Signal');
xlabel('Time (s)'); ylabel('Amplitude');
subplot(2,1,2);
plot(f, Y);
title('FFT of Random Signal');
xlabel('Frequency (Hz)'); ylabel('Magnitude');

% Additional context or existing code can be placed here if needed
