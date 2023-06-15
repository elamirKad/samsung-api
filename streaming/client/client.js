document.getElementById("startButton").addEventListener("click", function() {
    startStreaming();
});

async function startStreaming() {
    const pc = new RTCPeerConnection();
    const ws = new WebSocket('ws://localhost:8000/ws');

    ws.onmessage = async (event) => {
        const msg = JSON.parse(event.data);
        if (msg.type === 'offer') {
            await pc.setRemoteDescription(new RTCSessionDescription(msg));
            const answer = await pc.createAnswer();
            await pc.setLocalDescription(answer);
            ws.send(JSON.stringify({"sdp": pc.localDescription.sdp, "type": pc.localDescription.type}));
        }
    };

    pc.ontrack = (event) => {
        document.getElementById('audio').srcObject = event.streams[0];
    };
}
