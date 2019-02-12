% sample values 
X1 = [2.5, 3.6, 1.2, 0.8, 4.0, 3.4]';
X2 = [1.2, 1.0, 1.8, 0.9, 3.0, 2.2]';
X3 = [8.0, 15.0, 12.0, 6.0, 8.0, 10.0]';

% correlation coefficient matrix - each column represents a variable
% and each row represents an observation
correlation_coefficient = corrcoef([X1, X2, X3]);
