from flask import Flask, request
import requests
import psycopg2
app = Flask(__name__)

db__info = "dbname=flask-postgres user=postgres password='0095'"


def db(address):
    conn = psycopg2.connect(db__info)
    cur = conn.cursor()
    cur.execute("SELECT * FROM nft where address='"+address+"'")
    if cur.rowcount == 0:
        return False
    return True


@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        return__v = ''
        address = request.form.get('address')
        if db(address):
            connection__pg4 = psycopg2.connect(db__info)
            cur = connection__pg4.cursor()
            cur.execute("SELECT metadata FROM nft where address='"+address+"'")
            records__sql = cur.fetchall()
            return__v = records__sql[0][0]
        else:
            url__solana = 'https://solana-gateway.moralis.io/nft/mainnet/{}/metadata'.format(
                address)
            return__v = requests.get(url__solana, headers={
                "accept": "application/json",
                "X-API-Key": "rxutHtSPhOrUi3Akni1pDggwTvbKuj7iHifSR8BT0Obv5Hi2UNyMZ6lDYnMfz8vx"
            }).text
            connection__pg4 = psycopg2.connect(db__info)
            cur = connection__pg4.cursor()
            cur.execute("insert into nft(address,metadata) values('{}','{}')".format(
                address, return__v))
            connection__pg4.commit()
        return '''
                <p>{}</p>
                  '''.format(return__v)

    return '''
	 	<div align = "center">
         <form method="POST">
				<label>
					address: 
				</label></br></br>
				<input type="text" name="address"></br></br>
            <input type="submit" value="Get Info">
         </form>
		</div>'''


if __name__ == '__main__':
    app.run(debug=True, port=5000)
