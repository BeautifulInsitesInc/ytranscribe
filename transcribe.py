# --- TRANSCRIPTION FUNCTION
def yTranscribe(YouTubeText):
    count=0 # Used to protect agains potential infint loop
    RemoveCharacter = ":"
    Position = YouTubeText.find(RemoveCharacter)
    while Position != -1:
        #Set beginning and ending index to remove
        FrontPosition = Position -3            # Number of Characters to remove before character
        if FrontPosition <0:                   # If first character to remove is larger than first character, make it first character
            FrontPosition =0 
        RearPosition = Position +4             # Number of characters to remove after, aslo removes line return
        if RearPosition > len(YouTubeText):    # If last character to remove is past last character of file, make it the last.
            RearPosition = len(YouTubeText)
        YouTubeText = YouTubeText[:FrontPosition] + " " + YouTubeText[RearPosition:] # Make new Sample by adding everthing before removal to everything after and replace line return with space
        Position = YouTubeText.find(RemoveCharacter)
        count += 1
        if count > len(YouTubeText):                 # Used as emergency stop, incase of infinity loop
            break
    return(YouTubeText)