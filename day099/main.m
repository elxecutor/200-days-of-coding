% Day 099: Random Walk Simulation and Plot
N = 100;
steps = randi([-1, 1], 1, N);
walk = cumsum(steps);
plot(walk);
title('Random Walk');
xlabel('Step');
ylabel('Position');
grid on;
