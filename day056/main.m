
% Day 056: Random Bar Chart Generation

% Generate random data
data = randi(100, 1, 10);

% Display data
disp('Random data:');
disp(data);

% Plot bar chart
figure;
bar(data);
title('Random Bar Chart');
xlabel('Index'); ylabel('Value');
