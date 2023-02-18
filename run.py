from upload.views import app, db


if __name__ == '__main__':
    db.create_all()#criando BD
    app.run(debug=True)