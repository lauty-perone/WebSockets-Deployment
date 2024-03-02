html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebSocket Chat</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="chat-container">
        <h1>Chat en Vivo</h1>
        <h2>Tu ID es: <span id="ws-id"></span></h2>
        <form class="message-form" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" placeholder="Escribe tu mensaje..." autocomplete="off"/>
            <button>Enviar</button>
        </form>
        <ul id='messages'></ul>
    </div>
    <script>
        var client_id = Date.now();
        document.querySelector("#ws-id").textContent = client_id;
        var ws = new WebSocket('wss://websockets-deployment.onrender.com/ws/' + client_id);
        ws.onmessage = function(event) {
            var messages = document.getElementById('messages');
            var message = document.createElement('li');
            var content = document.createTextNode(event.data);
            message.appendChild(content);
            messages.appendChild(message);
        };
        function sendMessage(event) {
            var input = document.getElementById("messageText");
            ws.send(input.value);
            input.value = '';
            event.preventDefault();
        }
    </script>
</body>
</html>
"""