from flask import Flask, render_template, request, jsonify
from scheduling_algorithms import FCFS, SJF, RoundRobin

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    processes = data['processes']
    algorithm = data['algorithm']
    quantum = data.get('quantum', 2)  # Default quantum for Round Robin

    if algorithm == 'FCFS':
        result = FCFS(processes)
    elif algorithm == 'SJF':
        result = SJF(processes)
    elif algorithm == 'RR':
        result = RoundRobin(processes, quantum)
    else:
        return jsonify({'error': 'Invalid algorithm'})

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
