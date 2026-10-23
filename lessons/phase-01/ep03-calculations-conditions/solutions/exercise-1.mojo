def main():
    var temperature: Int = -1
    var threshold: Int = 30
    print("Temperature:", temperature)
    if temperature < 0:
        print("Status: INVALID")
    elif temperature >= threshold:
        print("Status: WARNING")
    else:
        print("Status: OK")
