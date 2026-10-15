# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
The majority of the model was developed by Udacity. Some code was written by Calvin Kingery.
The model was created October 2026. It is a logistic regression model. Feedback can be sent to ckinge9@wgu.edu.

## Intended Use
The primary intended use for is to show whether an individual makes >$50k or not. The model was developed to show
demonstrate expertise in creating a working machine learning pipeline.

## Training Data
The training data is from a training data split of the census.csv file.

## Evaluation Data
The test data is from a test data split of the census.csv file.

## Metrics
_Please include the metrics used and your model's performance on those metrics._
The model shows performance on Precision, Recall, and F1-Score, both as a whole, and as individual slices of the data.
The overall metrics for the data were as follows: Precision: 0.7490, Recall: 0.6136, F1: 0.6746
The data slices are covered in the slice_output.txt file and show various information such as metrics by race, gender,
education, job type, country, or marital status. Some of the metrics have very small sample sizes, leading to
irregular scores.

## Ethical Considerations
Limited data on certain demographics lead to them either not being present in the data, or having irregular scores.
The data is from an older data set and may not represent current economic standings.

## Caveats and Recommendations
Due to older, incomplete data, it is suggested to obtain a more current, robust version or the census data and 
utilize it, or compare it to the older data set.
