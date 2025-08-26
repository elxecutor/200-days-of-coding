
% Day 070: Random Points Clustering and Plot

X = [randn(50,2)+2; randn(50,2)-2];
idx = kmeans(X,2);
gscatter(X(:,1), X(:,2), idx);
title('Random Points Clustering');
xlabel('X'); ylabel('Y');
