from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Mock database
panels = {
    '1': {
        'id': '1',
        'type': 'Monocrystalline',
        'manufacturer': 'SolarTech',
        'capacity': '300W',
        'Temperature':'50 degrees',
        'Radiation':'1000w/m^2',
        'installation_date': '2021-05-20'
    },
    '2': {
        'id': '2',
        'type': 'Thin-film',
        'manufacturer': 'SolarTech',
        'capacity': '310W',
        'Temperature':'52 degrees',
        'Radiation':'1200w/m^2',
        'installation_date': '2021-06-20'
    },
    '3': {
        'id': '3',
        'type': 'Polycrystalline',
        'manufacturer': 'SolarTech',
        'capacity': '280W',
        'Temperature':'45 degrees',
        'Radiation':'900w/m^2',
        'installation_date': '2021-07-20'
    }
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/track_qr')
def track_qr():
    return render_template('track_qr.html')

@app.route('/track_id', methods=['GET', 'POST'])
def track_id():
    if request.method == 'POST':
        panel_id = request.form.get('panel_id')
        panel = panels.get(panel_id)
        return render_template('track_id.html', panel=panel)
    return render_template('track_id.html', panel=None)

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/panel/<panel_id>')
def get_panel(panel_id):
    panel = panels.get(panel_id)
    if panel:
        return jsonify(panel)
    else:
        return jsonify({'error': 'Panel not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
