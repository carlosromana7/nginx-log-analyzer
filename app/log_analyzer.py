import re
from collections import Counter
from datetime import datetime

def parse_date(date_string):
    date_string = date_string.split()[0]
    return datetime.strptime(date_string, '%d/%b/%Y:%H:%M:%S')

def parse_nginx_log(log_file):
    log_pattern = re.compile(
        r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)" "(.*?)" .*?Server_Name:(\S+)'
    )
    requests = []
    for line in log_file:
        match = log_pattern.match(line)
        if match:
            ip, timestamp, request, status, bytes_sent, referer, user_agent, dash, server_name = match.groups()
            requests.append({
                'ip': ip,
                'timestamp': parse_date(timestamp),
                'request': request,
                'status': int(status),
                'bytes_sent': int(bytes_sent),
                'referer': referer,
                'user_agent': user_agent,
                'server_name': server_name
            })
    return requests

def analyze_logs(requests):
    total_requests = len(requests)
    ips = Counter(req['ip'] for req in requests)
    paths = Counter(req['request'].split()[1] for req in requests if len(req['request'].split()) > 1)
    status_codes = Counter(req['status'] for req in requests)
    user_agents = Counter(req['user_agent'] for req in requests)
    server_names = Counter(req['server_name'] for req in requests)
    total_traffic = sum(req['bytes_sent'] for req in requests)
    hours = Counter(req['timestamp'].strftime('%H') for req in requests)
    peak_hour = hours.most_common(1)[0][0]

    return {
        'total_requests': total_requests,
        'unique_ips': len(ips),
        'top_ips': ips.most_common(5),
        'top_paths': paths.most_common(5),
        'status_codes': dict(status_codes),
        'top_user_agents': user_agents.most_common(5),
        'top_server_names': server_names.most_common(5),
        'total_traffic': total_traffic,
        'peak_hour': peak_hour
    }

def parse_error_log(error_log_file):
    error_pattern = re.compile(
        r'\[(.*?)\] \[(.*?)\] \[.*?\] (.*)'
    )
    errors = []
    for line in error_log_file:
        match = error_pattern.match(line)
        if match:
            timestamp, level, message = match.groups()
            errors.append({
                'timestamp': timestamp,
                'level': level,
                'message': message
            })
    return errors

def analyze_errors(errors):
    total_errors = len(errors)
    error_levels = Counter(err['level'] for err in errors)
    top_errors = Counter(err['message'] for err in errors).most_common(5)

    return {
        'total_errors': total_errors,
        'error_levels': dict(error_levels),
        'top_errors': top_errors
    }

def get_log_analysis(log_file_path, error_log_file_path=None):
    try:
        with open(log_file_path, 'r') as log_file:
            requests = parse_nginx_log(log_file)
        analysis = analyze_logs(requests)

        if error_log_file_path:
            with open(error_log_file_path, 'r') as error_log_file:
                errors = parse_error_log(error_log_file)
            error_analysis = analyze_errors(errors)
            analysis['error_analysis'] = error_analysis

        return analysis
    except FileNotFoundError as e:
        return {"error": f"No se pudo encontrar el archivo: {str(e)}"}
    except Exception as e:
        return {"error": f"Ocurrió un error: {str(e)}"}
