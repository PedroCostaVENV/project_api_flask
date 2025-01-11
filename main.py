import mysql.connector
from flask import Flask, make_response, jsonify, request
from bd import carros


mydb = mysql.connector.connect(
    host='localhost',
    user='MainUser',
    password='MainPassword',
    database='Pycodebr'
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/carros', methods=['GET'])
def get_carros():

    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM carros')
    meus_carros = my_cursor.fetchall()

    carros = list()
    for carro in meus_carros:
        carros.append(
            {
                'id': carro[0],
                'marca': carro[1],
                'modelo': carro[2],
                'ano': carro[3]
            }
        )

    response_data = {
        'mensagem': 'lista de carros.',
        'dados': carros
    }
    return make_response(
        jsonify(response_data, 200)
    )

@app.route('/carros', methods=['POST'])
def create_carros():
    
    carro = request.json # captura o valor da requisição
    
    my_cursor = mydb.cursor()
    sql = f"INSERT INTO carros (marca, modelo, ano) VALUES ('{carro['marca']}','{carro['modelo']}', {carro['ano']})"
    my_cursor.execute(sql)
    mydb.commit()

    return make_response(
        jsonify(mensagem='Carro cadastrado com sucesso.', carro=carro)
    )

app.run()