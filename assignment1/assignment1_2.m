% Exercise 2 - Estimate house pricing

dataset = load('training_dataset.mat');
training_ds = dataset.training_dataset;

testdata = [0, 4, 100, 25;
            0, 1, 60, 20];
        
for i = 1:2
    [rooms, roomIndex] = min(abs(training_ds(:,2)-testdata(i, 2)));
    [sizes, sizeIndex] = min(abs(training_ds(:,3)-testdata(i, 3)));
    [ages, ageIndex] = min(abs(training_ds(:,4)-testdata(i, 4)));
    
    % get prize of these houses and average it
    estimatedPrice = mean([training_ds(roomIndex, 1), training_ds(sizeIndex, 1), training_ds(ageIndex, 1)]);
    testdata(i, 1) = estimatedPrice;
end

% display estimated prices of houses in testdata
testdata(:, 1)

