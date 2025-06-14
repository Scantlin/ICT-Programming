from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
'''
@app.route('/calculate_wave', methods=['POST'])
def calculate_wave():
    data = request.get_json()
    
    try:
        wavelength = float(data['wavelength'])
        frequency = float(data['frequency'])
        amplitude = float(data['amplitude'])
        
        # Calculate wave speed (v = λf)
        wave_speed = wavelength * frequency
        
        # Calculate period (T = 1/f)
        period = 1 / frequency if frequency != 0 else 0
        
        # Calculate angular frequency (ω = 2πf)
        angular_frequency = 2 * 3.14159 * frequency
        
        # Calculate wave number (k = 2π/λ)
        wave_number = 2 * 3.14159 / wavelength if wavelength != 0 else 0
        
        return jsonify({
            'success': True,
            'wave_speed': round(wave_speed, 2),
            'period': round(period, 4),
            'angular_frequency': round(angular_frequency, 2),
            'wave_number': round(wave_number, 4)
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)