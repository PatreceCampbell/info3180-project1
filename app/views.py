"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from .forms import PropForm
import os
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from werkzeug.utils import secure_filename
from app.models import PropertyTable
import psycopg2

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Patrece Campbell")

@app.route('/property', methods=['GET', 'POST'])
def property():
    """ Render the website's property form """
    propform = PropForm()

    if request.method == 'POST': 
        if propform.validate_on_submit():
            title = propform.title.data
            bedrooms = propform.bedrooms.data
            bathrooms = propform.bathrooms.data
            location = propform.location.data
            price = propform.price.data
            option = propform.option.data
            description = propform.description.data
            photo = propform.photo.data

            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            propertydb = PropertyTable(title, bedrooms, bathrooms, location, price, option, description, filename)
            db.session.add(propertydb)
            db.session.commit()
            
            flash('Property Added!', 'success')
            return redirect(url_for('properties'))
        else:
            return flash_errors(propform)
    return render_template('propertyform.html', form=propform)

def connect_db():
    return psycopg2.connect(host="localhost",database="project1", user="project1", password="project1")

def get_uploaded_images():
    rootdir = os.getcwd()
    photolist = []

    for subdir, dirs, files in os.walk(rootdir + '/uploads'):
        for file in files:
            photolist += [file]
    photolist.pop(0)
    return photolist

@app.route('/uploads/<filename>')
def get_image(filename):
    rootdir2 = os.getcwd()

    return send_from_directory(os.path.join(rootdir2, app.config['UPLOAD_FOLDER']), filename)

@app.route('/properties')
def properties():
    """ Render the website's properties page """
    
    props = db.session.query(PropertyTable).all()
    return render_template('properties.html', props=props)

@app.route('/property/<propertyid>')
def viewproperty(propertyid):
    """ Render the websites view property page """

    view = db.session.query(PropertyTable).filter_by(id=propertyid).all()
    return render_template('viewproperty.html', view=view)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
