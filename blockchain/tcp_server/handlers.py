'''
TODOs:

1. Handler to accept LRP (leader rotation proof) requests
2. Handler to accept epoch rotation propositions requests
3. Handler to accept FP (finalization proof) requests


API routes

1. GET Handler to return block by ID
2. GET Handler to return AFP (aggregated finalization proof) by block ID
3. GET Handler to return AEFP (aggregated epoch finalization proof) by epoch index
4. GET Handler to return assumption about first block

'''


async def handle_request(data: dict) -> dict:
    command = data.get("command")
    if command == "ping":
        return {"response": "pong"}
    return {"error": "Unknown command"}
