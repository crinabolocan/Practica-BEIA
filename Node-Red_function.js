var payload = msg.payload;
var temperature = parseFloat(payload.temperature);
var humidity = parseFloat(payload.humidity);

var message = {
    topic: "/training/device/Crina-Bolocan/",
    payload: {
        temperature: temperature,
        humidity: humidity
    },
    qos: 0,
    retain: false
};

return message;

