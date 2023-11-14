from django.shortcuts import render
from transaction.models import Transaction
from admininstrator.models import Admin
from django.utils import timezone

def renderPage(renderData): 
    if not renderData['request']: 
        return 'No request provided'
    if not renderData['path']:
        return 'No template path provided'
    if not renderData['context']: 
        return render(renderData['request'], renderData['path'])
    return render(renderData['request'], renderData['path'], renderData['context'])

def getTransactionsByMachine(machine_id): 
    try: 
        transactions = Transaction.objects.all().filter(atm_machine_uid = machine_id)
    except: 
        return False 
    if len(transactions) == 0: 
        return False
    return transactions

#METHOD TO SET THE MESSAGE OF CONTEXT OBJECT, ASSUMES THE OBJECT ALREADY HAS A MESSAGE PROPERTY
#@Params: (data) the context object containing the message, (message) string message to be added to message property
def setContextMessage(data, message): 
    data['message'] = message
    return

def getAdmin(user): 
    try:
        admin = Admin.objects.get(username = user)
    except: 
        return False
    return admin

def validatePhoneNumber(phone_number): 
    countCheck = phone_number.count('-')
    if countCheck != 2: 
        return False 
    numberCheck = phone_number.replace('-', '')
    if not numberCheck.isdigit(): 
        return False 
    
    return True



