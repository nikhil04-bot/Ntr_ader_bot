from flask import Flask, render_template
from strategy.smc_ai_strategy import smc_ai_strategy
from data.fetch_data import get_live_data

app = Flask(__name__)

@app.route('/')
def home():
    df = get_live_data()
    signal = smc_ai_strategy(df)
    return render_template('index.html', signal=signal)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)