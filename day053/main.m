% Day 053: Random Vector Dot and Cross Product

% Generate two random 3D vectors
v1 = randi(10, 1, 3);
v2 = randi(10, 1, 3);

% Calculate dot and cross product
dot_prod = dot(v1, v2);
cross_prod = cross(v1, v2);

% Display results
fprintf('v1: %s\n', mat2str(v1));
fprintf('v2: %s\n', mat2str(v2));
fprintf('Dot product: %d\n', dot_prod);
fprintf('Cross product: %s\n', mat2str(cross_prod));
