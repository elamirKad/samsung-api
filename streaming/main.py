from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaPlayer
from fastapi import FastAPI, WebSocket
import json

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    pc = RTCPeerConnection()
    player = MediaPlayer("_neurosama - I don't want to be an engineer.mp3")
    track = player.audio
    pc.addTrack(track)

    @pc.on("track")
    def on_track(track):
        print("Track %s received" % track.kind)

    # Server creates offer
    offer = await pc.createOffer()
    await pc.setLocalDescription(offer)
    await websocket.send_text(json.dumps({"sdp": pc.localDescription.sdp, "type": pc.localDescription.type}))

    while True:
        data = await websocket.receive_text()
        msg = json.loads(data)
        if msg['type'] == 'answer':
            await pc.setRemoteDescription(RTCSessionDescription(**msg))

