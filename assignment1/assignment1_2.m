% Exercise 2 - Estimate house pricing with K nearest neighbor method

dataset = load('training_dataset.mat');
training_ds = dataset.training_dataset;
k = 2;

testdata = [0, 4, 100, 25;
            0, 1, 60, 20];

[rows, columns] = size(testdata);
        
for i = 1:rows
    % get calculate distance between all datapoints and sort these in
    % separate vectors
    [rooms, roomIndex] = sort(abs(training_ds(:,2)-testdata(i, 2)));
    [sizes, sizeIndex] = sort(abs(training_ds(:,3)-testdata(i, 3)));
    [ages, ageIndex] = sort(abs(training_ds(:,4)-testdata(i, 4)));
    
    % get prize of these houses and average it
    estimatedPrice = mean([mean(training_ds(roomIndex(1:k), 1)), ... 
                           mean(training_ds(sizeIndex(1:k), 1)), ...
                           mean(training_ds(ageIndex(1:k), 1))]);
                       
    testdata(i, 1) = estimatedPrice;
end

% display testdata with added predicted house prices (first column)
testdata

