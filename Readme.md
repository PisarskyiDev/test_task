# Test Task

# Project Description 
 The Test Task project is a web application built using the Django framework. This application provides two endpoints: /api/revenue and /api/spend, designed for working with revenue and expenditure data.

# Installation
 To install and run the project, follow these steps:
```shell 
git clone https://github.com/PisarskyiDev/test_task.git
cd test_task
```
 Then open the project, after open follow this commands:
```shell 
python -m venv venv
source venv/bin/activate  # On Linux or macOS
pip install -r requirements.txt
```
 Apply migrations and create a superuser (if needed):
```shell
python manage.py migrate
python manage.py createsuperuser
```
 Start the Django development server:
```shell
python manage.py runserver localhost:8000
```

# Key Features

>/api/revenue/

The /api/revenue/ endpoint allows you to retrieve revenue statistics, with the option to filter by date and product name. The endpoint returns a queryset of the RevenueStatistic model, including aggregated sums of revenue, spend, impressions, clicks, and conversion values from the SpendStatistic model.

>/api/spend/

The /api/spend/ endpoint enables you to obtain expenditure statistics, with the ability to filter by date and product name. You can also filter the results by date and product name. The endpoint returns a queryset of the SpendStatistic model, including aggregated sums of spend, impressions, clicks, conversion, and associated revenue values from the RevenueStatistic model.



