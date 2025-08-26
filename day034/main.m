% Day 034: Random Walk Simulation
N = 100;
steps = randi([-1, 1], 1, N);
walk = cumsum(steps);
plot(walk);
title('Random Walk');
xlabel('Step');
ylabel('Position');
grid on;
