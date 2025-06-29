def smc_ai_strategy(df):
    last = df.iloc[-1]
    prev = df.iloc[-2]
    trend = "UP" if last['high'] > prev['high'] and last['low'] > prev['low'] else "DOWN"

    breaker_zone = {
        "CALL": df[df['close'] < df['open']].iloc[-3]['close'],
        "PUT": df[df['close'] > df['open']].iloc[-3]['close']
    }

    body = abs(last['close'] - last['open'])
    wick = last['high'] - last['low']
    rejection = body < wick * 0.4

    if trend == "UP" and last['low'] <= breaker_zone["CALL"] and rejection:
        sl = last['low']
        entry = last['close']
        target = entry + (entry - sl) * 2
        return {
            "signal": "CALL",
            "entry": round(entry, 2),
            "sl": round(sl, 2),
            "target": round(target, 2),
            "reason": "SMC breaker + bullish rejection + trend up"
        }

    if trend == "DOWN" and last['high'] >= breaker_zone["PUT"] and rejection:
        sl = last['high']
        entry = last['close']
        target = entry - (sl - entry) * 2
        return {
            "signal": "PUT",
            "entry": round(entry, 2),
            "sl": round(sl, 2),
            "target": round(target, 2),
            "reason": "SMC breaker + bearish rejection + trend down"
        }

    return None
