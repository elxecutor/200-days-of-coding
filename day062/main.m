% Day 062: Random Circle Points Plot

theta = linspace(0, 2*pi, 100);
r = 5 + rand(1, 100);
x = r .* cos(theta);
y = r .* sin(theta);
figure;
plot(x, y, 'o'); axis equal;
title('Random Points on a Circle');
