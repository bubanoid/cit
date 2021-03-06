import os
from flask import g
from ..db import db
from .models import Issue
from ..auth.models import User
from flask import Blueprint, request, redirect, url_for, jsonify, current_app, session, jsonify
from werkzeug import secure_filename
from werkzeug.datastructures import FileStorage
from shapely.geos import WKBReader, lgeos
from shapely.geometry import Point

issues_bp = Blueprint('issues', __name__)


@issues_bp.route('/', methods=['GET', 'POST'])
def issues_info():
    issues_user_query = db.session.query(Issue, User).join(User).all()
    table_dict = []
    for issue, user in issues_user_query:
        list_row = {}
        point = WKBReader(lgeos).read_hex(str(issue.coordinates))
        list_row.update({
            'type': 'Feature',
            'properties': {
                'id': issue.id,
                'reporter': {
                    'name': user.fb_first_name,
                    'surname': user.fb_last_name,
                    'fb_id': user.fb_id
                },
                'description': issue.description
            },
            "geometry": {
                'coordinates': [point.x, point.y],
                'type': 'Point'
            }
        })
        table_dict.append(list_row)

    return jsonify(type='FeatureCollection', features=table_dict, name='Points', keyField='GPSUserName')


@issues_bp.route('/file-upload/', methods=['POST'])
def upload_file():
    error = 0
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
    else:
        filename = ''
        error = 2 

    return jsonify({'filename': filename, 'error': error})
