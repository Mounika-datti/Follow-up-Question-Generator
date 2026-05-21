interview_sessions = {}

def get_followup_count(session_id):

    if session_id not in interview_sessions:
        interview_sessions[session_id] = 0

    return interview_sessions[session_id]

def increment_followup(session_id):

    if session_id not in interview_sessions:
        interview_sessions[session_id] = 0

    interview_sessions[session_id] += 1