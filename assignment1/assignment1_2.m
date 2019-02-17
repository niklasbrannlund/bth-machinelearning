% Exercise 2 - Estimate house pricing with K nearest neighbor method

dataset = load('training_dataset.mat');
training_ds = dataset.training_dataset;
k = 2;

testdata = [0, 4, 100, 25;
            0, 1, 60, 20];

[rows, columns] = size(testdata);
        
for i = 1:rows
    
    % calculate manhattan distance
    distance = abs(training_ds(:, 2) - testdata(i, 2)) + ... % room variable distance
               abs(training_ds(:, 3) - testdata(i, 3)) + ... % size variable distance
               abs(training_ds(:, 4) - testdata(i, 4));      % age variable distance
           
    % sort the distance vector
    [sortedDistance, indexes] = sort(distance);
    
    % pick out the k closest neighbors from training dataset
    prices = training_ds(indexes(1:k), 1);
    
    % get the estimated house price using mean of training prices
    estimatedPrice = mean(prices);
                       
    testdata(i, 1) = estimatedPrice;
end

% display testdata with added predicted house prices (first column)
testdata

