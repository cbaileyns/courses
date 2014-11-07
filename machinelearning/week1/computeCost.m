function J = computeCost(X, y, theta)
m = length(y); % number of training examples
% You need to return the following variables correctly 
J = (X*theta - y)'*(X*theta - y);
J = J / (2*m);
end
