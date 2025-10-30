from website import create_app #absolute import from the package (__init__)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)