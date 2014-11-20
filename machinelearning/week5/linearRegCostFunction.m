function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
h = X*theta;
error = h - y;
temp = theta;
temp(1) = 0;
J = error'*error + lambda*temp'*temp;
J = J / (2*m);
grad = zeros(size(theta));
grad = ((error'*X)/m) + (lambda/m)*temp';


grad = grad(:);

end
