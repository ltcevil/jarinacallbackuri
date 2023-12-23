import json
import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        audio_src = req_body.get('item', {}).get('audio_src', None)

        if not audio_src:
            raise ValueError("audio_src key not found")

    except (ValueError, json.JSONDecodeError) as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=400)

    return func.HttpResponse(f"Audio Source URL: {audio_src}", status_code=200)
