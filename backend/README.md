just a filler

main.py is working backend
i was able to talk to ollama model and got a response
only thing to look into is why i cant send more than once 
i have to update the page to get a new response 

User opens app
    → React calls POST /session/new
    → FastAPI creates a session in SQLite, returns session_id
    → React stores that session_id

User sends a message
    → React sends { session_id, message } to POST /chat
    → FastAPI loads that session's history from SQLite
    → Builds the full conversation prompt
    → Calls Ollama
    → Saves both the user message and AI reply to SQLite
    → Returns the reply to React

id — unique identifier for the message itself
session_id — foreign key, links back to which session this belongs to
role — "user" or "assistant"
content — the actual text of the message
created_at — timestamp