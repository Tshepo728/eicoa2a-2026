from system_logger import log_event
try:
    temperature = 135
    
    if temperature > 120:
        raise ValueError("Motor temperature is too high.")
    
except ValueError as error:
    log_event(f"SAFETY ERROR: {error}")
    print("Safety error recorded.")

print("All events have been recorded in system.log.")