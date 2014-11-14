function [J, grad] = costFunctionReg(theta, X, y, lambda)

m = length(y); 
n = length(theta);

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

x = 0;
for j=2:n,
	x = x + theta(j)*theta(j);
end;


J = J / m;
Q = x*(lambda/(2*m));
J = J + Q;
grad = grad / m;
for j=2:n,
	grad(j) = grad(j) + (lambda/m)*theta(j);
end;
	

end;



