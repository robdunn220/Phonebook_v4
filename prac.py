from flask import Flask, render_template, request, redirect
import pg

db = pg.DB(dbname='phonebook')
app = Flask('MyApp')

@app.route('/display_all')
def display_all():
    query = db.query('select * from phonebook')
    return render_template(
        'phonebook.html',
        title='Contacts',
        phonebook_list=query.namedresult()
    )

@app.route('/new_phonebook')
def new_phonebook_form():
    return render_template(
        'new_phonebook.html',
        title='New Contact')

@app.route('/submit_new_phonebook', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    phone_number = request.form.get('phone_number')
    db.insert(
        'phonebook',
        name=name,
        phone_number = phone_number,
        email=email
        )
    return redirect('/display_all')

@app.route('/update_phonebook')
def update_phonebook_form():
    id = request.args.get('id')
    if not id:
        return redirect('/display_all')
    sql = 'select * from phonebook where id = %s' % id
    print sql
    result_list = db.query(sql).namedresult()
    phonebook = result_list[0]
    return render_template(
        'update_phonebook.html',
        title='Update Phonebook',
        phonebook=phonebook)

@app.route('/submit_update_phonebook', methods=['POST'])
def submit_update():
    id = request.form.get('id')
    name = request.form.get('name')
    email = request.form.get('email')
    phone_number = request.form.get('phone_number')
    db.update(
        'phonebook', {
        'id': id,
        'name': name,
        'phone_number': phone_number,
        'email': email
        }
        )
    return redirect('/display_all')

if __name__=='__main__':
    app.run(debug=True)
