from flask import Flask, Blueprint, render_template, request, jsonify, session  
 
lab6 = Blueprint('lab6', __name__)  
offices = []  
for i in range(1, 11):  
    offices.append({"number": i, "tenant": "", "price": 100})  
 
@lab6.route('/lab6/')  
def main():  
    return render_template('lab6/lab6.html')  
 
 
@lab6.route('/lab6/json-rpc-api/', methods=['POST'])  
def api():  
    data = request.json  
    id = data['id']  
    login = session.get('login')  

    if data['method'] == 'info':  
        return jsonify({  
            'jsonrpc': '2.0',  
            'result': offices,  
            'id': id  
        }) 

    if data['method'] == 'booking': 
        office_number = data['params'] 
        for office in offices: 
            if office['number'] == office_number: 
                if office['tenant'] != '': 
                    return jsonify({ 
                        'jsonrpc': '2.0', 
                        'error': { 
                            'code': 2, 
                            'message': 'Office already booked' 
                    }, 
                    'id': id 
                    }) 
                     
                office['tenant'] = login 
                return jsonify({ 
                    'jsonrpc': '2.0', 
                    'result': 'success', 
                    'id': id 
                })

    if data['method'] == 'unbooking':
        office_number = data['params']

        if not login:
            return jsonify({
                'jsonrpc': '2.0',
                'error': {
                    'code': 1,
                    'message': 'Unauthorized'
                },
                'id': id
            })

        for office in offices:
            if office['number'] == office_number:
                if office['tenant'] == '':
                    return jsonify({
                        'jsonrpc': '2.0',
                        'error': {
                            'code': 3,
                            'message': 'Office is not booked'
                        },
                        'id': id
                    })

                if office['tenant'] != login:
                    return jsonify({
                        'jsonrpc': '2.0',
                        'error': {
                            'code': 4,
                            'message': 'You cannot unbook someone else\'s office'
                        },
                        'id': id
                    })
                
                office['tenant'] = ''
                return jsonify({
                    'jsonrpc': '2.0',
                    'result': 'success',
                    'id': id
                })

        return jsonify({
            'jsonrpc': '2.0',
            'error': {
                'code': -32602,
                'message': 'Invalid params: Office not found'
            },
            'id': id
        }

    return jsonify({
        'jsonrpc': '2.0',
        'error': {
            'code': -32601,
            'message': 'Method not found'
        },
        'id': id
    })