# File to manage the tables of budget data
# References:
#  - https://flask-table.readthedocs.io/en/stable/
from flask_table import Table, Col, DateCol
from flask import url_for

class BudgetTable(Table):
    # The columns, with specified column headers and attributes for the <th> elements
    date = DateCol(
        'Date',
        th_html_attrs={
            'onclick': 'sortTable(0)',
            'class': 'cursor-pointer'
        }
    )
    fac_name = Col(
        'Faculty Name(s)',
        th_html_attrs={
            'onclick': 'sortTable(1)',
            'class': 'cursor-pointer'
        }
    )
    acct_code = Col(
        'Account Code',
        th_html_attrs={
            'onclick': 'sortTable(2)',
            'class': 'cursor-pointer'
        }
    )
    class_code = Col(
        'Class Code (if applicable)',
        th_html_attrs={
            'onclick': 'sortTable(3)',
            'class': 'cursor-pointer'
        }
    )
    amt_expensed = Col(
        'Amount Expensed',
        th_html_attrs={
            'onclick': 'sortTable(4)',
            'class': 'cursor-pointer'
        }
    )
    amt_remaining = Col(
        'Amount Remaining',
        th_html_attrs={
            'onclick': 'sortTable(5)',
            'class': 'cursor-pointer'
        }
    )
    description = Col(
        'Description',
        th_html_attrs={
            'onclick': 'sortTable(6)',
            'class': 'cursor-pointer'
        }
    )

    # String to set as the `id` attribute on the <table> element.
    # This string needs to be identical to the one used to locate the table in sortTable.js
    table_id = 'budget-table'

    # CSS/Bootstrap classes for the <table> element
    classes = ['table', 'table-striped', 'table-bordered', 'table-condensed']

    # CSS/Bootstrap classes for the <thead> element
    thead_classes = ['thead-dark']
