# companies_bankruptcy_prediction
Bankruptcy prediction of Polish companies based on the dataset: https://archive.ics.uci.edu/ml/datasets/Polish+companies+bankruptcy+data

Relevant paper:
- Zieba, M., Tomczak, S. K., & Tomczak, J. M. (2016). Ensemble Boosted Trees with Synthetic Features Generation in Application to Bankruptcy Prediction. Expert Systems with Applications.

Areas: finance, econometrics.

To install all libraries and run the notebooks from Docker:
- docker-compose build
- docker-compose up

Goals:
1. find the subsets of the most significant features using different feature selection methods (Kendall's tau, mutual information, ANOVA);
2. implement the model that performs well in solving 6-class classification task:
- multi-class classification (6 classes - firm did not bankrupt or bankrupted after 1..5 years).

Results:
- random forest with maximum depth = 10 (parameter tuning using Grid Search) solves 6-class classification with area under the precision-recall curve **0.966** on the data that was:
    1. cleaned from the missing values,
    2. oversampled with SMOTE (Synthetic Minority Over-sampling Technique).

![Alt text](models/pr_curve.png?raw=true)


Class values for binary classification:

- 0 - company that did not bankrupt in the forecasting period
- 1 - bankrupted company

Class values for 6-class classification:

- 0 - company that did not bankrupt in the forecasting period
- 1 - company bankrupted after 1 year
- 2 - company bankrupted after 2 years
- 3 - company bankrupted after 3 years
- 4 - company bankrupted after 4 years
- 5 - company bankrupted after 5 years

Synthetic attributes description:

- X1 net profit / total assets
- X2 total liabilities / total assets
- X3 working capital / total assets
- X4 current assets / short-term liabilities
- X5 ((cash + short-term securities + receivables - short-term liabilities) / (operating expenses - depreciation)) * 365
- X6 retained earnings / total assets
- X7 EBIT / total assets
- X8 book value of equity / total liabilities
- X9 sales / total assets
- X10 equity / total assets
- X11 (gross profit + extraordinary items + financial expenses) / total assets
- X12 gross profit / short-term liabilities
- X13 (gross profit + depreciation) / sales
- X14 (gross profit + interest) / total assets
- X15 (total liabilities * 365) / (gross profit + depreciation)
- X16 (gross profit + depreciation) / total liabilities
- X17 total assets / total liabilities
- X18 gross profit / total assets
- X19 gross profit / sales
- X20 (inventory * 365) / sales
- X21 sales (n) / sales (n-1)
- X22 profit on operating activities / total assets
- X23 net profit / sales
- X24 gross profit (in 3 years) / total assets
- X25 (equity - share capital) / total assets
- X26 (net profit + depreciation) / total liabilities
- X27 profit on operating activities / financial expenses
- X28 working capital / fixed assets
- X29 logarithm of total assets
- X30 (total liabilities - cash) / sales
- X31 (gross profit + interest) / sales
- X32 (current liabilities * 365) / cost of products sold
- X33 operating expenses / short-term liabilities
- X34 operating expenses / total liabilities
- X35 profit on sales / total assets
- X36 total sales / total assets
- X37 (current assets - inventories) / long-term liabilities
- X38 constant capital / total assets
- X39 profit on sales / sales
- X40 (current assets - inventory - receivables) / short-term liabilities
- X41 total liabilities / ((profit on operating activities + depreciation) * (12/365))
- X42 profit on operating activities / sales
- X43 rotation receivables + inventory turnover in days
- X44 (receivables * 365) / sales
- X45 net profit / inventory
- X46 (current assets - inventory) / short-term liabilities
- X47 (inventory * 365) / cost of products sold
- X48 EBITDA (profit on operating activities - depreciation) / total assets
- X49 EBITDA (profit on operating activities - depreciation) / sales
- X50 current assets / total liabilities
- X51 short-term liabilities / total assets
- X52 (short-term liabilities * 365) / cost of products sold)
- X53 equity / fixed assets
- X54 constant capital / fixed assets
- X55 working capital
- X56 (sales - cost of products sold) / sales
- X57 (current assets - inventory - short-term liabilities) / (sales - gross profit - depreciation)
- X58 total costs /total sales
- X59 long-term liabilities / equity
- X60 sales / inventory
- X61 sales / receivables
- X62 (short-term liabilities *365) / sales
- X63 sales / short-term liabilities
- X64 sales / fixed assets