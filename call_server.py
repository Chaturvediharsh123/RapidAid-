from fastapi import FastAPI, Request
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse

from main import process_complaint

app = FastAPI()


@app.post("/voice")
async def voice():

    response = VoiceResponse()

    response.say(
        "Welcome to AI civic helpline. Please describe your complaint after the beep."
    )

    response.record(
        action="/process",
        max_length=5
    )

    return Response(content=str(response), media_type="application/xml")


@app.post("/process")
async def process(request: Request):

    form = await request.form()

    recording_url = form.get("RecordingUrl")

    # simulated speech-to-text
    complaint_text = "garbage everywhere in sector9"

    issue, location, priority, department = process_complaint(complaint_text)

    response = VoiceResponse()

    response.say(
        f"Your complaint about {issue} has been registered."
    )

    return Response(content=str(response), media_type="application/xml")