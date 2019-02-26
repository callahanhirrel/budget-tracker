# File to manage the tables of budget data
# References:
#  - https://flask-table.readthedocs.io/en/stable/
from flask_table import Table, Col, DateCol
from flask import url_for

class BudgetTable(Table):
    # The columns and column headers
    date = DateCol('Date')
    fac_name = Col('Faculty Name(s)')
    acct_code = Col('Account Code')
    class_code = Col('Class Code (if applicable)')
    amt_expensed = Col('Amount Expensed')
    amt_remaining = Col('Amount Remaining')
    description = Col('Description')

    # TODO Make the table sortable
    #allow_sort = True

    # CSS/Bootstrap classes for the <table> element
    classes = ['table', 'table-striped', 'table-bordered', 'table-condensed']

    # CSS/Bootstrap classes for the <thead> element
    thead_classes = ['thead-dark']

# TODO
#    def sort_url(self, col_key, reverse=False):
#        if reverse:
#            direction = 'desc'
#        else:
#            direction = 'asc'
#        return url_for('index', sort=col_key, direction=direction)
