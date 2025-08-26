% Day 060: Random Sine and Cosine Plot
x = linspace(0, 2*pi, 100);
y1 = sin(x + rand());
y2 = cos(x + rand());
plot(x, y1, x, y2);
legend('Sine', 'Cosine');
title('Random Sine and Cosine Plot');

% Day 060: Random Pie Chart Generation
values = randi(20, 1, 5);
labels = {'A', 'B', 'C', 'D', 'E'};
figure;
pie(values, labels);
title('Random Pie Chart');
