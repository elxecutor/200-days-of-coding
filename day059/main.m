
% Day 059: Random Surface Plot Generation

[X, Y] = meshgrid(1:0.5:10, 1:0.5:10);
Z = rand(size(X)) * 10;

% Plot surface
figure;
surf(X, Y, Z);
title('Random Surface Plot');
xlabel('X'); ylabel('Y'); zlabel('Z');
