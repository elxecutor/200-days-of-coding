
% Day 039: Random Signal and FFT Analysis

% Generate a random signal
fs = 500; % Sampling frequency
t = 0:1/fs:1-1/fs;
signal = randn(size(t));

% Compute FFT
N = length(signal);
f = (0:N-1)*(fs/N);
Y = abs(fft(signal));

% Display results
figure;
subplot(2,1,1);
plot(t, signal);
title('Random Signal');
xlabel('Time (s)'); ylabel('Amplitude');

subplot(2,1,2);
plot(f, Y);
title('FFT of Random Signal');
xlabel('Frequency (Hz)'); ylabel('Magnitude');
