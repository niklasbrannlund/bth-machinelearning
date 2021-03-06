% -------------------------------
% Ex 1 - Correlation coefficients

% sample values 
X1 = [2.5, 3.6, 1.2, 0.8, 4.0, 3.4]';
X2 = [1.2, 1.0, 1.8, 0.9, 3.0, 2.2]';
X3 = [8.0, 15.0, 12.0, 6.0, 8.0, 10.0]';

% own implementation of mathematical quantities
cov_own = @(a,b) sum((a-mean(a)).*(b-mean(b)))/(length(a) - 1); % covariance
std_own = @(a) sqrt(sum((a-mean(a)).^2) / (length(a)-1));       % standard deviation
rho_own = @(a,b) cov_own(a,b) / (std_own(a)*std_own(b));        % correlation coefficient

% calculate correlation coefficient matrix
corrcoef_own = [rho_own(X1,X1), rho_own(X1,X2), rho_own(X1,X3);
                rho_own(X2,X1), rho_own(X2,X2), rho_own(X2,X3);
                rho_own(X3,X1), rho_own(X3,X2), rho_own(X3,X3)];

% verify with matlabs own implementation 'corrcoef(...)'
corrcoef_matlab = corrcoef([X1, X2, X3]);

% verify all values in matrices are the same up to 5 decimals
all(round(corrcoef_matlab,5)==round(corrcoef_own,5))