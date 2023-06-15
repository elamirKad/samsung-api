import asyncio
import json
import threading
import wave

import pyaudio
from aiofile import AIOFile
from aiortc import RTCPeerConnection, RTCSessionDescription, RTCRtpReceiver
from aiortc.contrib.media import MediaRecorder
import websockets

class AudioPlayer:
    def __init__(self):
        self.p = pyaudio.PyAudio()

    def play(self, filename):
        def _play():
            CHUNK = 1024
            wf = wave.open(filename, 'rb')
            stream = self.p.open(format=self.p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
            data = wf.readframes(CHUNK)
            while data != '':
                stream.write(data)
                data = wf.readframes(CHUNK)
            stream.stop_stream()
            stream.close()
        threading.Thread(target=_play).start()

    def stop(self):
        self.p.terminate()

player = AudioPlayer()

async def client():
    async with websockets.connect('ws://localhost:8000/ws') as websocket:
        pc = RTCPeerConnection()
        recorder = MediaRecorder('received.wav')

        @pc.on("track")
        async def on_track(track):
            print("Track %s received" % track.kind)
            recorder.addTrack(track)
            await recorder.start()

        @pc.on("datachannel")
        async def on_datachannel(channel):
            @channel.on("message")
            async def on_message(message):
                if isinstance(message, str) and message.startswith("file:"):
                    filename = message.split(":", 1)[1]
                    player.play(filename)

        while True:
            msg = await websocket.recv()
            msg = json.loads(msg)
            if msg['type'] == 'offer':
                await pc.setRemoteDescription(RTCSessionDescription(**msg))
                answer = await pc.createAnswer()
                await pc.setLocalDescription(answer)
                await websocket.send(json.dumps({"sdp": pc.localDescription.sdp, "type": pc.localDescription.type}))

asyncio.run(client())
