from behave import step  # the framework
from solve import sum

# decimal sum
@step('sum "{val_0:d}" com "{val_1:d}"')
def test_sum(context, val_0, val_1):
    context.result = sum(val_0, val_1) # context.result is equal global result

@step('O resultado é "{response:d}"')
def test_sum_response(context, response):
    assert context.result == response

# float sum
@step('sum "{val_0:f}" com "{val_1:f}"')
def test_sum(context, val_0, val_1):
    context.result = sum(val_0, val_1)
    
@step('O resultado é "{response:f}"')
def test_sum_response(context, response):
    assert context.result == response 