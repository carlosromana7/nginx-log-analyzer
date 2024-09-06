from flask import Flask, render_template
from log_analyzer import get_log_analysis

app = Flask(__name__)

@app.route('/')
def dashboard():
    log_file_path = '/var/log/nginx/access.log'
    analysis = get_log_analysis(log_file_path)

    # Asegúrate de que todos los datos necesarios estén presentes
    if 'error' not in analysis:
        analysis['top_ips'] = analysis.get('top_ips', [])
        analysis['status_codes'] = analysis.get('status_codes', {})
        analysis['top_paths'] = analysis.get('top_paths', [])
        analysis['top_user_agents'] = analysis.get('top_user_agents', [])
        analysis['top_server_names'] = analysis.get('top_server_names', [])

    return render_template('dashboard.html', data=analysis)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
