% Day 047: Random Circle Points
theta = linspace(0, 2*pi, 100);
r = 5 + rand(1, 100);
x = r .* cos(theta);
y = r .* sin(theta);
plot(x, y, 'o'); axis equal;
title('Random Points on a Circle');
