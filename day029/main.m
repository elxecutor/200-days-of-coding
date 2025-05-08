%% Simulation parameters
P0 = 10;        % initial population
r = 0.1;        % growth rate per time step
T = 100;        % total simulation time
dt = 1;         % time step

time = 0:dt:T;  % time vector
nSteps = length(time);

%% FOR LOOP simulation (Exponential growth)
pop_for = zeros(1, nSteps);
pop_for(1) = P0;
for k = 2:nSteps
  pop_for(k) = pop_for(k-1) + r * pop_for(k-1) * dt;
end

%% WHILE LOOP simulation (Exponential growth)
pop_while = zeros(1, nSteps);
pop_while(1) = P0;
index = 2;
while index <= nSteps
  pop_while(index) = pop_while(index - 1) + r * pop_while(index - 1) * dt;
  index = index + 1;
end

%% Plotting results
figure;
plot(time, pop_for, 'b-', 'LineWidth', 2);
hold on;
plot(time, pop_while, 'r--', 'LineWidth', 2);
xlabel('Time');
ylabel('Population');
title('Population Growth Model');
legend('For Loop', 'While Loop');
grid on;