% Day 035: Random Image Generation
img = randi([0, 255], 100, 100, 3, 'uint8');
imshow(img);
title('Random RGB Image');
