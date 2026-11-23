assignment = """
Python Assignment

1. Why do you think companies analyze large volumes of data?

Companies analyze large volumes of data because data is the modern world's
compass: it helps businesses stop guessing and make informed decisions.
Without data analysis, running a large company is like driving with a fogged-up
windshield. For example, an online retailer can analyze customer clicks,
purchase histories, and search queries to spot trends. If searches for portable
phone chargers increase before a music festival, the retailer can stock nearby
warehouses and show relevant ads. This can improve sales and help customers.

2. If analyzing and sorting large data manually in Excel is difficult, how
do you think Python can help solve this problem?

Excel is useful for smaller spreadsheets and quick calculations, but it has a
limit of about 1,048,576 rows per worksheet and can become slow with large
files. Python, with libraries such as pandas, can load, clean, filter, and sort
large datasets. It can also automate repetitive work: instead of rebuilding
formulas and pivot tables each week, you can run the same script on new data.

3. Imagine you work at a sales company that receives data about 10,000
customer transactions daily. How would you analyze this data?

I would create a systematic process:

Step 1: Clean the data. Use Python to check for missing values, correct
formatting issues, and identify duplicate transactions.

Step 2: Analyze segments and trends. Group transactions to find the most
popular products, busiest sales times, and customer groups that generate the
most revenue.

Step 3: Report results and set alerts. Create daily summaries or dashboards.
For example, flag a product category if its sales drop significantly compared
with its usual level, so the team can investigate.

4. In your opinion, what tasks can Python be useful for in BI processes?

Python can help throughout the Business Intelligence (BI) process:

1. Data cleaning: standardize dates, correct inconsistent values, and handle
   missing fields before the data reaches a dashboard.
2. Data integration: combine information from databases, cloud storage, and
   APIs into one dataset.
3. Predictive analysis: use libraries such as scikit-learn to forecast sales,
   customer churn, or inventory needs.
4. Visualization: use libraries such as Matplotlib and Seaborn to create
   statistical charts, heatmaps, and trend lines.

5. If you wanted to compare a company's profit year by year, how could this
be done using Python?

I would load the historical financial data into a pandas DataFrame, convert
the date column to datetime format, and then:

1. Group transactions by year and sum the profit for each year.
2. Calculate the percentage change between consecutive years to see how profit
   grew or declined.
3. Plot the yearly profits in a bar chart or line graph using Matplotlib.

6. If you don't know Python, what difficulties might you face when working
with large datasets?

Without Python or a similar programming language, working with large datasets
can be difficult:

1. Spreadsheet software may slow down or may not support all the rows in a
   large file. Splitting the data manually can take time and lead to errors.
2. Without automation, you may need to repeat copying, formatting, and
   calculations whenever new data arrives.
3. Manual tools can make advanced statistical analysis and forecasting more
   difficult, so useful patterns may be missed.
"""

print(assignment)