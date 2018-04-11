from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            .error {{
                color: red;
            }}
        </style>
    </head>
    <body>
    <h1>Signup</h1>
        <form action="/" method="get">
            <table>
                <tbody>
                <tr>
                    <td><label for="username">Username</label></td>
                    <td>
                        <input name="username" type="text" value="{username}">
                        <span class="error">{username_error}</span>
                    </td>
                </tr>
                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" type="password" value="{password}">
                        <span class="error">{password_error}</span>
                    </td>
                </tr>
                <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify" type="password" value="{password}">
                        <span class="error">{password_error}</span>
                    </td>
                </tr>
                <tr>
                    <td><label for="email">Email (optional)</label></td>
                    <td>
                        <input name="email" value="{email}">
                        <span class="error">{email_error}</span>
                    </td>
                </tr>
            </tbody></table>
            <input type="submit" value="validate">
        </form>
    </body>
    </head>
</html>
"""

@app.route("/")
def display_form():
    return form.format(username='', username_error='', password='',
    password_error='', email='', email_error='')

@app.route("/", methods=['POST'])
def validate_form():

    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    return form


app.run()