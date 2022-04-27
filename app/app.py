import os
from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Summary
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
csrf = CSRFProtect(app)
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0')
duration = Summary('duration_compute_seconds', 'Time spent in the compute() function')

@duration.time()
@app.route('/')
def hello_world():
   return render_template('index.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=False, host='0.0.0.0', port=port)
