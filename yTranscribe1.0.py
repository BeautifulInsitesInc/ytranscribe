# --- GET SAMPLE TRANSRIPTION FROM FILE TO PROCESS
ImportFile = "yTranscribe\Sample.txt"
ExportFile = r'yTranscribe\Converted.txt'
Sample = open(ImportFile, 'r').read()
print(Sample) #Display original in terminal

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
        if count > len(Sample):                 # Used as emergency stop, incase of infinity loop
            break
    return(YouTubeText)

# --- PROCESS SAMPLE AND OUTPUT
Processed = yTranscribe(Sample)
print(Processed)

# Export result to file
with open(ExportFile, 'w') as Export:
    Export.write(Processed)
Export.close
#msgBox("Exported to converted.txt")