function p = predictOneVsAll(all_theta, X)
m = size(X, 1);
b = [1:size(all_theta,1)];


num_labels = size(all_theta, 1);
p = zeros(size(X, 1), 1);
% Add ones to the X data matrix
X = [ones(m, 1) X];


theta = all_theta;
q = X*theta';
for i=1:m,
	a = q(i,:);
	t = (q(i,:) == max(a));
	prediction = t*b';
	p(i) = prediction;
end;


end
