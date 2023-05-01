#! /usr/bin/env python3
#! -*- coding: utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for, send_file
import tech, main
import io, os
from config import PATH, UPLOAD_FOLDER, ALLOWED_EXTENSIONS, ALLOWED_EXTENSIONS_STR, allowed_file
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder="static")



@app.route('/', methods=["GET", "POST"])
def start():
    return redirect(url_for('render_home_page'), 301)

@app.route("/home")
def render_home_page():
    return render_template("welcome-page.html", title="Home")



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@app.route("/login")
def render_login_form():
    return render_template("login-form.html", title="login")

@app.route("/reg")
def render_reg_form():
    return render_template("registration-form.html", title="registration")

@app.route("/rules")
def render_rules():
    return "<div> Правила позже :) <div>"

@app.route("/warning")
def render_not_found_page():
    return render_template("not-found-page.html", title="Sorry, but it's 404...")

@app.route("/waiting")
def render_waiting_email_page():
    return render_template("waiting-email-page.html", title="Please, check your e-mail")
    
@app.route("/account")
def render_account_page():
    return render_template("account.html", title="Profile")

@app.route("/account-admin")
def render_account_admin_page():
    return render_template("account-admin.html", title="Profile-admin")

@app.route("/support")
def render_support():
    return render_template("tech-support.html", title="Technical support")
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




#============================================================
@app.route("/table", methods=["GET", "POST"])
def gfg():
    #get fresh info from module tech
    w_timetable, w_swaps_file_name, w_swaps, w_timetable_time, w_swaps_time = tech.pass_info()
    teachers_list_otch, teachers_list, len_list= tech.get_surnames_with_otch(w_swaps_file_name)
    #===============================

    if request.method == "POST":
        first_name = request.form.get("fname")
        if first_name in teachers_list:
            print('')
            file_out = main.api(key_word=first_name.capitalize())
            f = open(file_out, "rb")
            return send_file(io.BytesIO(f.read()), download_name=f'Замены_{first_name}.xlsx')



    return render_template("table-page.html", title="Main", w_timetable= w_timetable, w_swaps= w_swaps, ln=teachers_list_otch, lenarr=len_list, teachers_list_otch=teachers_list)
#============================================================



@app.route("/upload", methods=["GET", "POST"])
def render_upload_page():
    if  request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('zero file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            if filename.split('.')[-1] == 'docx':
                print(f'{PATH}{UPLOAD_FOLDER}/swaps/{filename}')
                file.save(f'{PATH}{UPLOAD_FOLDER}/swaps/{filename}')
                print('')
                w_timetable, w_swaps_file_name, w_swaps, w_timetable_time, w_swaps_time = tech.pass_info()
                #teachers_list, len_list= tech.get_surnames(w_swaps_file_name)
                teachers_list_otch, teachers_list, len_list= tech.get_surnames_with_otch(w_swaps_file_name)

                return render_template("table-page.html", title="Main", w_timetable= w_timetable, w_swaps= w_swaps, ln=teachers_list_otch, lenarr=len_list, teachers_list_otch=teachers_list)

    return render_template("upload-page.html", title="Upload")

#ssl_context=("iorin.crt","iorin.key"),
if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True)

