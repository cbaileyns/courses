function p = predict(Theta1, Theta2, X)

m = size(X, 1);
num_labels = size(Theta2, 1);
X = [ones(m, 1) X];

p = zeros(size(X, 1), 1);

z1 = X*Theta1';
g1 = sigmoid(z1);
g1 = [ones(m, 1) g1];
a2 = g1;
z2 = a2*Theta2';
g2 = sigmoid(z2);
h = g2;

b = [1:size(h,2)];

for i=1:m,
	a = h(i,:);
	t = (h(i,:) == max(a));
	prediction = t*b';
	p(i) = prediction;
end;



end
