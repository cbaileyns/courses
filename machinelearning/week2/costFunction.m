function [J, grad] = costFunction(theta, X, y)

m = length(y); % number of training examples
n = size(X)(2)

% You need to return the following variables correctly 
J = 0;

grad = zeros(size(theta));

for i=1:m,
	z = theta'*X(i,:)';
	v = (-y(i)*log(sigmoid(z)) - (1 - y(i))*log(1-sigmoid(z)));
	J = J + v;
	for j=1:n,
		grad(j) = grad(j) + (sigmoid(z) - y(i))*X(i,j);
	end;
end;

J = J / m;
grad = grad / m;
	

end;
